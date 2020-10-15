from peewee import *
from . import BaseModel
from .Course import Course


class Chapter(BaseModel):
    name = CharField()
    series_no = IntegerField()
    progress = IntegerField(default=0)
    course = ForeignKeyField(Course, backref='chapters')
