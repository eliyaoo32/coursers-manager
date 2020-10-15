from peewee import *
from . import BaseModel


class Category(BaseModel):
    name = CharField(unique=True)
