import os, sys
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuickControls2 import QQuickStyle

from py_components.resources import Resources
from py_components.movie_list import MovieList, MovieListProxy


APP_ROOT = os.path.dirname(__file__)
MAIN_QML = os.path.join(APP_ROOT, "main.qml")
QQuickStyle.setStyle("Material")

class TMDB:
    def __init__(self):
        # instance of QGuiApplication
        self.app = QGuiApplication(sys.argv)

        # instance of QQmlApplicationEngine
        self.engine = QQmlApplicationEngine()

        # get rootContext
        self.context = self.engine.rootContext()

        # insert my python objects into QML context
        self.resources = Resources()
        self.context.setContextProperty("Resources", self.resources)

        self.movie_list = MovieList()
        self.context.setContextProperty("MovieList", self.movie_list)

        self.movie_list_proxy = MovieListProxy()
        self.movie_list_proxy.setSourceModel(self.movie_list)
        self.context.setContextProperty("MovieListProxy", self.movie_list_proxy)

        # load main.qml
        self.engine.load(MAIN_QML)

        if not self.engine.rootObjects:
            sys.exit(-1)
        
        self.app.lastWindowClosed.connect(self._close_app)

        # hold window open till user click close button
        sys.exit(self.app.exec_())
    
    def _close_app(self):
        print("Closing threads...")
        self.movie_list.movie_list_worker.stop()

if __name__ == "__main__":
    TMDB()