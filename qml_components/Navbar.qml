import QtQuick 2.15
import QtQuick.Layouts 1.15

Rectangle{
    id: root
    color: "#032541"

    property int font_size: 20
    property color text_color: "white"

    RowLayout{
        anchors.fill: parent
        spacing: 30
        anchors.leftMargin: 10
        anchors.rightMargin: 10

        Image{
            id: logo
            source: Resources.get("logo.svg")
        }

        Text{
            text: "Movies"
            font.bold: true
            font.pixelSize: root.font_size
            color: root.text_color
        }

        Text{
            text: "TV Shows"
            font.bold: true
            font.pixelSize: root.font_size
            color: root.text_color
        }

        Text{
            text: "People"
            font.bold: true
            font.pixelSize: root.font_size
            color: root.text_color
        }

        Text{
            text: "More"
            font.bold: true
            font.pixelSize: root.font_size
            color: root.text_color
        }

        // spacer item
        Item{
            Layout.fillWidth: true
        }
    }
}