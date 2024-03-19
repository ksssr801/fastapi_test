from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_discounted: bool
    is_deleted: bool

@app.get('/')
def home():
    print ("data : ", Item)
    return { 'data': 'Welcome to the home page.' }

@app.get('/item/{item_id}')
def get_item(item_id: int, q: Union[str, None] = None):
    print ("data: ", item_id)
    return { 'data': 'Getting item by id.' }

@app.put('/item/{item_id}')
def update_item(item_id: int, item: Item):
    print ("data: ", item_id, Item)
    return { 'data': 'Putting item by id.' }

@app.post('/item/')
def create_item(item: Item):
    print ("data: ", item)
    return { 'data': 'Item created.' }

@app.delete('/item/{item_id}')
def create_item(item_id: int):
    print ("data: ", item_id)
    return { 'data': 'Item deleted.' }


import uvicorn
uvicorn.run(app)