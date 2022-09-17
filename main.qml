import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.15
import "qml_components"

Window{
    visible: true
    title: "The Movie Database"
    width: 1280
    height: 720

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
            
            MovieListView{
                Layout.fillWidth: true
                Layout.fillHeight: true
            }
        }
    }    
}