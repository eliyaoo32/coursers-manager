from loaders.ILoader import ILoader
from models import create_tables
from loaders.CourseFolderLoader import CourseFolderLoader
from controllers.ModelCoursesController import ModelCoursesController

if __name__ == "__main__":
    create_tables()

    COURSE_FOLDER = r'C:\Users\Eliyahu\Desktop\Study\General\The Complete Facebook Marketplace Dropshipping Masterclass'
    loader: ILoader = CourseFolderLoader(COURSE_FOLDER)
    loader.load_course(ModelCoursesController())
