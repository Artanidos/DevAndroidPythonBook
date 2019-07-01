import QtQuick 2.0

Item {
    id: root
    property alias text: link.text
    default property alias _contentChildren: content.data
    width: 200
    height: 30

    Rectangle {
        id: button
        anchors.fill: parent
        color: "gray"

        Text {
            id: link
            anchors.centerIn: parent
            text: "Click"
        }

        MouseArea {
            id: trigger
            anchors.fill: parent
            onClicked: root.state = root.state == "expanded" ? "collapsed" : "expanded"
        }
    }

    Rectangle  {
        property int contentHeight: childrenRect.height
        id: content
        width: parent.width
        anchors.top: button.bottom
        color: "gray"
        clip: true
    }

    states: [
        State {
            name: "collapsed"
            PropertyChanges {
                target: content
                height: 0
            }
            PropertyChanges {
                target: button
                color: "gray"
            }
        },
        State {
            name: "expanded"
            PropertyChanges {
                target: content
                height: content.contentHeight
            }
            PropertyChanges {
                target: button
                color: "lightblue"
            }
        }
    ]

    transitions: Transition {
        ParallelAnimation {
            NumberAnimation {
                target: content
                property: "height"
                duration: 200
                easing.type: Easing.InOutQuad
            }
            ColorAnimation {
                target: button
                property: "color"
                duration: 200
            }
        }
    }
}
