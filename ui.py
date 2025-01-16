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
        MainWindow.resize(604, 330)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.interface_combo = QComboBox(self.centralwidget)
        self.interface_combo.setObjectName(u"interface_combo")
        self.interface_combo.setGeometry(QRect(270, 90, 161, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 90, 101, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 150, 101, 31))
        self.start_dump_but = QPushButton(self.centralwidget)
        self.start_dump_but.setObjectName(u"start_dump_but")
        self.start_dump_but.setGeometry(QRect(270, 150, 161, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 220, 101, 31))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(270, 220, 161, 31))
        self.jam_but = QPushButton(self.centralwidget)
        self.jam_but.setObjectName(u"jam_but")
        self.jam_but.setGeometry(QRect(450, 210, 121, 41))
        self.stop_but = QPushButton(self.centralwidget)
        self.stop_but.setObjectName(u"stop_but")
        self.stop_but.setGeometry(QRect(460, 270, 101, 41))
        self.scan_interface_but = QPushButton(self.centralwidget)
        self.scan_interface_but.setObjectName(u"scan_interface_but")
        self.scan_interface_but.setGeometry(QRect(270, 30, 161, 31))
        self.start_monitor_but = QPushButton(self.centralwidget)
        self.start_monitor_but.setObjectName(u"start_monitor_but")
        self.start_monitor_but.setGeometry(QRect(440, 90, 151, 31))
        self.stop_dump_but = QPushButton(self.centralwidget)
        self.stop_dump_but.setObjectName(u"stop_dump_but")
        self.stop_dump_but.setGeometry(QRect(440, 150, 151, 31))
        self.manage_mode_but = QPushButton(self.centralwidget)
        self.manage_mode_but.setObjectName(u"manage_mode_but")
        self.manage_mode_but.setGeometry(QRect(440, 30, 151, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select interface", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select interface", None))
        self.start_dump_but.setText(QCoreApplication.translate("MainWindow", u"start dump", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select ESSID ", None))
        self.jam_but.setText(QCoreApplication.translate("MainWindow", u"JAM !", None))
        self.stop_but.setText(QCoreApplication.translate("MainWindow", u"STOP X", None))
        self.scan_interface_but.setText(QCoreApplication.translate("MainWindow", u"Scan Interfaces", None))
        self.start_monitor_but.setText(QCoreApplication.translate("MainWindow", u"Start Monitor Mode", None))
        self.stop_dump_but.setText(QCoreApplication.translate("MainWindow", u"STOP dump", None))
        self.manage_mode_but.setText(QCoreApplication.translate("MainWindow", u"Managed mode", None))
    # retranslateUi

