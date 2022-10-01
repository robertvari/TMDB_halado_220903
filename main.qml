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
        anchors.fill: parent

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

                MovieListView{
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }
            }
        }
    }    
}