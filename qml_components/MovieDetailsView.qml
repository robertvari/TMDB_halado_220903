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

                RowLayout{
                    TitleText{
                        Layout.fillWidth: true
                        text: MovieDetails.title
                        wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                    }
                }

                RowLayout{
                    SubtitleText{
                        text: MovieDetails.release_date
                        font.bold: false
                    }

                    SubtitleText{
                        text: "⁫⁫•⁫⁫⁫⁫"
                        font.bold: false
                    }

                    SubtitleText{
                        text: MovieDetails.genres
                        font.bold: false
                    }

                    SubtitleText{
                        text: "⁫⁫•"
                        font.bold: false
                    }

                    SubtitleText{
                        text: MovieDetails.runtime
                        font.bold: false
                    }
                }

                SubtitleText{
                    text: MovieDetails.tagline
                }

                Item{
                    implicitHeight: 20
                }

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