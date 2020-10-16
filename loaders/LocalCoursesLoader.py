import os
from os.path import basename
from typing import List
from distutils.dir_util import copy_tree

from dataObjects.ChapterData import ChapterData
from dataObjects.EpisodeData import EpisodeData
from dataObjects.EpisodeStatus import EpisodeStatus
from libs.utils import get_directories_of_path, get_all_playable_files, remove_extension_of_filename
from libs.config import config
from controllers.AbsCoursesController import AbsCoursesController
from loaders.ILoader import ILoader


class LocalCoursesLoader(ILoader):
    def __init__(self, original_course_path):
        self._original_course_path = original_course_path
        self._course_name = basename(self._original_course_path)

    def loader_name(self):
        return "Local"

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

            episodes_data: List[EpisodeData] = get_episodes_from_folder(chapter_data.folder_path)
            for episode in episodes_data:
                courses_controller.create_episode(
                    name=episode.name,
                    video_path=episode.video_path,
                    thumbnail_path=episode.thumbnail_path,
                    status=EpisodeStatus.TO_WATCH,
                    chapter=chapter
                )

    def _copy_course_from_original_folder(self):
        copy_tree(self._original_course_path, self._course_path)

    @property
    def _course_path(self):
        storage_path = config['COURSE_FOLDER_LOADER']['courses_folder']
        return os.path.join(storage_path, self._course_name)


# Utils
def get_chapters_from_folder(folder_path) -> List[ChapterData]:
    chapters_folders = get_directories_of_path(folder_path)
    chapters: List[ChapterData] = [
        ChapterData(
            **extract_data_from_folder_name(basename(folder_path)),
            folder_path=folder_path
        )
        for folder_path in chapters_folders
    ]

    return chapters


def get_episodes_from_folder(folder_path) -> List[EpisodeData]:
    episodes_paths: List[str] = get_all_playable_files(folder_path)
    episodes: List[EpisodeData] = [
        EpisodeData(
            **extract_data_from_folder_name(basename(epi_path), True),
            video_path=epi_path,
            thumbnail_path=""
        )
        for epi_path in episodes_paths
    ]
    return episodes


def extract_data_from_folder_name(folder_name: str, remove_extension=False):
    series_no, *name = folder_name.split(" ")
    series_no = int(series_no)
    name = " ".join(name).strip()

    if remove_extension:
        name = remove_extension_of_filename(name)

    return {
        "series_no": series_no,
        "name": name
    }
