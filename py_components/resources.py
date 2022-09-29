from PySide2.QtCore import QObject, Slot, QUrl
import os, requests
from os.path import expanduser

RESOURCES_PATH = os.path.dirname(__file__).replace("py_components", "resources")
CACHE_FOLDER = os.path.join(expanduser("~"), "TMDB_CACHE")

class Resources(QObject):
    @Slot(str, result=QUrl)
    def get(self, resource_name):
        resource_path = os.path.join(RESOURCES_PATH, resource_name)
        assert os.path.exists(resource_path), f"Resource does not exist: {resource_path}"
        return QUrl().fromLocalFile(resource_path)


def get_poster(url):
    if not os.path.exists(CACHE_FOLDER):
        os.makedirs(CACHE_FOLDER)
        
    poster_file_name = url[1:]
    poster_path = os.path.join(CACHE_FOLDER, poster_file_name)

    if os.path.exists(poster_path):
        return QUrl().fromLocalFile(poster_path)

    server_url = f"https://image.tmdb.org/t/p/w300{url}"

    assert requests.get(server_url).status_code == 200, f"Bad URL {server_url}"

    img_data = requests.get(server_url).content
    with open(poster_path, 'wb') as f:
        f.write(img_data)

        return QUrl().fromLocalFile(poster_path)


if __name__ == '__main__':
    download_poster("/uHA5COgDzcxjpYSHHulrKVl6ByL.jpg")