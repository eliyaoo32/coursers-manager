from controllers.AbsCoursesController import AbsCoursesController
from models.Course import Course
from models.Chapter import Chapter


class ModelCoursesController(AbsCoursesController):
    def create_course(self, course_name, logo_path, category, progress=0):
        return Course.create(name=course_name, logo_path=logo_path, category=category, progress=progress)

    def create_chapter(self, course, name, series_no, progress=0):
        return Chapter.create(name=name, series_no=series_no, progress=progress, course=course)
