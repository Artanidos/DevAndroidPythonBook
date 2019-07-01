import QtQuick 2.0
import QtQuick.Controls 2.5

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QML Layout Demo"

    // Step 1
    /* Rectangle {
        width: 200
        height: 200
        x: 100
        y: 100
        color: "green"
        border {
            width: 2
            color: "black"
        }
        radius: 20
    } */

    // Step 2
    /* Rectangle {
        width: parent.width / 2
        height: parent.height / 2
        x: parent.width / 2
        y: parent.height / 2
        color: "green"
        border {
            width: 2
            color: "black"
        }
        radius: 20
    } */

    // Step 3
    /* Rectangle {
        width: parent.width / 2
        height: parent.height / 2
        x: (parent.width - width) / 2
        y: (parent.height - height) / 2
        color: "green"
        border {
            width: 2
            color: "black"
        }
        radius: parent.width / 20.0
    } */

    // Step 4
    /* Rectangle {
        width: parent.width / 2
        height: parent.height / 2
        anchors.centerIn: parent
        color: "green"
        border {
            width: 2
            color: "black"
        }
        radius: parent.width / 20.0
    } */

    // Step 5
    /* Rectangle {
        // width: parent.width / 2
        // height: parent.height / 2
        anchors.fill: parent
        color: "green"
        border {
            width: 2
            color: "black"
        }
        radius: parent.width / 20.0
    } */

    // Step 6
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
    }

    Rectangle {
        id: rect2
        width: parent.width / 4
        height: parent.height / 4
        anchors.left: rect1.left
        anchors.top: rect1.bottom
        anchors.topMargin: 10
        color: "blue"
        border {
            width: 2
            color: "black"
        }
        radius: parent.width / 20.0
    }
}
