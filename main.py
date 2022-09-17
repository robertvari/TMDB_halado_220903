import os, sys
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

APP_ROOT = os.path.dirname(__file__)
MAIN_QML = os.path.join(APP_ROOT, "main.qml")

class TMDB:
    def __init__(self):
        # instance of QGuiApplication
        self.app = QGuiApplication(sys.argv)

        # instance of QQmlApplicationEngine
        self.engine = QQmlApplicationEngine()

        # load main.qml
        self.engine.load(MAIN_QML)

        if not self.engine.rootObjects:
            sys.exit(-1)
        
        # hold window open till user click close button
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    TMDB()