from datetime import datetime
from app import app, session
from app.model import *

#app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

def mockup():
    stations = [Station(name="лубянка-1", province="Рязанская область"),
                Station(name="искра-1", province="Рязанская область"),
                Station(name="боровое-1", province="Рязанская область")]
    routes = [BaseRoute(Name="Рязань Лубянка - Искра")]
    stops = [Stop(station_id=stations[0].id, route_id=routes[0].id,
                  departure=datetime(2020, 10, 1, 0, 0)),
             Stop(station_id=stations[1].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 2, 0), departure=datetime(2020, 10, 1, 2, 5)),
             Stop(station_id=stations[2].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 4, 0))]
    trains = [Train()]
    wagons = [Wagon(train_id=trains[0].id, type='type-1', places_count=50),
              Wagon(train_id=trains[0].id, type='type-2', places_count=40),
              Wagon(train_id=trains[0].id, type='type-3', places_count=20)]
    schedules = [Schedule(train_id=trains[0].id, base_route_id=routes[0].id,
                          departure_time=routes[0].departure)]
    app.session.add_all(stations)
    app.session.add_all(routes)
    app.session.add_all(stops)
    app.session.add_all(trains)
    app.session.add_all(wagons)
    app.session.add_all(schedules)
