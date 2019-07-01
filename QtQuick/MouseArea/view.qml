import QtQuick 2.0
import QtQuick.Controls 2.5

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QML Mouse Demo"

    Rectangle {
        id: rect1
        width: parent.width / 4
        height: parent.height / 4
        x: (parent.width - width) / 2
        y: parent.height / 10
        color: "green"
        border {
            width: 2
            color: "black"
        }
        radius: parent.width / 20.0

        MouseArea {
            anchors.fill: parent
            onClicked: {
                rect1.color = "red"
                console.log("mouse has been clicked")
            }

            onDoubleClicked: rect1.color = "green"
        }
    }
}
