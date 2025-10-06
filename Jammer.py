import sys
from pathlib import Path
import res
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtCore import Slot, QObject

import subprocess
import os
import csv
import time

QML_IMPORT_NAME = "com.mtm.jammer"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement # Python class can be imported into qml file and code
class Jammer(QObject):

    @Slot(result=str) # retrun type is str
    def scan_interfaces(self):
        result = subprocess.run(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Process the output to get the interface names
        self.wireless_interface_mon = None

        for line in result.stdout.splitlines():
            if 'IEEE 802.11' in line:
                self.interface_names = line.split()[0]
                if 'Mode:Monitor' in line:
                    self.wireless_interface_mon = self.interface_names
        
        if not self.wireless_interface_mon:
            self.wireless_interface_mon = self.interface_names + "mon"

        subprocess.run(['airmon-ng', 'start', self.interface_names], stdout=subprocess.PIPE,text=True)

        return self.interface_names

    @Slot()
    def start_dump(self):
        print("start_dump working")
        os.system('clear')
        if os.path.exists('dump-01.csv'):
            os.remove('dump-01.csv')

        time.sleep(0.5)
        self.process = subprocess.Popen(
        ['airodump-ng', '--output-format', 'csv', '--write', 'dump', self.wireless_interface_mon]) 

    @Slot(result=list)
    def stop_dump(self):
        print("stop_dump working")

        subprocess.run(['pkill', 'airodump-ng'])
        self.process.terminate()
        self.process.kill()
        time.sleep(1)
        self.retrive_info(13)
        print(self.essid[1:])
        return [item.strip() for item in self.essid[1:]]

    def retrive_info(self, index):

        self.essid = []
        self.bssid = []
        self.channel = []

        with open("dump-01.csv", mode='r') as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) > 13:
                    var = row[index]  

                    if index == 0:   #index 0 is bssid
                        if var.strip():
                            self.bssid.append(var)
                    elif index == 3:  #insex 3 is channel
                        if var.strip():
                            self.channel.append(var)
                    elif index == 13:  #index 13 is essid
                        if var.strip():
                            self.essid.append(var)


if __name__ == "__main__":

    if not os.geteuid() == 0 :
            print  ("Run it as root")
            sys.exit(1)
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "qml/Main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
