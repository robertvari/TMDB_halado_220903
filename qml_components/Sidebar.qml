import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "custom_widgets"

Item{
    ColumnLayout{
        anchors.fill: parent
        anchors.leftMargin: 5

        // Search by title
        IconTextField{id: search_by_title; placeholder_text: "Search by title"; icon: Resources.get("search.svg")}

        // Sorting
        CustomRectangle{
            Layout.fillWidth: true
            implicitHeight: 100
        }

        // spacer
        Item{
            Layout.fillHeight: true
        }
    }
}