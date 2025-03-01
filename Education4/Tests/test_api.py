import pytest
from MyFirstApi.app import create_app

def test_passing():
    assert 1 == 1
    print(1)
    flask_app = create_app()
    print(23333)
    with flask_app.test_client() as test_client:
        print(3)
        response = test_client.get('/about')
        print(4)
        assert response.status_code == 200
        assert response.text == '<body><b>This is the about page ♥</b></body>'
