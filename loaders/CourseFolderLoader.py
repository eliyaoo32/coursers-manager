import os

from libs.config import config
from controllers.AbsCoursesController import AbsCoursesController
from loaders.ILoader import ILoader


class CourseFolderLoader(ILoader):
    def __init__(self, folder_path):
        self._folder_path = folder_path
        self._course_name = os.path.basename(self._folder_path)
        self._courses_path = config['COURSE_FOLDER_LOADER']['courses_folder']

    def load_course(self, courses_controller: AbsCoursesController):
        self._copy_course_folder()

    def _copy_course_folder(self):
        course_path = os.path.join(self._courses_path, self._course_name)
        copy_tree(self._folder_path, course_path)
