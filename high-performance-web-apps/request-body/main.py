from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


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


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
