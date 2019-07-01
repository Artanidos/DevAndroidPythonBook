import QtQuick 2.5

Rectangle {
    id: root
    width: 240
    height: 240
    color: "#4A4A4A"

    Rectangle {
        id: rect
        x: (parent.width - width) / 2
        y: 40
        width: 40
        height: 40
        color: "green"
    }

    Text {
        y: rect.y + rect.height + 20
        width: root.width
        color: "white"
        horizontalAlignment: Text.AlignHCenter
        text: "Triangle"
    }
}