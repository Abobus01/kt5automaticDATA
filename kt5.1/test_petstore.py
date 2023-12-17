import allure
import pytest
import requests
from pydantic import BaseModel, EmailStr

BASE_URL = "https://dog.ceo/dog-api"

class User(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: EmailStr
    phone: str
    userStatus: int

class Order(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool

@allure.feature("Petstore API Tests")
class TestPetstoreAPI:

    @allure.story("User Operations")
    @allure.title("Create User")
    @pytest.mark.parametrize("user_data", [
        {"id": 1, "username": "john_doe", "firstName": "John", "lastName": "Doe", "email": "john.doe@example.com", "phone": "1234567890", "userStatus": 0},
    ])
    def test_create_user(self, user_data):
        with allure.step("Send POST request to create user"):
            response = requests.post(f"{BASE_URL}/user", json=user_data)
            assert response.status_code == 200

        with allure.step("Validate created user"):
            created_user = User(**response.json())
            assert created_user.username == user_data["username"]

    @allure.story("User Operations")
    @allure.title("Get User by Username")
    @pytest.mark.parametrize("username", ["john_doe", "another_user"])
    def test_get_user_by_username(self, username):
        with allure.step(f"Send GET request to get user by username: {username}"):
            response = requests.get(f"{BASE_URL}/user/{username}")
            assert response.status_code == 200

        with allure.step("Validate retrieved user"):
            retrieved_user = User(**response.json())
            assert retrieved_user.username == username

    @allure.story("Store Operations")
    @allure.title("Create Order")
    @pytest.mark.parametrize("order_data", [
        {"id": 1, "petId": 1, "quantity": 1, "shipDate": "2023-01-01T12:00:00Z", "status": "placed", "complete": False},
    ])
    def test_create_order(self, order_data):
        with allure.step("Send POST request to create order"):
            response = requests.post(f"{BASE_URL}/store/order", json=order_data)
            assert response.status_code == 200

        with allure.step("Validate created order"):
            created_order = Order(**response.json())
            assert created_order.petId == order_data["petId"]

    @allure.story("Store Operations")
    @allure.title("Get Order by ID")
    @pytest.mark.parametrize("order_id", [1, 2])
    def test_get_order_by_id(self, order_id):
        with allure.step(f"Send GET request to get order by ID: {order_id}"):
            response = requests.get(f"{BASE_URL}/store/order/{order_id}")
            assert response.status_code == 200

        with allure.step("Validate retrieved order"):
            retrieved_order = Order(**response.json())
            assert retrieved_order.id == order_id