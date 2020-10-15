from peewee import *
from . import BaseModel
from .Chapter import Chapter


class Episode(BaseModel):
    name = CharField()
    video_path = CharField()
    thumbnail_path = CharField()
    status = CharField()
    chapter = ForeignKeyField(Chapter, backref='episodes')
