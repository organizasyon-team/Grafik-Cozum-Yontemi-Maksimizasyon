# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 261)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnHesapla = QtWidgets.QPushButton(self.centralwidget)
        self.btnHesapla.setGeometry(QtCore.QRect(40, 190, 271, 40))
        self.btnHesapla.setObjectName("btnHesapla")
        self.sbAdet = QtWidgets.QSpinBox(self.centralwidget)
        self.sbAdet.setGeometry(QtCore.QRect(40, 80, 61, 26))
        self.sbAdet.setObjectName("sbAdet")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 80, 98, 29))
        self.label_8.setObjectName("label_8")

        self.btnKisitEkle = QtWidgets.QPushButton(self.centralwidget)
        self.btnKisitEkle.setGeometry(QtCore.QRect(220, 80, 90, 30))
        self.btnKisitEkle.setObjectName("btnAdet")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 10, 271, 61))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 28, 271, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.zmaksX1 = QtWidgets.QSpinBox(self.layoutWidget)
        self.zmaksX1.setObjectName("zmaksX1")
        self.horizontalLayout_3.addWidget(self.zmaksX1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.zmaksX2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.zmaksX2.setObjectName("zmaksX2")
        self.horizontalLayout_3.addWidget(self.zmaksX2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 150, 271, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 271, 28))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sbx11 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.sbx11.setMinimum(-999)
        self.sbx11.setMaximum(999)
        self.sbx11.setObjectName("sbx11")
        self.horizontalLayout.addWidget(self.sbx11)
        self.lblx1 = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblx1.setObjectName("lblx1")
        self.horizontalLayout.addWidget(self.lblx1)
        self.sbx21 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.sbx21.setMinimum(-999)
        self.sbx21.setMaximum(999)
        self.sbx21.setObjectName("sbx21")
        self.horizontalLayout.addWidget(self.sbx21)
        self.lblx2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblx2.setObjectName("lblx2")
        self.horizontalLayout.addWidget(self.lblx2)
        self.sbz1 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.sbz1.setObjectName("sbz1")
        self.horizontalLayout.addWidget(self.sbz1)
        self.lblFonksiyon = QtWidgets.QLabel(self.centralwidget)
        self.lblFonksiyon.setGeometry(QtCore.QRect(40, 110, 131, 16))
        self.lblFonksiyon.setObjectName("lblFonksiyon")
        self.lblX1X2 = QtWidgets.QLabel(self.centralwidget)
        self.lblX1X2.setGeometry(QtCore.QRect(40, 130, 121, 17))
        self.lblX1X2.setObjectName("lblX1X2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Kisit Objects
        self.kisitlarObjects = [QtWidgets.QSpinBox, QtWidgets.QLabel,QtWidgets.QSpinBox, QtWidgets.QLabel,QtWidgets.QSpinBox]

        #Events
        self.btnKisitEkle.clicked.connect(self.kisitEkle)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grafik Çözüm Programı (Maksimizasyon)"))
        self.btnHesapla.setText(_translate("MainWindow", "Hesapla"))
        self.btnKisitEkle.setText(_translate("MainWindow", "Ekle"))
        self.label_8.setText(_translate("MainWindow", "Adet Denklem"))
        self.groupBox.setTitle(_translate("MainWindow", "Amaç Fonksiyonu"))
        self.label.setText(_translate("MainWindow", "Zmax="))
        self.label_2.setText(_translate("MainWindow", "X1 +"))
        self.label_3.setText(_translate("MainWindow", "X2"))
        self.lblx1.setText(_translate("MainWindow", "X1 +"))
        self.lblx2.setText(_translate("MainWindow", "X2 <="))
        self.lblFonksiyon.setText(_translate("MainWindow", "Fonksiyon Kısıtları"))
        self.lblX1X2.setText(_translate("MainWindow", "X1 >= 0,  X2 >= 0"))

    def kisitEkle(self):
        kisit_sayi = self.sbAdet.value()
        print(kisit_sayi)

