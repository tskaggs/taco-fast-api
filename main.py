from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from connections import deta_base_connect

db_toppings = deta_base_connect.connect_toppings()
db_tacos = deta_base_connect.connect_tacos()


class Topping(BaseModel):
    name: str
    description: Optional[str] = None


class Taco(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    random: bool = None
    toppings: list


app = FastAPI()


@app.get("/tacos/name/")
async def get_taco_by_name(taco_name: Optional[str] = None):
    if taco_name:
        return db_tacos.fetch({"name": taco_name})

    return db_tacos.fetch()


@app.get("/tacos/")
async def find_one_taco_by_id(item_id: Optional[str] = None):
    if item_id:
        return db_tacos.get(item_id)

    return db_tacos.fetch()


@app.post("/tacos")
async def create_taco(taco: Taco):
    taco_dict = taco.dict()
    new_taco = db_tacos.put(taco_dict)
    return new_taco


@app.delete("/tacos")
async def delete_taco(tacos_id: str):
    db_tacos.delete(tacos_id)
    return


@app.get("/topping/name/")
async def get_topping_by_name(topping_name: Optional[str] = None):
    if topping_name:
        return db_toppings.fetch({"name": topping_name})

    return db_toppings.fetch()


@app.get("/topping/")
async def get_topping_by_name(topping_id: Optional[str] = None):
    if topping_id:
        return db_toppings.get(topping_id)

    return db_toppings.fetch()


@app.post("/topping")
async def create_topping(topping: Topping):
    topping_dict = topping.dict()
    new_topping = db_toppings.put(topping_dict)
    return new_topping


@app.delete("/topping")
async def delete_topping(topping_id: str):
    db_toppings.delete(topping_id)
    return
