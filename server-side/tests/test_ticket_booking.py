from app.model import *
from copy import copy
from operator import xor
from sqlalchemy.sql.expression import text


def test_ticket_booking(session, trains, routes, stops, schedules, wagons, user, tickets, client, manager_token):
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
    assert new_result.status == '200 OK'
    usr_tickets = client.post('/search_tickets', json={'usr_email': user.email},
                              headers={'Authorization': 'Bearer ' + manager_token})
    assert usr_tickets.status == '200 OK'
    assert len(usr_tickets.get_json()) == 4
    assert usr_tickets.get_json()[3]['is_booked'] is True
    verification_query = client.post('/verify_ticket', json={'ticket_id': usr_tickets.get_json()[3]['ticket_id']})
    assert verification_query.status == '401 UNAUTHORIZED'
    verification_query = client.post('/verify_ticket', json={'ticket_id': usr_tickets.get_json()[3]['ticket_id']},
                                     headers={'Authorization': 'Bearer ' + manager_token})
    assert verification_query.status == '200 OK'
    usr_tickets = client.post('/search_tickets', json={'usr_email': user.email},
                              headers={'Authorization': 'Bearer ' + manager_token})
    assert usr_tickets.status == '200 OK'
    assert len(usr_tickets.get_json()) == 4
    for i in range(4):
        print(i)
        print("ticket id - " + str(usr_tickets.get_json()[i]))
        assert (xor(usr_tickets.get_json()[i]['is_booked'], (i==2))) is False
    assert False == True


def test_ticket_placement(session, tickets, client, manager_token, stops, schedules, wagons, user):
    ticket_data = {'schedule_id': schedules[0].id, 'arrival_stop_id': stops[3].id,
                   'cost': 34, 'departure_stop_id': stops[0].id,
                   'wagon_id': wagons[0].id, 'place': 1}
    usr_tickets = client.post('/search_tickets', json={'usr_email': user.email},
                              headers={'Authorization': 'Bearer ' + manager_token})
    assert usr_tickets.status == '200 OK'
    assert len(usr_tickets.get_json()) == 3
    login = client.post('/login', json={'email': user.email, 'password': 'passw'})
    assert login.status == '200 OK'
    result = client.post('/place_ticket', json=ticket_data,
                         headers={'Authorization': 'Bearer ' + login.get_json()['access_token']})
    assert result.status == '401 UNAUTHORIZED'
    ticket_data = {'schedule_id': schedules[0].id, 'arrival_stop_id': stops[3].id,
                   'cost': 34, 'departure_stop_id': stops[0].id,
                   'wagon_id': wagons[0].id, 'place': 1, 'buyer_email': "randomerg.ru"}
    result = client.post('/place_ticket', json=ticket_data,
                         headers={'Authorization': 'Bearer ' + manager_token})
    assert result.status == '400 BAD REQUEST'
    ed_ticket_data = {'schedule_id': schedules[0].id, 'arrival_stop_id': stops[3].id,
                      'cost': 34, 'departure_stop_id': stops[0].id,
                      'wagon_id': wagons[0].id, 'place': 1, 'buyer_email': user.email}
    result = client.post('/place_ticket', json=ed_ticket_data,
                         headers={'Authorization': 'Bearer ' + manager_token})
    assert result.status == '200 OK'
    usr_tickets = client.post('/search_tickets', json={'usr_email': user.email},
                              headers={'Authorization': 'Bearer ' + manager_token})
    assert usr_tickets.status == '200 OK'
    assert len(usr_tickets.get_json()) == 4
    usr_tickets = client.post('/search_tickets', json={'ticket_id': 4},
                              headers={'Authorization': 'Bearer ' + manager_token})
    assert usr_tickets.status == '200 OK'
    assert len(usr_tickets.get_json()) == 1


# login = client.post('/login', json={'email': 'testmail@mail.com', 'password': 'passw'})


# ticket_data = {'schedule_id': 1, 'arrival_stop_id': 4,
#                   'cost': 34, 'departure_stop_id': 1,
#                   'wagon_id': 1, 'place': 1}

def test_ticket_deletion(session, tickets, client, manager_token, user_token):
    usrstr = 'Bearer ' + user_token
    mngstr = 'Bearer ' + manager_token
    user_tickets = client.get('/user_tickets', headers={'Authorization': usrstr})
    assert len(user_tickets.get_json()) == 3
    assert len(tickets) == 3
    delete_query = client.post('/delete_ticket', json={'ticket_id': tickets[0].id}, headers={'Authorization': usrstr})
    assert delete_query.status == '401 UNAUTHORIZED'
    delete_query = client.post('/delete_ticket', json={'ticket_id': tickets[2].id}, headers={'Authorization': usrstr})
    assert delete_query.status == '200 OK'
    delete_query = client.post('/delete_ticket', json={'ticket_id': tickets[0].id}, headers={'Authorization': mngstr})
    assert delete_query.status == '200 OK'
    user_tickets = client.get('/user_tickets', headers={'Authorization': usrstr})
    assert len(user_tickets.get_json()) == 1


def test_manager_ticket_search(session, tickets, client, manager_token, user_token):
    usrstr = 'Bearer ' + user_token
    mngstr = 'Bearer ' + manager_token
    ticket_query = client.post('/search_tickets', json={'usr_email': 'testmail@mail.com'},
                               headers={'Authorization': usrstr})
    assert ticket_query.status == '401 UNAUTHORIZED'
    ticket_query = client.post('/search_tickets', json={'usr_email': 'testmail@mail.com'},
                               headers={'Authorization': mngstr})
    assert ticket_query.status == '200 OK'
    assert len(ticket_query.get_json()) == 3
    ticket_query = client.post('/search_tickets', json={'ticket_id': 1},
                               headers={'Authorization': mngstr})
    print(ticket_query.get_json())
    assert ticket_query.get_json()[0]['ticket_id'] == tickets[0].id
