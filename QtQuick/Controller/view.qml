import QtQuick 2.0
import QtQuick.Controls 2.5

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QML Controller Demo"

    function myQmlFunction(msg) {
        txt.text = "Python has answered: " + msg
        return "some return value"
    }

    Button {
        id: button
        x: (parent.width - width) / 2
        y: 20
        height: 40
        text: "Click me" 
        onClicked: controller.myPythonFunction("Hello from QML")
    }

    Text {
        id: txt
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: button.bottom
        anchors.topMargin: 10
        text: "You should click the button"
        font.pixelSize: 13
    }
}
