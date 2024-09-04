from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    """_summary_

    Args:
        item_id (int): _description_
        item (Item): _description_
        user (User): _description_
        importance (Annotated[int, Body, optional): _description_. Defaults to 0)].
        q (str | None, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
