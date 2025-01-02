from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # decorador decora uma função
def read_root():
    return {"Hello": "World"}

@app.get("/jornada")
def read_jornada():
    return {"Minha primeira": "API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# if __name__ == "__main__":
#     print(read_root())
#     print(read_jornada())