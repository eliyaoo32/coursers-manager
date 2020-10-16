import os
from glob import glob
from pydash import flatten
from typing import List


def get_directories_of_path(path: str) -> List[str]:
    return [
        f.path
        for f in os.scandir(path) if f.is_dir()
    ]


def get_all_playable_files(path: str) -> List[str]:
    extensions = ('*.mp4', '*.mp3', '*.flv', '*.avi')
    files = [
        glob(os.path.join(path, ext))
        for ext in extensions
    ]

    return flatten(files)


def remove_extension_of_filename(filename):
    return os.path.splitext(filename)[0]
