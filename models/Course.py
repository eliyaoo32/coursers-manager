from peewee import *
from . import BaseModel
from .Category import Category


class Course(BaseModel):
    name = CharField(unique=True)
    logo_path = CharField()
    progress = IntegerField(default=0)
    category = ForeignKeyField(Category, backref='courses', null=True, default=None)
