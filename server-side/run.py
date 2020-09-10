from datetime import datetime
from app import app, session, logger, session_lock
from app.model import *
import threading
import atexit

database_cleaning_thread = threading.Thread()


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        while self.stopped() is False:
            logger.info('thread begins the proccess')
            session_lock.acquire()
            now = datetime.now()
            tickets_to_delete = session.query(Ticket).filter(Ticket.book_end_date > now).all()
            if len(tickets_to_delete) != 0:
                print(str(len(tickets_to_delete)) + " outdated bookings found, commence deletion")
            for ticket in tickets_to_delete:
                session.delete(ticket)
            session.commit()
            session_lock.release()
            logger.info('thread proccess completed')
            self._stop_event.wait(4)
        logger.info('dataclean thread has stopped')

# app = create_app()

def mockup():
    users = [
        User(firstname='testn', lastname='testsg', email='testmail@mail.com', password='passw', role='client'),
        User(firstname='testmng', lastname='testmng', email='mngemail@mail.com', password='mngpassw', role='manager')
    ]
    session.add_all(users)
    stations = [Station(name="лубянка-1", province="Рязанская область"),
                Station(name="искра-1", province="Рязанская область"),
                Station(name="боровое-1", province="Рязанская область"),
                Station(name="Ковылкиноб", province="Мордовия")]
    session.add_all(stations)
    session.commit()
    routes = [BaseRoute(name="Рязань - Мордовия")]
    session.add_all(routes)
    session.commit()
    stops = [Stop(station_id=stations[0].id, route_id=routes[0].id, departure=datetime(2020, 10, 1, 0, 0)),
             Stop(station_id=stations[1].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 2, 0), departure=datetime(2020, 10, 1, 2, 5)),
             Stop(station_id=stations[2].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 4, 0), departure=datetime(2020, 10, 1, 4, 5)),
             Stop(station_id=stations[3].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 7, 0))]
    session.add_all(stops)
    session.commit()
    trains = [Train()]
    session.add_all(trains)
    session.commit()
    wagons = [Wagon(train_id=trains[0].id, type='Купе', places_count=5),
              Wagon(train_id=trains[0].id, type='Плацкартовый', places_count=4),
              Wagon(train_id=trains[0].id, type='Купе', places_count=2)]
    session.add_all(wagons)
    session.commit()
    schedules = [Schedule(train_id=trains[0].id, base_route_id=routes[0].id, departure_time=stops[0].departure)]
    session.add_all(schedules)
    session.commit()
    tickets = [
        Ticket(departure_stop_id=stops[2].id, arrival_stop_id=stops[3].id, cost=34, wagon_id=wagons[0].id, place=2,
               schedule_id=schedules[0].id, is_booked=False, user_id=users[0].id),
        Ticket(departure_stop_id=stops[1].id, arrival_stop_id=stops[3].id, cost=34, wagon_id=wagons[1].id, place=3,
               schedule_id=schedules[0].id, is_booked=False, user_id=users[0].id)]
    session.add_all(tickets)
    session.commit()


if __name__ == '__main__':
    database_cleaning_thread = StoppableThread()
    database_cleaning_thread.setDaemon(True)
    database_cleaning_thread.start()
    app.run(debug=True)
    database_cleaning_thread.stop()
