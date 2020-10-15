from peewee import Model, SqliteDatabase
from libs.config import config

db = SqliteDatabase(config['DATA']['db_path'])


class BaseModel(Model):
    class Meta:
        database = db


def create_tables():
    from .Category import Category
    from .Course import Course
    from .Chapter import Chapter
    from .Episode import Episode

    db.create_tables([Category, Course, Chapter, Episode])
