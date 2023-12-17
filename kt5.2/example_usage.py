from models import User, Pet, Order

user_data = {
    "id": 1,
    "username": "john_doe",
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phone": "1234567890",
    "userStatus": 0
}

pet_data = {
    "id": 1,
    "category": {"id": 1, "name": "Dog"},
    "name": "Buddy",
    "photoUrls": ["https://example.com/buddy.jpg"],
    "tags": [{"id": 1, "name": "Friendly"}]
}

order_data = {
    "id": 1,
    "petId": 1,
    "quantity": 1,
    "shipDate": "2023-01-01T12:00:00Z",
    "status": "placed",
    "complete": False
}


user_model = User(**user_data)
pet_model = Pet(**pet_data)
order_model = Order(**order_data)


print("User JSON:", user_model.json())
print("Pet JSON:", pet_model.json())
print("Order JSON:", order_model.json())