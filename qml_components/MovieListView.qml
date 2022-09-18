import QtQuick 2.15
import "custom_widgets"

Item{
    GridView{
        anchors.fill: parent
        id: movie_list_view
        clip: true

        model: MovieList
        cellWidth: 184
        cellHeight: 386

        delegate: MovieCard{
            width: movie_list_view.cellWidth - 10
            height: movie_list_view.cellHeight -10
            title: movie_data.title
        }
    }
}