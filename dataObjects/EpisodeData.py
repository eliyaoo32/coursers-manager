from dataclasses import dataclass


@dataclass
class EpisodeData:
    name: str
    series_no: int
    video_path: str
    thumbnail_path: str
