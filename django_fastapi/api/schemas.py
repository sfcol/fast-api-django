from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


from tortoise import Model, fields, Tortoise, run_async
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields import CASCADE


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)


User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)


# Box Model

class Box(Model):
    id = fields.UUIDField(pk=True)
    label = fields.CharField(max_length=255)
    address = fields.CharField(max_length=255)
    lat = fields.DecimalField(decimal_places=6, max_digits=9)
    lon = fields.DecimalField(decimal_places=6, max_digits=9)


Box_Pydantic = pydantic_model_creator(Box, name="Box")
BoxIn_Pydantic = pydantic_model_creator(Box, name="BoxIn", exclude_readonly=True)


class Delivery(Model):
    id = fields.UUIDField(pk=True)
    sender = fields.ForeignKeyField("models.User", "deliveries_as_sender", on_delete=CASCADE, null=False)
    receiver = fields.ForeignKeyField("models.User", "deliveries_as_receiver", on_delete=CASCADE, null=False)


Delivery_Pydantic = pydantic_model_creator(Delivery, name="Delivery")
DeliveryIn_Pydantic = pydantic_model_creator(Delivery, name="DeliveryIn", exclude_readonly=True)
