from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex
import tmdbsimple as tmdb
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5


class MovieList(QAbstractListModel):
    DataRole = Qt.UserRole

    def __init__(self):
        super().__init__()

        self._movies = []
        self.tmdb_movies = tmdb.Movies()
        self._fetch_movies()

    def _fetch_movies(self):
        self._reset()
        
        popular_movies = self.tmdb_movies.popular(page=1)["results"]
        for movie_data in popular_movies:
            self._inser_movie({
                "title": movie_data.get("title"),
                "release_date": movie_data.get("release_date"),
                "vote_average": int(movie_data.get("vote_average") * 10),
            })

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