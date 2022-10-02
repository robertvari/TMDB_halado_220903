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
    visibility: "Maximized"

    Material.theme: Material.Light
    Material.accent: Material.LightBlue

    ColumnLayout{
        id: app_layout
        anchors.fill: parent

        state: "movies"
        states: [
            State{
                name: "movies"
                PropertyChanges{
                    target: movies_list
                    visible: true
                }
            },
            State{
                name: "tvshows"
                PropertyChanges{
                    target: tvshows_list
                    visible: true
                }
            },
            State{
                name: "peoples"
                PropertyChanges{
                    target: peoples_list
                    visible: true
                }
            },
            State{
                name: "more"
                PropertyChanges{
                    target: more_list
                    visible: true
                }
            },
            State{
                name: "movie_details"
                PropertyChanges{
                    target: list_view_layout
                    visible: false
                }
                PropertyChanges{
                    target: movie_details_view
                    visible: true
                }
            }
        ]


        Navbar{
            Layout.fillWidth: true
            implicitHeight: 64
        }

        MovieDetailsView{id: movie_details_view; Layout.fillWidth: true; Layout.fillHeight: true; visible: false}

        RowLayout{
            id: list_view_layout

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

                MovieListView{id: movies_list; Layout.fillWidth: true; Layout.fillHeight: true; visible:false}
                TVShowsView{id: tvshows_list; Layout.fillWidth: true; Layout.fillHeight: true; visible:false}
                PeoplesView{id: peoples_list; Layout.fillWidth: true; Layout.fillHeight: true; visible:false}
                MoreView{id: more_list; Layout.fillWidth: true; Layout.fillHeight: true; visible:false}
            }
        }
    }
}