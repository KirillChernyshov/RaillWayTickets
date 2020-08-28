from datetime import datetime
from app import app, session
from app.model import *

#app = create_app()

def mockup():
    stations = [Station(name="лубянка-1", province="Рязанская область"),
                Station(name="искра-1", province="Рязанская область"),
                Station(name="боровое-1", province="Рязанская область"),
                Station(name="Ковылкиноб", province="Мордовия")]
    session.add_all(stations)
    session.commit()
    routes = [BaseRoute(Name="Рязань - Мордовия")]
    session.add_all(routes)
    session.commit()
    stops = [Stop(station_id=stations[0].id, route_id=routes[0].id, departure=datetime(2020, 10, 1, 0, 0)),
             Stop(station_id=stations[1].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 2, 0), departure=datetime(2020, 10, 1, 2, 5)),
             Stop(station_id=stations[2].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 4, 0)),
             Stop(station_id=stations[3].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 7, 0))]
    session.add_all(stops)
    session.commit()
    trains = [Train()]
    session.add_all(trains)
    session.commit()
    wagons = [Wagon(train_id=trains[0].id, type='type-1', places_count=5),
              Wagon(train_id=trains[0].id, type='type-2', places_count=4),
              Wagon(train_id=trains[0].id, type='type-3', places_count=2)]
    session.add_all(wagons)
    session.commit()
    schedules = [Schedule(train_id=trains[0].id, base_route_id=routes[0].id, departure_time=stops[0].departure)]
    session.add_all(schedules)
    session.commit()
    tickets = [Ticket(departure_stop=stops[2].id, arrival_stop=stops[3].id, cost=34, wagon_id=wagons[0].id, place_num=2,
                      schedule_id=schedules[0].id, is_booked=False),
               Ticket(departure_stop=stops[1].id, arrival_stop=stops[3].id, cost=34, wagon_id=wagons[1].id, place_num=3,
                      schedule_id=schedules[0].id, is_booked=False)]
    session.add_all(tickets)
    session.commit()


if __name__ == '__main__':
    app.run(debug=True)

