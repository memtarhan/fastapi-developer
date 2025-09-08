import uvicorn
from typing import Dict
from typing import Dict, List
from pydantic import BaseModel, SecretStr, HttpUrl, Json, validator, field_validator
from fastapi import FastAPI

app = FastAPI()


class Product(BaseModel):
    prodId: int
    prodName: str
    price: float
    stock: int
    Inventory_val: float


class ProductVal(BaseModel):
    prodId: int
    prodName: str
    Inventory_val: float


@app.post("/product/", response_model=ProductVal)
async def add_new(product: Product):
    product.Inventory_val = product.price * product.stock
    return product


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
