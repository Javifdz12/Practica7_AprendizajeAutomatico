from app import app
import pytest
import requests
@pytest.fixture
def client():
	app.config['TESTING']=True
	with app.test_client() as client:
		yield client
def test_hello(client):
	response=client.get('/')
	assert response.status_code==200
	assert b'Hola esta es mi aplicacion' in response.data
def test_saludo(client):
	response=client.get('/saludo/John')
	assert response.status_code==200
	assert b'Hola John' in response.data
def test_pagina(client):
	response=client.get('/pagina')
	assert response.status_code==200
	assert b'Bienvenido a mi pagina' in response.data
