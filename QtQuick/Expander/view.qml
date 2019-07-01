import QtQuick 2.12
import QtQuick.Controls 2.5

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QML Demo"

    Expander {
        text: "Dashboard"
        Column {
            padding: 5
            width: parent.width
            Text {
                height: 25
                width: parent.width
                text: "Item 1"
            }
            Text {
                height: 25
                width: parent.width
                text: "Item 2"
            }
            Text {
                height: 25
                width: parent.width
                text: "Item 3"
            }
            Text {
                height: 25
                width: parent.width
                text: "Item 4"
            }
        }
    }
}
