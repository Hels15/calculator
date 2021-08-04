import QtQuick
import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls
Window {
    width: 400
    height: 400
    visible: true
    title: qsTr("Calculator")

    ColumnLayout{
        anchors.fill: parent  //Egész ablakot kitölti
        anchors.margins: 10


        TextField{
            Layout.fillWidth: true
            font.pixelSize: 30
            horizontalAlignment: TextInput.AlignRight

            background: Rectangle{
                color: "lightgrey"
                radius: 5
            }
            readOnly: true
            text: Calculator.display


        }


        GridLayout{
            Layout.fillHeight: true
            Layout.fillWidth: true
            columns: 4

            Repeater{
                model: ["C", "+/-", "%", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "="]

                Button{
                    id: button
                    implicitWidth:  50
                    implicitHeight: 100
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    contentItem: Text{
                        text: modelData
                        font.pixelSize: 25
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter



                    }


                    onClicked: Calculator.set_display(modelData)
                }

                }


        }

    }

}
