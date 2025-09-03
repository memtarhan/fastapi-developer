from typing import Optional

import uvicorn
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


# @app.get("/{name}/{id}")
# async def user(name: str, id: int):
#     return {"name": name, "id": id}
#
#
# # Path Parameters
# @app.get("/employee/{name}/{age}")
# async def get_employee1(name: str, age: int):
#     return {"name": name, "age": age}
#
#
# # Query Parameters
# @app.get("/employee/{name}")
# async def get_employee2(name: str, age: int):
#     return {"name": name, "age": age}
#
#
# # Default Parameters
# @app.get("/employee/{name}")
# async def get_employee3(name: str, age: int = 20):
#     return {"name": name, "age": age}
#
#
# # Optional Parameters
# @app.get("/employee/{name}")
# async def get_employee4(name: str, age: Optional[int] = None):
#     return {"name": name, "age": age}
#
#
# Order of Parameters
@app.get("/employee/{name}/branch/{branch_id}")
async def get_employee5(name: str, brname: str, branch_id: int, age: Optional[int] = None):
    employee = {'name': name, 'Branch': brname, 'Branch ID': branch_id, 'age': age}
    return employee


# Validating String Parameter
@app.get("/employee/{name}/branch/{branch_id}")
async def get_employee6(branch_id: int,
                        name: str = Path(..., min_length=10),
                        brname: str = Query(None, min_length=5, max_length=10),
                        age: Optional[int] = None):
    employee = {
        'name': name,
        'branch': brname,
        'branch_id': branch_id,
        'age': age,
    }

    return employee


# Validating Numeric Parameters
"""
The following types of validation criteria can be specified in the Path()
or Query() constructor:
• gt: Greater than
• ge: Greater than or equal
• lt: Less than
• le: Less than or equal
"""


@app.get("/employee/{name}/branch/{branch_id}")
async def get_employee7(name: str, brname: str, branch_id: int = Path(..., gt=0, le=100),
                        age: int = Query(None, ge=20, lt=61)):
    employee = {
        'name': name,
        'branch': brname,
        'branch_id ID': branch_id,
        'age': age
    }

    return employee


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
