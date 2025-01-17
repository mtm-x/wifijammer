# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(622, 330)
        MainWindow.setMinimumSize(QSize(622, 330))
        MainWindow.setMaximumSize(QSize(622, 330))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.interface_combo = QComboBox(self.centralwidget)
        self.interface_combo.setObjectName(u"interface_combo")
        self.interface_combo.setGeometry(QRect(250, 90, 161, 31))
        self.interface_combo.setStyleSheet(u"QComboBox {\n"
"	\n"
"	font: 500 9pt \"Product Sans Medium\";\n"
"    background-color: #EAEAEA; /* Light gray background */\n"
"    color: #333333;           /* Dark gray text */\n"
"    border: 1px solid #D3D3D3; /* Subtle border */\n"
"    border-radius: 6px;        /* Rounded corners */\n"
"\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #C8C8C8; /* Even darker gray when clicked */\n"
"}\n"
"\n"
"\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 90, 101, 31))
        self.label.setStyleSheet(u"font: 9pt \"Product Sans\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 150, 101, 31))
        self.label_2.setStyleSheet(u"font: 9pt \"Product Sans\";")
        self.start_dump_but = QPushButton(self.centralwidget)
        self.start_dump_but.setObjectName(u"start_dump_but")
        self.start_dump_but.setGeometry(QRect(250, 150, 161, 31))
        self.start_dump_but.setStyleSheet(u"QPushButton {\n"
"	\n"
"	font: 500 9pt \"Product Sans Medium\";\n"
"    background-color: #EAEAEA; /* Light gray background */\n"
"    color: #333333;           /* Dark gray text */\n"
"    border: 1px solid #D3D3D3; /* Subtle border */\n"
"    border-radius: 6px;        /* Rounded corners */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6D6D6; /* Slightly darker gray on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C8C8C8; /* Even darker gray when clicked */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #F2F2F2; /* Pale gray background for disabled */\n"
"    color: #A9A9A9;            /* Gray text for disabled state */\n"
"}\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 210, 101, 31))
        self.label_3.setStyleSheet(u"font: 9pt \"Product Sans\";")
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(250, 210, 161, 31))
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"	\n"
"	font: 500 9pt \"Product Sans Medium\";\n"
"    background-color: #EAEAEA; /* Light gray background */\n"
"    color: #333333;           /* Dark gray text */\n"
"    border: 1px solid #D3D3D3; /* Subtle border */\n"
"    border-radius: 6px;        /* Rounded corners */\n"
"\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #C8C8C8; /* Even darker gray when clicked */\n"
"}\n"
"\n"
"\n"
"")
        self.jam_but = QPushButton(self.centralwidget)
        self.jam_but.setObjectName(u"jam_but")
        self.jam_but.setGeometry(QRect(450, 210, 121, 31))
        self.jam_but.setStyleSheet(u"QPushButton {\n"
"    background-color: #28A745; /* Green background */\n"
"    color: white;             /* White text */\n"
"    border: none;             /* No border */\n"
"    border-radius: 6px;       \n"
"    font: 500 9pt \"Product Sans Medium\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #218838; /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E7E34; /* Even darker green when clicked */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A9A9A9; /* Gray background for disabled state */\n"
"    color: white;              /* Keep white text for disabled state */\n"
"}\n"
"")
        self.stop_but = QPushButton(self.centralwidget)
        self.stop_but.setObjectName(u"stop_but")
        self.stop_but.setGeometry(QRect(450, 250, 121, 31))
        self.stop_but.setStyleSheet(u"QPushButton {\n"
"	\n"
"	font: 500 9pt \"Product Sans Medium\";\n"
"    background-color: #EAEAEA; /* Light gray background */\n"
"    color: #333333;           /* Dark gray text */\n"
"    border: 1px solid #D3D3D3; /* Subtle border */\n"
"    border-radius: 6px;        /* Rounded corners */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6D6D6; /* Slightly darker gray on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C8C8C8; /* Even darker gray when clicked */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #F2F2F2; /* Pale gray background for disabled */\n"
"    color: #A9A9A9;            /* Gray text for disabled state */\n"
"}\n"
"")
        self.scan_interface_but = QPushButton(self.centralwidget)
        self.scan_interface_but.setObjectName(u"scan_interface_but")
        self.scan_interface_but.setGeometry(QRect(250, 30, 161, 31))
        self.scan_interface_but.setStyleSheet(u"QPushButton {\n"
"    background-color: #28A745; /* Green background */\n"
"    color: white;             /* White text */\n"
"    border: none;             /* No border */\n"
"    border-radius: 6px;       \n"
"    font: 500 9pt \"Product Sans Medium\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #218838; /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E7E34; /* Even darker green when clicked */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A9A9A9; /* Gray background for disabled state */\n"
"    color: white;              /* Keep white text for disabled state */\n"
"}\n"
"")
        self.start_monitor_but = QPushButton(self.centralwidget)
        self.start_monitor_but.setObjectName(u"start_monitor_but")
        self.start_monitor_but.setGeometry(QRect(420, 90, 151, 31))
        self.start_monitor_but.setStyleSheet(u"QPushButton {\n"
"	\n"
"	font: 500 9pt \"Product Sans Medium\";\n"
"    background-color: #EAEAEA; /* Light gray background */\n"
"    color: #333333;           /* Dark gray text */\n"
"    border: 1px solid #D3D3D3; /* Subtle border */\n"
"    border-radius: 6px;        /* Rounded corners */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6D6D6; /* Slightly darker gray on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C8C8C8; /* Even darker gray when clicked */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #F2F2F2; /* Pale gray background for disabled */\n"
"    color: #A9A9A9;            /* Gray text for disabled state */\n"
"}\n"
"\n"
"")
        self.stop_dump_but = QPushButton(self.centralwidget)
        self.stop_dump_but.setObjectName(u"stop_dump_but")
        self.stop_dump_but.setGeometry(QRect(420, 150, 151, 31))
        self.stop_dump_but.setStyleSheet(u"QPushButton {\n"
"	\n"
"	font: 500 9pt \"Product Sans Medium\";\n"
"    background-color: #EAEAEA; /* Light gray background */\n"
"    color: #333333;           /* Dark gray text */\n"
"    border: 1px solid #D3D3D3; /* Subtle border */\n"
"    border-radius: 6px;        /* Rounded corners */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6D6D6; /* Slightly darker gray on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C8C8C8; /* Even darker gray when clicked */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #F2F2F2; /* Pale gray background for disabled */\n"
"    color: #A9A9A9;            /* Gray text for disabled state */\n"
"}\n"
"")
        self.manage_mode_but = QPushButton(self.centralwidget)
        self.manage_mode_but.setObjectName(u"manage_mode_but")
        self.manage_mode_but.setGeometry(QRect(420, 30, 151, 31))
        self.manage_mode_but.setStyleSheet(u"QPushButton {\n"
"	\n"
"	font: 500 9pt \"Product Sans Medium\";\n"
"    background-color: #EAEAEA; /* Light gray background */\n"
"    color: #333333;           /* Dark gray text */\n"
"    border: 1px solid #D3D3D3; /* Subtle border */\n"
"    border-radius: 6px;        /* Rounded corners */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6D6D6; /* Slightly darker gray on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C8C8C8; /* Even darker gray when clicked */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #F2F2F2; /* Pale gray background for disabled */\n"
"    color: #A9A9A9;            /* Gray text for disabled state */\n"
"}\n"
"")
        self.bssid_label = QLabel(self.centralwidget)
        self.bssid_label.setObjectName(u"bssid_label")
        self.bssid_label.setGeometry(QRect(250, 260, 181, 31))
        self.bssid_label.setStyleSheet(u"QLabel {\n"
"    color: #28A745; /* Text color */\n"
"    font: 500 9pt \"Product Sans Medium\";\n"
"}\n"
"\n"
"")
        self.channel_label = QLabel(self.centralwidget)
        self.channel_label.setObjectName(u"channel_label")
        self.channel_label.setGeometry(QRect(250, 290, 101, 31))
        self.channel_label.setStyleSheet(u"QLabel {\n"
"    color: #28A745; /* Text color */\n"
"    font: 500 9pt \"Product Sans Medium\";\n"
"}\n"
"\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 20, 51, 31))
        self.label_4.setStyleSheet(u"font: 20pt \"Product Sans\";")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 40, 131, 31))
        self.label_5.setStyleSheet(u"font: 12pt \"Product Sans\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select interface", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select interface", None))
        self.start_dump_but.setText(QCoreApplication.translate("MainWindow", u"Start dump", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select ESSID ", None))
        self.jam_but.setText(QCoreApplication.translate("MainWindow", u"JAM !", None))
        self.stop_but.setText(QCoreApplication.translate("MainWindow", u"STOP X", None))
        self.scan_interface_but.setText(QCoreApplication.translate("MainWindow", u"Scan Interfaces", None))
        self.start_monitor_but.setText(QCoreApplication.translate("MainWindow", u"Start Monitor Mode", None))
        self.stop_dump_but.setText(QCoreApplication.translate("MainWindow", u"Stop Dump", None))
        self.manage_mode_but.setText(QCoreApplication.translate("MainWindow", u"Managed mode", None))
        self.bssid_label.setText(QCoreApplication.translate("MainWindow", u"BSSID", None))
        self.channel_label.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"WiFi", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Jammer By mtm-x", None))
    # retranslateUi

