from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    age: int

class CarsCreate(BaseModel):
    name: str
    model: str
    yom: int

class CarsResponse(BaseModel):
    id: int
    name: str
    model: str
    yom: int    