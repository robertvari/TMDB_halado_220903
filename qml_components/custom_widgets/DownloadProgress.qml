import QtQuick 2.15

Item{
    id: root
    implicitHeight: 10
    visible: MovieList.is_downloading

    property int max_value: 20
    property int current_value: 5

    Rectangle{
        height: root.height
        width: (root.width / root.max_value) * root.current_value
        color: "#05B4E3"
        radius: root.height / 2
    }
}