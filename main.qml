import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls.Material 2.12
import QtQuick.Controls 2.15
import "qml_components"
import "qml_components/custom_widgets"


ApplicationWindow{
    visible: true
    title: "The Movie Database"
    width: 1280
    height: 720

    Material.theme: Material.Light
    Material.accent: Material.LightBlue

    ColumnLayout{
        id: app_layout
        anchors.fill: parent
        state: "movies"

        states: [
            State {
                name: "movies"
                PropertyChanges{
                    target: movies_view
                    visible: true
                }
            },
            State {
                name: "tvshows"
                PropertyChanges{
                    target: tvshows_view
                    visible: true
                }
            },
            State {
                name: "peoples"
                PropertyChanges{
                    target: peoples_view
                    visible: true
                }
            },
            State {
                name: "more"
                PropertyChanges{
                    target: more_view
                    visible: true
                }
            }
        ]

        Navbar{
            Layout.fillWidth: true
            implicitHeight: 64
        }

        RowLayout{
            Sidebar{
                Layout.fillHeight: true
                implicitWidth: 260
            }

            ColumnLayout{
                Layout.fillWidth: true
                Layout.fillHeight: true

                DownloadProgress{
                    Layout.fillWidth: true
                }
                
                MovieListView{id: movies_view; Layout.fillWidth: true; Layout.fillHeight: true; visible: false}
                TvShowsView{id: tvshows_view; Layout.fillWidth: true; Layout.fillHeight: true; visible: false}
                PeoplesView{id: peoples_view; Layout.fillWidth: true; Layout.fillHeight: true; visible: false}
                MoreView{id: more_view; Layout.fillWidth: true; Layout.fillHeight: true; visible: false}
            }
        }
    }    
}