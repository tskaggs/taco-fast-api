from typing import Optional
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel


class ToppingName(str, Enum):
    cheese = "cheese"
    tomatoes = "tomatoes"
    carnitas = "carnitas"


class Taco(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    random: bool = None


fake_tacos_db = [
    {
        "name": "Jumbo Rocket",
        "description": "This sh*t is huge!!",
        "price": "18",
        "toppings": [
            {
                "name": "tomato",
                "description": "Gross."
            },
            {
                "name": "carnitas",
                "description": "I'll take all of it."
            }
        ]
    },
    {
        "name": "Party Rocket",
        "description": "Dance!!",
        "price": "13",
        "toppings": [
            {
                "name": "cheese",
                "description": "Put it all on my taco."
            },
            {
                "name": "carnitas",
                "description": "I'll take all of it."
            }
        ]
    },
    {
        "name": "Boring",
        "description": "ZzzzZzzzz",
        "price": "8",
        "toppings": [
            {
                "name": "cheese",
                "description": "Put it all on my taco."
            }
        ]
    }
]


app = FastAPI()


@app.get("/tacos/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_tacos_db[skip : skip + limit]


@app.get("/tacos/topping/{topping_name}")
async def get_(topping_name: ToppingName):
    if topping_name == ToppingName.tomatoes:
        return {"model_name": topping_name, "message": "Gross."}

    if topping_name == ToppingName.cheese:
        return {"model_name": topping_name, "message": "Put it all on my taco."}

    return {"model_name": topping_name, "message": "I'll take all of it."}


@app.get("/tacos/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.post("/tacos/")
async def create_item(taco: Taco):
    taco_dict = taco.dict()
    if taco.random:
        taco_dict.update({"taco": [
            {"tomato"}
        ]})
    return taco_dict
