import QtQuick 2.15

Text{
    id: root
    property color default_color: Qt.rgba(1, 1, 1, 0.7)
    property color highlight_color: Qt.rgba(1, 1, 1, 1)
    property color active_color: Qt.rgba(1, 1, 1, 1)
    property int font_size: 16
    property bool bold_font: false

    font.bold: root.bold_font
    font.pixelSize: root.font_size
    color: default_color

    // custom signal
    signal clicked

    states: [
        State{
            name: "active"
            PropertyChanges{
                target: root
                color: root.active_color
            }
        },
        State{
            name: ""
            PropertyChanges{
                target: root
                color: root.default_color
            }
        }
    ]

    MouseArea{
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor

        hoverEnabled: true
        onEntered: if(root.state !== "active") parent.color = parent.highlight_color
        onExited: if(root.state !== "active") parent.color = parent.default_color

        // call root.clicked
        onClicked: root.clicked()
    }
}