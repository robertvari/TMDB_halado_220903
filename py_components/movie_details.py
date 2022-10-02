from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl
import tmdbsimple as tmdb
from datetime import datetime, timedelta
from py_components.resources import get_poster


class MovieDetails(QObject):
    movie_changed = Signal()

    def __init__(self):
        super().__init__()
        self._movie_data = None
    
    @Slot(int)
    def set_movie(self, movie_id):
        movie = tmdb.Movies(movie_id)
        self._movie_data = movie.info()
        self.movie_changed.emit()

    def _get_title(self):
        if self._movie_data:
            return self._movie_data.get("title")
        return ""

    def _get_overview(self):
        if self._movie_data:
            return self._movie_data.get("overview")
        return ""

    def _get_tagline(self):
        if self._movie_data:
            return self._movie_data.get("tagline")
        return ""

    def _get_genres(self):
        if self._movie_data:
            genre_names = [i["name"] for i in self._movie_data.get("genres")]
            return ", ".joint(genre_names)
        return ""

    def _get_poster(self):
        if self._movie_data:
            return get_poster(self._movie_data.get("poster_path"))
        return QUrl()

    def _get_date_obj(self):
        return datetime.strptime(self._movie_data.get("release_date"), "%Y-%m-%d")

    def _get_release_date(self):
        if self._movie_data:
            return self._get_date_obj().strftime("%Y %B %d")
        
        return ""
    
    def _get_runtime(self):
        if self._movie_data:
            tdelta = timedelta(seconds=self._movie_data.get("runtime"))
            d, h, m = str(tdelta).split(":")
            return f"{int(h)}h {int(m)}m"
        return ""

    title = Property(str, _get_title, notify=movie_changed)
    overview = Property(str, _get_overview, notify=movie_changed)
    tagline = Property(str, _get_tagline, notify=movie_changed)
    genres = Property(str, _get_genres, notify=movie_changed)
    poster = Property(QUrl, _get_poster, notify=movie_changed)
    release_date = Property(str, _get_release_date, notify=movie_changed)
    runtime = Property(str, _get_runtime, notify=movie_changed)