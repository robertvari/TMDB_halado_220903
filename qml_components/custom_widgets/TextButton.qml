import QtQuick 2.15

Text{
    id: root
    property color default_color: Qt.rgba(1, 1, 1, 0.7)
    property color highlight_color: Qt.rgba(1, 1, 1, 1)
    property int font_size: 16
    property bool bold_font: false

    font.bold: root.bold_font
    font.pixelSize: root.font_size
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