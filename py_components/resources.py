from PySide2.QtCore import QObject, Slot, QUrl
import os

RESOURCES_PATH = os.path.dirname(__file__).replace("py_components", "resources")

class Resources(QObject):
    @Slot(str, result=QUrl)
    def get(self, resource_name):
        resource_path = os.path.join(RESOURCES_PATH, resource_name)
        assert os.path.exists(resource_path), f"Resource does not exist: {resource_path}"
        return QUrl().fromLocalFile(resource_path)