import QtQuick 2.15
import QtQuick.Window 2.15
import "qml_components"

Window{
    visible: true
    title: "The Movie Database"
    width: 1280
    height: 720

    Navbar{}
    Sidebar{x: 600}
    MovieListView{y: 600}
}