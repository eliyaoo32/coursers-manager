from dataclasses import dataclass


@dataclass
class ChapterData:
    name: str
    series_no: int
    progress: int = 0
