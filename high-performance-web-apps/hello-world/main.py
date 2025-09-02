from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/{name}/{id}")
async def user(name: str, id: int):
    return {"name": name, "id": id}


# Path Parameters
@app.get("/employee/{name}/{age}")
async def get_employee1(name: str, age: int):
    return {"name": name, "age": age}


# Query Parameters
@app.get("/employee/{name}")
async def get_employee2(name: str, age: int):
    return {"name": name, "age": age}


# Default Parameters
@app.get("/employee/{name}")
async def get_employee3(name: str, age: int = 20):
    return {"name": name, "age": age}


# Optional Parameters
@app.get("/employee/{name}")
async def get_employee4(name: str, age: Optional[int] = None):
    return {"name": name, "age": age}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
