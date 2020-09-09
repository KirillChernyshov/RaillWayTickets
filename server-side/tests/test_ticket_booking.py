from app.model import *

def test_ticket_booking(session, trains, routes, stops, schedules, wagons, user, tickets, client):
    ticket_data = {'schedule_id': schedules[0].id, 'arrival_stop_id': stops[3].id,
                   'cost': 34, 'departure_stop_id': stops[0].id,
                   'wagon_id': wagons[0].id, 'place': 1}
    result = client.post('/book_ticket', json=ticket_data)
    assert result.status == '401 UNAUTHORIZED'
    login = client.post('/login', json={'email': user.email, 'password': 'passw'})
    assert login.status == '200 OK'
    assert session.query(Schedule).get(schedules[0].id).departure_time == schedules[0].departure_time
    new_result = client.post('/book_ticket', json=ticket_data,
                             headers={'Authorization': 'Bearer ' + login.get_json()['access_token']})
    print(new_result.get_json())
    assert new_result == '200 OK'

#login = client.post('/login', json={'email': 'testmail@mail.com', 'password': 'passw'})


#ticket_data = {'schedule_id': 1, 'arrival_stop_id': 4,
#                   'cost': 34, 'departure_stop_id': 1,
#                   'wagon_id': 1, 'place': 1}