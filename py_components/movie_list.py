from tkinter.messagebox import NO
from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex, \
    QObject, Signal, QRunnable, QThreadPool, Property, QSortFilterProxyModel, Slot
import tmdbsimple as tmdb
from py_components.resources import get_poster
import time
from datetime import datetime

tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5


class MovieList(QAbstractListModel):
    DataRole = Qt.UserRole
    download_progress_changed = Signal()
    movie_genres = tmdb.Genres().movie_list()["genres"]

    def __init__(self):
        super().__init__()

        self.job_pool = QThreadPool()
        self.job_pool.setMaxThreadCount(1)
        self.movie_list_worker = MovieListWorker()

        self._movies = []
        self._fetch_movies()

    @property
    def movies(self):
        return self._movies

    def _fetch_movies(self):
        self._reset()

        self.movie_list_worker.signals.movie_data_downloaded.connect(self._inser_movie)
        self.movie_list_worker.signals.task_started.connect(self.download_progress_changed)
        self.movie_list_worker.signals.task_finished.connect(self.download_progress_changed)
        self.job_pool.start(self.movie_list_worker)

    def _reset(self):
        self.beginResetModel()
        self._movies.clear()
        self.endResetModel()

    def _inser_movie(self, movie_data):
        self.download_progress_changed.emit()
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._movies.append(movie_data)
        self.endInsertRows()

    def rowCount(self, parent=QModelIndex) -> int:
        return len(self._movies)

    def roleNames(self):
        return {
            MovieList.DataRole: b'movie_data'
        }
    
    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == MovieList.DataRole:
            return self._movies[row]

    def _get_is_downloading(self):
        return self.movie_list_worker.is_working

    def _get_download_max_count(self):
        return self.movie_list_worker.max_count
    
    def _get_download_current_value(self):
        return self.movie_list_worker.current_count
    
    def _get_genre_list(self):
        return [i["name"] for i in self.movie_genres]

    # Python property for QML item types
    # name           Property type      getter method   optional setter    signal
    is_downloading = Property(bool, _get_is_downloading, notify=download_progress_changed)
    download_max_count = Property(int, _get_download_max_count, notify=download_progress_changed)
    download_current_value = Property(int, _get_download_current_value, notify=download_progress_changed)
    genre_list = Property(list, _get_genre_list, constant=True)


class MovieListProxy(QSortFilterProxyModel):
    genre_changed = Signal()
    sorting_changed = Signal()

    def __init__(self):
        super().__init__()
        self.sort(0, Qt.AscendingOrder)

        self._filter = ""
        self._genre = None
        self._sorting_options = [
            "Rating Descending",
            "Rating Ascending",
            "Release Date Descending",
            "Release Date Ascending",
            "Title (A-Z)",
            "Title (Z-A)"
        ]
        self._current_sorting = self._sorting_options[0]
    
    @Slot(str)
    def set_filter(self, search_string):
        self._filter = search_string
        self.invalidateFilter()
    
    def filterAcceptsRow(self, source_row, source_parent):
        movie_data = self.sourceModel().movies[source_row]

        if self._genre:
            return (self._filter.lower() in movie_data["title"].lower()) and (self._genre in movie_data["genres"])

        return self._filter.lower() in movie_data["title"].lower()
    
    def lessThan(self, source_left, source_right):
        left_movie = self.sourceModel().data(source_left, Qt.UserRole)
        right_movie = self.sourceModel().data(source_right, Qt.UserRole)

        if self._current_sorting == self._sorting_options[0]:
            return left_movie["vote_average"] > right_movie["vote_average"]
        elif self._current_sorting == self._sorting_options[1]:
            return left_movie["vote_average"] < right_movie["vote_average"]
        elif self._current_sorting == self._sorting_options[2]:
            return left_movie["date"] > right_movie["date"]
        elif self._current_sorting == self._sorting_options[3]:
            return left_movie["date"] < right_movie["date"]
        elif self._current_sorting == self._sorting_options[4]:
            return left_movie["title"] < right_movie["title"]
        elif self._current_sorting == self._sorting_options[5]:
            return left_movie["title"] > right_movie["title"]

    def _get_current_genre(self):
        return self._genre

    def _set_current_genre(self, new_genre):
        if new_genre == self._genre:
            self._genre = None
        else:
            self._genre = new_genre

        self.invalidateFilter()
        self.genre_changed.emit()

    def _get_sorting_option(self):
        return self._sorting_options

    def _get_current_sorting(self):
        return self._current_sorting

    @Slot(str)
    def _set_current_sorting(self, new_sorting):
        self._current_sorting = new_sorting
        self.sorting_changed.emit()
        self.invalidate()

    current_genre = Property(str, _get_current_genre, _set_current_genre, notify=genre_changed)
    sorting_options = Property(list, _get_sorting_option, constant=True)
    current_sorting = Property(str, _get_current_sorting, _set_current_sorting, notify=sorting_changed)


class WorkerSignals(QObject):
    movie_data_downloaded = Signal(dict)
    task_started = Signal()
    task_finished = Signal()

    def __init__(self):
        super().__init__()


class MovieListWorker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()
        self.tmdb_movies = tmdb.Movies()
        
        self.is_working = False
        self.max_count = 0
        self.current_count = 0

    def _get_genres(self, id_list):
        if not id_list:
            return []

        result = []
        for id in id_list:
            for genre_data in MovieList.movie_genres:
                if genre_data["id"] == id:
                    result.append(genre_data["name"])
                    break
        
        return result

    def stop(self):
        self.is_working = False

    def run(self):
        self.is_working = True
        self.signals.task_started.emit()

        popular_movies = self.tmdb_movies.popular(page=1)["results"]
        self.max_count = len(popular_movies)
        for movie_data in popular_movies:
            if not self.is_working:
                break

            datetime_obj = datetime.strptime(movie_data.get("release_date"), "%Y-%m-%d")

            movie_data = {
                "id": movie_data.get("id"),
                "title": movie_data.get("title"),
                "release_date": datetime_obj.strftime("%Y %b. %d"),
                "date": datetime_obj,
                "vote_average": int(movie_data.get("vote_average") * 10),
                "poster": get_poster(movie_data.get("poster_path")),
                "genres": self._get_genres(movie_data.get("genre_ids"))
            }

            self.current_count += 1

            try:
                self.signals.movie_data_downloaded.emit(movie_data)
            except RuntimeError:
                pass
        
        self.is_working = False

        try:
            self.signals.task_finished.emit()
        except RuntimeError: 
            pass