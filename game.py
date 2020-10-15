from loaders.ILoader import ILoader
from loaders.CourseFolderLoader import CourseFolderLoader

if __name__ == "__main__":
    COURSE_FOLDER = r'C:\Users\Eliyahu\Desktop\Study\General\The Complete Facebook Marketplace Dropshipping Masterclass'
    loader: ILoader = CourseFolderLoader(COURSE_FOLDER)
    loader.load_course(None)
