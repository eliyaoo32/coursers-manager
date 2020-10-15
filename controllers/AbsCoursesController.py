from abc import ABC, abstractmethod


class AbsCoursesController(ABC):
    @abstractmethod
    def create_course(self, course_name, logo_path, category, progress=0):
        pass
