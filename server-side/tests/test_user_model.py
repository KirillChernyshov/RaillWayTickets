


def test_model(user):
    assert user.name == 'testn'

def test_user_login(user, client):
    res = client.post('/login', json={
        'email': user.email,
        'password': 'passw'
    })
    assert res.status_code == 200
    assert res.get_json().get('access_token')

def test_user_reg(client):
    res = client.post('/register', json={
        'name': 'testname',
        'surname': 'testsurname',
        'email': 'testingmail@mail.com',
        'password': 'passw'
    })
    assert res.status_code == 200
    assert res.get_json().get('access_token')

