def test_ticket_booking(session, trains, routes, stops, schedules, wagons, user, tickets, client):
    result = client.post('/book_ticket', json={'arr_station_name': 'Ковылкиноб', 'arrival_time': stops[3].arriving,
                                               'cost': 34, 'dep_station_name': 'лубянка-1',
                                               'departure_time': stops[0].departure, 'place': 1,
                                               'route_name': 'Рязань - Мордовия', 'wagon_id': wagons[0].id})
    assert result.status == '401 UNAUTHORIZED'
