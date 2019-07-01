import QtQuick 2.0
import QtQuick.Controls 2.5

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QML Mouse Demo"

    Image {
        anchors.fill: parent
        source: "./images/QtForPython.png"
        onProgressChanged: console.log(progress)
    }
}
