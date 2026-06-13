from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg2.extras

from database import get_connection, init_db
from schemas import UserCreate, UserResponse, CarsCreate, CarsResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/users", response_model=list[UserResponse])
def get_users():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

    
@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute(
        "INSERT INTO users (name, age) VALUES (%s, %s) RETURNING *",
        (user.name, user.age)
    )

    new_user = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    return new_user



@app.get("/cars", response_model=list[CarsResponse])
def get_cars():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("SELECT * FROM cars")
    cars = cursor.fetchall()

    cursor.close()
    conn.close()

    return cars

    
@app.post("/cars", response_model=CarsResponse, status_code=201)
def create_cars(car: CarsCreate):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute(
        "INSERT INTO cars (name, model, yom) VALUES (%s, %s, %s) RETURNING *",
        (car.name, car.model, car.yom)
    )

    new_car = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    return new_car

@app.on_event("startup")
def startup():
    init_db()