from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    """_summary_

    Args:
        item (Item): _description_

    Returns:
        _type_: _description_
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
