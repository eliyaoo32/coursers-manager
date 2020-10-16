import os
from os.path import basename
from typing import List
from distutils.dir_util import copy_tree

from data.ChapterData import ChapterData
from libs.config import config
from controllers.AbsCoursesController import AbsCoursesController
from loaders.ILoader import ILoader


class CourseFolderLoader(ILoader):
    def __init__(self, original_course_path):
        self._original_course_path = original_course_path
        self._course_name = basename(self._original_course_path)

    def load_course(self, courses_controller: AbsCoursesController):
        # Load course files
        self._copy_course_from_original_folder()

        # Create course
        course = courses_controller.create_course(category=None, course_name=self._course_name, logo_path="")

        # Create chapters
        chapters_data: List[ChapterData] = get_chapters_from_folder(self._course_path)
        for chapter_data in chapters_data:
            chapter = courses_controller.create_chapter(
                name=chapter_data.name,
                series_no=chapter_data.series_no,
                course=course
            )

    def _copy_course_from_original_folder(self):
        copy_tree(self._original_course_path, self._course_path)

    @property
    def _course_path(self):
        storage_path = config['COURSE_FOLDER_LOADER']['courses_folder']
        return os.path.join(storage_path, self._course_name)


# Utils
def get_chapters_from_folder(folder_path) -> List[ChapterData]:
    chapters_folder = [
        f.path
        for f in os.scandir(folder_path) if f.is_dir()
    ]
    chapters: List[ChapterData] = [
        ChapterData(**extract_course_folder_name(basename(folder_path)))
        for folder_path in chapters_folder
    ]

    return chapters


def extract_course_folder_name(folder_name: str):
    series_no, *name = folder_name.split(" ")
    series_no = int(series_no)
    name = " ".join(name).strip()

    return {
        "series_no": series_no,
        "name": name
    }
