from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex, QObject, Signal, QRunnable, QThreadPool
import tmdbsimple as tmdb
from py_components.resources import get_poster

tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5


class MovieList(QAbstractListModel):
    DataRole = Qt.UserRole

    def __init__(self):
        super().__init__()

        self.job_pool = QThreadPool()
        self.job_pool.setMaxThreadCount(1)
        self.movie_list_worker = MovieListWorker()

        self._movies = []
        self._fetch_movies()

    def _fetch_movies(self):
        self._reset()
        self.movie_list_worker.signals.movie_data_downloaded.connect(self._inser_movie)
        self.job_pool.start(self.movie_list_worker)

    def _reset(self):
        self.beginResetModel()
        self._movies.clear()
        self.endResetModel()

    def _inser_movie(self, movie_data):
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


class WorkerSignals(QObject):
    movie_data_downloaded = Signal(dict)

    def __init__(self):
        super().__init__()


class MovieListWorker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()
        self.tmdb_movies = tmdb.Movies()

    def run(self):
        popular_movies = self.tmdb_movies.popular(page=1)["results"]
        
        for movie_data in popular_movies:
            movie_data = {
                "title": movie_data.get("title"),
                "release_date": movie_data.get("release_date"),
                "vote_average": int(movie_data.get("vote_average") * 10),
                "poster": get_poster(movie_data.get("poster_path"))
            }

            self.signals.movie_data_downloaded.emit(movie_data)