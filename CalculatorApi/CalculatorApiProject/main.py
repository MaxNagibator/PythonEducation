from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/calc/{a}/plus/{b}")
async def say_hello(a: int, b: int):
    return a + b

class Item(BaseModel):
    a: int
    b: int

@app.post("/calc/mult2")
async def say_hello(item: Item):
    return item.a * item.b

@app.post("/calc/mult")
async def say_hello(a: int, b: int):
    return a * b
