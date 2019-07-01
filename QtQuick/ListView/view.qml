import QtQuick 2.0
import QtQuick.Controls 2.5

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QML ListView Demo"

    ListView {
        width: 100 
        height: 100
        anchors.fill: parent
        model: myModel
        delegate: Rectangle {
            height: 25
            width: 200
            color: "lightgray"
            Text { 
                text: modelData
                font.pixelSize: 15
            }
        }
    }
}
