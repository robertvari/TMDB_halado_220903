import QtQuick 2.15
import QtQuick.Layouts 1.15


CustomRectangle{
    id: root

    property string movie_title: "Prey"
    property string movie_date: "02 Aug 2022"
    property int movie_rating
    property string movie_id
    property var movie_poster

    ColumnLayout{
        anchors.fill: parent
        spacing: 0

        // poster
        Image{
            source: Resources.get("poster.jpg")
            sourceSize: Qt.size(root.width, 262)
        }

        // rating
        
        Item{
            Layout.fillWidth: true
            Layout.fillHeight: true

            ColumnLayout{
                anchors.fill: parent
                anchors.margins: 10

                // Movie title
                SubtitleText{text: movie_title}

                Item{
                    Layout.fillHeight: true
                }

                // release date
                SmallText{text: movie_date; color: "gray"}
            }
        }
    }
}