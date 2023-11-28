from fastapi import FastAPI, HTTPException
from beanie import init_beanie
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()


client = MongoClient #(("mongodb+srv://{cluester}{passoword}.mongodb.net/"))
database_name = "aliest"
init_beanie(client, database_name)

class Product(BaseModel):
    name: str
    description: str = ""
    cnpj: int
    consult: str


@app.get("/")
async def read_root():
    try:
        products = await Product.find().to_list()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/products/{product_id}")
async def read_product(product_id: str):
    try:
        product = await Product.get(product_id)
        return product.dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
