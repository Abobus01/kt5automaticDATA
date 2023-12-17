from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List

class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class User(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: EmailStr
    phone: str
    userStatus: int

class Pet(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: List[HttpUrl]
    tags: List[Tag]

class Order(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool