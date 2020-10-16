from controllers.AbsCoursesController import AbsCoursesController
from dataObjects.EpisodeStatus import EpisodeStatus
from models.Course import Course
from models.Chapter import Chapter
from models.Episode import Episode


class ModelCoursesController(AbsCoursesController):
    def create_course(self, course_name, logo_path, category, progress=0):
        return Course.create(name=course_name, logo_path=logo_path, category=category, progress=progress)

    def create_chapter(self, course, name, series_no, progress=0):
        return Chapter.create(name=name, series_no=series_no, progress=progress, course=course)

    def create_episode(self, name: str, video_path: str, thumbnail_path: str, status: EpisodeStatus, chapter):
        return Episode.create(
            name=name, video_path=video_path, thumbnail_path=thumbnail_path,
            status=status, chapter=chapter
        )
