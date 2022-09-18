from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex

class MovieList(QAbstractListModel):
    DataRole = Qt.UserRole

    def __init__(self):
        super().__init__()
        
        self._movies = [
            {"title": "Fall", "release_date": "2022-08-11", "vote_average": 74},
            {"title": "Pinocchio", "release_date": "2022-09-07", "vote_average": 68},
            {"title": "Beast", "release_date": "2022-08-11", "vote_average": 71}
        ]

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