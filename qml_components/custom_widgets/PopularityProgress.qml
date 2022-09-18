import QtQuick 2.15

Rectangle{
    id: root
    implicitHeight: 50
    implicitWidth: implicitHeight
    color: "#141414"
    radius: width

    property int percentage: 50


    // pie chart
    Canvas{
        id: mycanvas
        width: parent.width
        height: parent.height

        onPaint: {
            var ctx = getContext("2d");
            ctx.reset()

            var radiant = root.percentage * 0.062831853071796
        }
    }

    // popularity text
    Rectangle{
        color: "gray"
        width: root.width -10
        height: width
        radius: width
        anchors.centerIn: parent

        Item{
            width: childrenRect.width
            height: childrenRect.height
            anchors.centerIn: parent

            Text{
                id: rating_text
                text: root.percentage
                color: "white"
                font.bold: true
                font.pixelSize: 16
            }

            Text{
                text: "%"
                color: "white"
                font.bold: true
                font.pixelSize: 8
                anchors.left: rating_text.right
                anchors.top: rating_text.top
            }

        }
    }
}