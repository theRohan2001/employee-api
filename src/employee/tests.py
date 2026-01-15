import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import Employee

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def auth_client(create_user, api_client):
    user = create_user(username='testuser', password='password')
    # Obtain token
    response = api_client.post('/api/token/', {'username': 'testuser', 'password': 'password'})
    token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return api_client

@pytest.fixture
def employee(db):
    return Employee.objects.create(
        name="John Doe",
        email="john@example.com",
        department="Engineering",
        role="Developer"
    )

@pytest.mark.django_db
class TestAuthentication:
    def test_token_obtain_pair(self, api_client, create_user):
        create_user(username='authuser', password='password')
        response = api_client.post('/api/token/', {
            'username': 'authuser',
            'password': 'password'
        })
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_token_obtain_pair_invalid(self, api_client):
        response = api_client.post('/api/token/', {
            'username': 'wrong',
            'password': 'wrong'
        })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
class TestEmployeeCRUD:
    def test_list_employees_unauthenticated(self, api_client):
        response = api_client.get('/api/employees/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_list_employees(self, auth_client, employee):
        response = auth_client.get('/api/employees/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) >= 1
        assert response.data['results'][0]['email'] == employee.email

    def test_create_employee(self, auth_client):
        data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "department": "HR",
            "role": "Manager"
        }
        response = auth_client.post('/api/employees/', data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == data['name']
        assert Employee.objects.count() >= 1

    def test_retrieve_employee(self, auth_client, employee):
        response = auth_client.get(f'/api/employees/{employee.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == employee.name

    def test_update_employee(self, auth_client, employee):
        data = {
            "name": "John Updated",
            "email": "john@example.com", # Keep unique email
            "department": "Engineering",
            "role": "Senior Developer"
        }
        response = auth_client.put(f'/api/employees/{employee.id}/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "John Updated"
        assert response.data['role'] == "Senior Developer"
        
        employee.refresh_from_db()
        assert employee.name == "John Updated"

    def test_partial_update_employee(self, auth_client, employee):
        data = {"role": "Lead Developer"}
        response = auth_client.patch(f'/api/employees/{employee.id}/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['role'] == "Lead Developer"

    def test_delete_employee(self, auth_client, employee):
        response = auth_client.delete(f'/api/employees/{employee.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Employee.objects.filter(id=employee.id).exists()
