from typing import List

from fastapi import APIRouter

from api import models, schemas

api_router = APIRouter()


@api_router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate):
    item = models.Item.objects.create(**item.dict())

    return item


@api_router.get("/items", response_model=List[schemas.Item])
def read_items():
    items = list(models.Item.objects.all())

    return items


@api_router.get("/users", response_model=List[schemas.User_Pydantic])
def read_items():
    users = list(models.User.objects.all())

    return users


@api_router.post("/user", response_model=schemas.User_Pydantic)
def create_item(user: schemas.UserCreate):
    user = models.Item.objects.create(**user.dict())

    return user
