import QtQuick 2.0
import QtQuick.Controls 2.5
import Shapes 1.0

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QML Circle Demo"

    Circle {
        id: circle
        radius: 50
        color: "green"
        x: (parent.width - width) / 2
        y: 30
    }

    Text {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: circle.bottom
        anchors.topMargin: 10
        font.pixelSize: 20
        text: "Circle"
    }
}
