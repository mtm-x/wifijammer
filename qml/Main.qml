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

    // property string pkg_clicked: ""
    property bool isProcessing: false
    property var packagesList

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
                color: customButton.down ? "#1E88E5" : (customButton.hovered ? "#42A5F5" : "#2196F3")
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
                color: customButton.down ? "#1E88E5" : (customButton.hovered ? "#42A5F5" : "#2196F3")
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
                color: customButton.down ? "#1E88E5" : (customButton.hovered ? "#42A5F5" : "#2196F3")
                border.color: "#fff"
                border.width: 2
            }
            font.pixelSize: 16

            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                onClicked: {

                    var newModel = jammer.stop_dump()
                    comboBox.model = []  // Clear first
                    comboBox.model = newModel  // Then set new model
                    isProcessing = false
                }
            }
        }
    }

    Rectangle{
        id : searchPage
        width: parent.width
        height: parent.height
        visible: false
        color: "#232323"

        Text {
            text: "Which Application you would like to uninstall"
            font.family: productsans.name
            font.pixelSize: 20
            font.bold: true
            color: "white"
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin:parent.height / 20
        }

        Label{
            id : connectedDevice
            font.family: productsans.name
            font.pixelSize: 16
            font.bold: true
            visible: true
            color: "white"
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin:parent.height / 4
        }

        TextField {
            id: appName
            placeholderText : "Search"
            placeholderTextColor: "#888"
            width: parent.width / 2
            height: 40
            font.family: productsans.name
            font.pixelSize: 16
            color: "#000"
            background: Rectangle {
                color: "#fff"
                radius: 6
                border.color: "#ccc"
                border.width: 1
            }
            onPressed: appName.placeholderText=""
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.leftMargin: parent.width / 6
            anchors.topMargin: parent.height / 6.5

        }

        Button{
            id: customButton
            text: "Search"
            width: 100
            height: 50
            font.family: productsans.name
            font.pixelSize: 16
            background: Rectangle {
                radius: 6
                color: customButton.down ? "#1E88E5" : (customButton.hovered ? "#42A5F5" : "#2196F3")
                border.color: "#fff"
                border.width: 2
            }

            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                onClicked: {
                    debloater.app_name(appName.text)
                    packageModel.clear();

                           var packages = debloater.load_pkgs("Search");
                           for (var i = 0; i < packages.length; i++) {
                               packageModel.append({ "packageName": packages[i] });
                           }


                }
            }
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.leftMargin: parent.width / 1.4
            anchors.topMargin: parent.height / 6.8
        }

        ScrollView{

            id : scroll
            width: 600
            height: 400
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
            anchors.topMargin: 210
            anchors.bottom : parent.bottom
            anchors.bottomMargin: 80

            ScrollBar.vertical: ScrollBar {
                    parent: scroll
                    x: scroll.mirrored ? 0 : scroll.width - width
                    y: scroll.topPadding
                    height: scroll.availableHeight
                    active: scroll.ScrollBar.horizontal.active
                }

            ListView {
                id: packageListView
                anchors.fill: scroll

                model: ListModel {
                    id: packageModel
                }

                delegate: Item {
                    width: scroll.width
                    height: 40

                    Rectangle {
                        width: parent.width
                        height: parent.height
                        color: "#2E2E2E"
                        border.color: "#AAAAAA"

                        Text {
                            text: model.packageName
                            font.family: productsans.name
                            color: "white"
                            anchors.centerIn: parent
                        }

                    }
                    MouseArea{
                        anchors.fill: parent
                        cursorShape: Qt.PointingHandCursor
                        onClicked: {
                            pkg_clicked = model.packageName
                            searchPage.visible = false
                            uninstallPage.visible = true
                            pkgName.text = "Selected Package: "+pkg_clicked
                        }
                    }
                }
            }
        }
    }


    Rectangle{
        id: uninstallPage
        width: parent.width
        height: parent.height
        visible: false
        color: "#232323"


        Text {
            id : pkgName
            font.family: productsans.name
            font.pixelSize: 16
            font.bold: true
            color: "white"
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: parent.height / 4
        }

        Column{
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
            anchors.topMargin: parent.height / 3
            spacing: 10
            Button {
                text: "Uninsttall"
                font.family: productsans.name
                width: 150
                height: 60

                background: Rectangle {
                    radius: 6
                    color: customButton.down ? "#1E88E5" : (customButton.hovered ? "#42A5F5" : "#2196F3")
                    border.color: "#fff"
                    border.width: 2
                }
                font.pixelSize: 16

                MouseArea {
                    anchors.fill: parent
                    cursorShape: Qt.PointingHandCursor
                    onClicked: {
                        pkgName.text = debloater.uninstall(pkg_clicked)

                    }
                }
            }

            Button {
                text: "Back"
                font.family: productsans.name
                width: 150
                height: 60

                background: Rectangle {
                    radius: 6
                    color: customButton.down ? "#1E88E5" : (customButton.hovered ? "#42A5F5" : "#2196F3")
                    border.color: "#fff"
                    border.width: 2
                }
                font.pixelSize: 16

                MouseArea {
                    anchors.fill: parent
                    cursorShape: Qt.PointingHandCursor
                    onClicked: {
                        uninstallPage.visible = false
                        searchPage.visible = true
                        appName.text = ""
                        packageModel.clear();
                        var packages = debloater.load_pkgs("");
                        for (var i = 0; i < packages.length; i++) {
                            packageModel.append({ "packageName": packages[i] });
                        }
                    }
                }
            }
        }
    }
}
