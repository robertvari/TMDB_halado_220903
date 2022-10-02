import QtQuick 2.15
import QtQuick.Layouts 1.15
import "custom_widgets"

Item{
    ColumnLayout{
        anchors.fill: parent
        anchors.margins: 20

        RowLayout{
            Image{
                source: MovieDetails.poster
            }

            ColumnLayout{
                Layout.alignment: Qt.AlignTop

                TitleText{
                    text: MovieDetails.title
                }

                RowLayout{
                    SmallText{text: MovieDetails.release_date}
                    SmallText{text: "•"}
                    SmallText{text: MovieDetails.genres}
                    SmallText{text: "•"}
                    SmallText{text: MovieDetails.runtime}
                }

                SubtitleText{text: MovieDetails.tagline}

                SmallText{
                    Layout.fillWidth: true
                    text: MovieDetails.overview
                    wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                }
            }
        }

        Item{
            Layout.fillHeight: true
        }
    }
}