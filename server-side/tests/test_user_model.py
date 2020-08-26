


def test_model(user):
    assert user.firstname == 'testn'

def test_user_login(user, client):
    res = client.post('/login', json={
        'email': user.email,
        'password': 'passw'
    })
    assert res.status_code == 200
    assert res.get_json().get('access_token')

def test_user_reg(client):
    res = client.post('/register', json={
        'firstname': 'testname',
        'lastname': 'testsurname',
        'email': 'testingmail@mail.com',
        'password': 'passw'
    })
    assert res.status_code == 200
    assert res.get_json().get('access_token')


