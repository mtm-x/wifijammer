#!/usr/bin/env python3
import subprocess
import os
import sys  
from time import sleep
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class Jammer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("WIFI Jammer")

        #chek if the user is root
        if not os.geteuid() == 0 :
            print  ("Run it as root")
            sys.exit(1)

        # Connect the buttons to the functions
        self.ui.start_dump_but.clicked.connect(self.start_dump)
        self.ui.jam_but.clicked.connect(self.jam)
        self.ui.stop_but.clicked.connect(self.stop)
        self.ui.scan_interface_but.clicked.connect(self.scan_interfaces)
        self.ui.start_monitor_but.clicked.connect(self.start_monitor)
        self.ui.jam_but.setEnabled(False)
        self.ui.stop_but.setEnabled(False)

    def scan_interfaces(self):
        result = subprocess.run(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Process the output to get the interface names
        self.interface_names = []
        for line in result.stdout.splitlines():
    
            if 'IEEE 802.11' in line:
                self.interface_names.append(line.split()[0])     

        # Print the interface names
        for name in self.interface_names:
            print(name)
            self.ui.interface_combo.addItem(name)
    def start_monitor(self):
        self.current_interface = self.ui.interface_combo.currentText()
        subprocess.run(['airmon-ng','start',self.current_interface],stdout=subprocess.PIPE,text=True)
        sleep(0.5)
        print(self.current_interface)
        
    def start_dump(self):
        self.wireless_interface_mon = self.current_interface + "mon"
        #process = subprocess.Popen(['airodump-ng','-w','dump','--output-format','csv', self.wireless_interface_mon])
        process = subprocess.Popen(
        ['airodump-ng', '--output-format', 'csv', '--write', 'dump-04.csv', self.wireless_interface_mon],
        stderr=subprocess.PIPE
    )
        self.ui.jam_but.setEnabled(True)
        self.ui.stop_but.setEnabled(True)   
        

    def jam(self):
        pass
    def stop(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    window = Jammer()
    window.show()
    app.exec()
        
