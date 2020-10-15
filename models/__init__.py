from peewee import Model, SqliteDatabase

db = SqliteDatabase('courses.db')


class BaseModel(Model):
    class Meta:
        database = db


def create_tables():
    from .Category import Category
    from .Course import Course
    from .Chapter import Chapter
    from .Episode import Episode

    db.create_tables([Category, Course, Chapter, Episode])
