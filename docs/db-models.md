# coursers-manager
### Course:
1) ID
2) Name
3) Logo
4) Chapters
5) Progress Status (0-100)
6) Category
### Chapter
1) ID
2) Name
3) Series No
4) Progress (0-100)
5) Episodes
### Episode
1) ID
2) Name
3) Video Path
4) Thumbnail
5) Status (Watched/Not Watched)

## DB Design
* Category(id, name)
* Course(id, name, logo_path, progress, category_id)
* Chapter(id, name, series_no, progress, course_id)
* Episode(id, name, video_path, thumbnail_path, status, chapter_id)
