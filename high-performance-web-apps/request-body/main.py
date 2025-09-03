from fastapi import FastAPI
import uvicorn
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from typing import Dict, List
from pydantic import BaseModel, SecretStr, HttpUrl, Json, validator, field_validator


class Product(BaseModel):
    product_id: int
    name: str
    price: float
    stock: int

    class Config:
        json_schema_extra = {
            "example": {
                "product_id": 1,
                "name": "Ceiling Fan",
                "price": 2000,
                "stock": 50
            }
        }
        from_attributes = True  # orm_mode


Base = declarative_base()


class ProductORM(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(63), unique=True)
    price = Column(Float)
    stock = Column(Integer)


prod_alchemy = ProductORM(
    product_id=1,
    name='Ceiling Fan',
    price=2000,
    stock=50
)
product = Product.model_validate(prod_alchemy)

product2 = Product(
    product_id=2,
    name='LED Bulb',
    price=250,

    stock=50)
prod_alchemy = ProductORM(**product2.model_dump())

app = FastAPI()

products = []


@app.post("/product/")
async def add_new_product1(product: Product):
    products.append(product)
    return products


@app.post("/product/")
async def add_new_product2(product: Product):
    data = product.model_dump()
    price = data['price']
    if price > 5000:
        data['price'] = price + price * 0.1
        product.price = data['price']

    products.append(product)
    return products


class Student(BaseModel):
    student_id: int
    name: str
    subjects: Dict[str, int]


@app.post("/student/")
async def add_new_student1(student: Student):
    return student


class Employee(BaseModel):
    ID: str
    pwd: SecretStr
    salary: int
    details: Json
    FBProfile: HttpUrl

    @field_validator('ID')
    def alphanum(cls, x):
        if not x.isalnum():
            raise (ValueError('Must be alphanumeric'))


@app.post("/employee/")
async def add_new_employee1(employee: Employee):
    return employee


class Suppliers(BaseModel):
    supplierID: int
    supplierName: str


class Products(BaseModel):
    productID: int
    productName: str
    price: int
    suppler: List[Suppliers]


class Customers(BaseModel):
    custID: int
    custName: str
    products: List[Products]


@app.post("/customer")
async def get_customer(c1: Customers):
    return c1


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
