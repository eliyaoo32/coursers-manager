from abc import ABC, abstractmethod
from controllers.AbsCoursesController import AbsCoursesController


class ILoader(ABC):
    @abstractmethod
    def load_course(self, courses_controller: AbsCoursesController):
        pass
