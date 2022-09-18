import QtQuick 2.15
import QtQuick.Layouts 1.15


CustomRectangle{
    id: root

    property string movie_title: "Demon Slayer -Kimetsu no Yaiba- The Movie: Mugen Train"
    property string movie_date: "02 Aug 2022"
    property int movie_rating: 50
    property string movie_id
    property var movie_poster

    ColumnLayout{
        anchors.fill: parent
        spacing: 0

        // poster
        Item{
            id: poster_container
            Layout.fillWidth: true
            implicitHeight: 262

            Image{
                id: poster
                source: Resources.get("poster.jpg")
                sourceSize: Qt.size(poster_container.width, poster_container.height)
            }

            PopularityProgress{
               anchors.bottom: poster.bottom
               x: 10
               anchors.bottomMargin: -10

               percentage: 100
            }
        }


        // rating
        
        Item{
            Layout.fillWidth: true
            Layout.fillHeight: true

            ColumnLayout{
                anchors.fill: parent
                anchors.margins: 10

                // Movie title
                SubtitleText{
                    text: movie_title
                    font.pixelSize: 14
                    wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                    Layout.fillWidth: true
                }

                Item{
                    Layout.fillHeight: true
                }

                // release date
                SmallText{text: movie_date; color: "gray"}
            }
        }
    }
}