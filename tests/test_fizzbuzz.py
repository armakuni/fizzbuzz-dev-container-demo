import pytest
import requests

from src.fizzbuzz import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_int_div_by_3(client):
    response = client.get('/9')
    assert response.json == {"result": "Fizz"}, "Div by 3"

def test_int_div_by_5(client):
    response = client.get('/10')
    assert response.json == {"result": "Buzz"}, "Div by 5"

def test_int_div_by_3_and_5(client):
    response = client.get('/30')
    assert response.json == {"result": "FizzBuzz"}, "Div by 3 and 5"

def test_not_dev_by_3_or_5(client):
    response = client.get('/11')
    assert response.json == {"result": 11}, "Not Div by 3 and 5"

@pytest.mark.integration
def test_running_app_responds_with_fizzbuzz():
    response = requests.get('http://fizzbuzz:5000/15')
    assert response.json() == {"result": "FizzBuzz"}, "Integration, Div by 3 and 5"