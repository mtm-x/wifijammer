import QtQuick
import QtQuick.Controls
import QtQuick.Window
import QtQuick.Controls.Material
import com.mtm.jammer 1.0

Window {
    width: 640
    height: 580
    visible: true
    title: qsTr("Jammer !!!")
    color: "#232323"

    maximumWidth: 640
    maximumHeight: 580
    minimumWidth: 640
    minimumHeight: 580

    Jammer{
        id: jammer
    }

    FontLoader {
        id: productsans
        source: "qrc:/res/fonts/ProductSansRegular.ttf"

    }

    property bool isProcessing: false

    Rectangle {
        id: mainPage
        width: parent.width
        height: parent.height
        color: "#232323"

        Text {
            id: welcome_main
            text: "© GitHub : mtm-x"
            font.family: productsans.name
            font.pixelSize: 20
            font.bold: true
            color: "white"
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottomMargin: parent.height / 5.3
        }
        Text {
            text: "Lets Jam !!"
            font.family: productsans.name
            font.pixelSize: 36
            font.bold: true
            color: "white"
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: parent.height / 3.7
        }
        Button {
            id: next_but
            text: "Start"
            font.family: productsans.name
            width: 100
            height: 60
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
            anchors.topMargin: parent.height / 2

            background: Rectangle {
                radius: 6
                color: next_but.down ? "#1E88E5" : (next_but.hovered ? "#42A5F5" : "#2196F3")
                border.color: "#fff"
                border.width: 2
            }
            font.pixelSize: 16
            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                onClicked: {
                    mainPage.visible = false
                    network.visible = true
                    var network_text = jammer.scan_interfaces()
                    networkText.text= "Network Card Name: " + network_text

                }
            }
        }
    }

    Timer {
        id: checkDeviceTimer
        interval: 10000
        running: false
        onTriggered: {

            ListModel.clear()
            var packages = jammer.stop_dump()
            for (var i = 0; i < packages.length; i++) {
                ListModel.append({ "wifiName": packages[i] });
            }
        }
    }

    Rectangle{
        id : network
        width: parent.width
        height: parent.height
        visible: false
        color: "#232323"

        BusyIndicator {
            id: busyIndicator
            anchors.top: parent.top
            running: isProcessing
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: parent.height / 3.5
        }

        Text {
            id: networkText
            font.family: productsans.name
            text: qsTr("Network Card Name: ")
            font.pixelSize: 20
            font.bold: true
            color: "white"
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin:parent.height / 5
        }

        Label{
            text: qsTr("Press Dump to show the nearby WiFi")
            font.family: productsans.name
            font.pixelSize: 16
            font.bold: true
            visible: true
            color: "white"
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin:parent.height / 2.2
        }

        Button {
            id: dumpButton
            text: "Dump"
            font.family: productsans.name
            width: 100
            height: 60
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
            anchors.topMargin: parent.height / 2

            background: Rectangle {
                radius: 6
                color: dumpButton.down ? "#1E88E5" : (dumpButton.hovered ? "#42A5F5" : "#2196F3")
                border.color: "#fff"
                border.width: 2
            }
            font.pixelSize: 16

            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                onClicked: {

                    network.visible = false
                    dumpPage.visible = true
                    isProcessing = true
                    jammer.start_dump()


                }
            }
        }
    }

    Rectangle{
        id : dumpPage
        width: parent.width
        height: parent.height
        visible: false
        color: "#232323"

        ComboBox{
            id: comboBox
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
            anchors.topMargin: parent.height / 3
            font.family: productsans.name
            width: 300
            model: ['select']
        }

        Button {
            id: dumpstopbut
            text: "Stop"
            font.family: productsans.name
            width: 100
            height: 60
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
            anchors.topMargin: parent.height / 2

            background: Rectangle {
                radius: 6
                color: dumpstopbut.down ? "#1E88E5" : (dumpstopbut.hovered ? "#42A5F5" : "#2196F3")
                border.color: "#fff"
                border.width: 2
            }
            font.pixelSize: 16

            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                onClicked: {

                    var newModel = jammer.stop_dump()
                    comboBox.model = []
                    comboBox.model = newModel
                    isProcessing = false
                    jamit.visible = true
                }
            }
        }

        Button {
            id: jamit
            text: "Jam itt"
            font.family: productsans.name
            width: 100
            height: 60
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
            anchors.topMargin: parent.height / 1.5
            visible: false

            background: Rectangle {
                radius: 6
                color: jamit.down ? "#D32F2F" : (jamit.hovered ? "#EF5350" : "#F44336")
                border.color: "#fff"
                border.width: 2
            }
            font.pixelSize: 16

            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                onClicked: {

                    jammer.jam(comboBox.currentIndex)
                    stopjam.visible = true

                }
            }
        }

        Button {
            id: stopjam
            text: "Stop jam"
            font.family: productsans.name
            width: 130
            height: 60
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
            anchors.topMargin: parent.height / 1.2
            visible: false

            background: Rectangle {
                radius: 6
                color: stopjam.down ? "#1E88E5" : (stopjam.hovered ? "#42A5F5" : "#2196F3")
                border.color: "#fff"
                border.width: 2
            }
            font.pixelSize: 16

            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                onClicked: {
                    jammer.stop()
                }
            }
        }
    }
}
