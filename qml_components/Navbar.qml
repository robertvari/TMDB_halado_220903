import QtQuick 2.15
import QtQuick.Layouts 1.15
import "custom_widgets"

Rectangle{
    id: root
    color: "#032541"

    // property int font_size: 20
    // property color text_color: "white"

    RowLayout{
        anchors.fill: parent
        spacing: 30
        anchors.leftMargin: 10
        anchors.rightMargin: 10

        Image{
            id: logo
            source: Resources.get("logo.svg")
        }

        TextButton{text: "Movies"; bold_font: true; font_size: 18; onClicked: app_layout.state="movies"; state: app_layout.state === "movies"? "active" : ""}
        TextButton{text: "TV Shows"; bold_font: true; font_size: 18; onClicked: app_layout.state="tvshows"; state: app_layout.state === "tvshows"? "active" : ""}
        TextButton{text: "People"; bold_font: true; font_size: 18; onClicked: app_layout.state="peoples"; state: app_layout.state === "peoples"? "active" : ""}
        TextButton{text: "More"; bold_font: true; font_size: 18; onClicked: app_layout.state="more"; state: app_layout.state === "more"? "active" : ""}

        // spacer item
        Item{
            Layout.fillWidth: true
        }
    }
}