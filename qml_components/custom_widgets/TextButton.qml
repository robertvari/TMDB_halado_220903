import QtQuick 2.15

Text{
    property color default_color: Qt.rgba(1, 1, 1, 0.7)
    property color highlight_color: Qt.rgba(1, 1, 1, 1)

    font.bold: true
    font.pixelSize: 26
    color: default_color

    MouseArea{
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor

        hoverEnabled: true
        onEntered: parent.color = parent.highlight_color
        onExited: parent.color = parent.default_color

        onClicked: print("clicked:", parent.text)
        
    }
}