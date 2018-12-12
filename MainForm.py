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
        MainWindow.resize(316, 131)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kisitAdet = QtWidgets.QSpinBox(self.centralwidget)
        self.kisitAdet.setGeometry(QtCore.QRect(30, 80, 61, 26))
        self.kisitAdet.setObjectName("kisitAdet")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 80, 98, 29))
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 271, 61))
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
        self.btnKisitEkle = QtWidgets.QPushButton(self.centralwidget)
        self.btnKisitEkle.setGeometry(QtCore.QRect(200, 80, 89, 25))
        self.btnKisitEkle.setObjectName("btnKisitEkle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #Events
        self.btnKisitEkle.clicked.connect(self.kisitEkle)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grafik Çözüm Programı (Maksimizasyon)"))
        self.label_8.setText(_translate("MainWindow", "Adet Denklem"))
        self.groupBox.setTitle(_translate("MainWindow", "Amaç Fonksiyonu"))
        self.label.setText(_translate("MainWindow", "Zmax="))
        self.label_2.setText(_translate("MainWindow", "X1 +"))
        self.label_3.setText(_translate("MainWindow", "X2"))
        self.btnKisitEkle.setText(_translate("MainWindow", "Ekle"))

    def kisitEkle(self):
        kisit_sayi = self.kisitAdet.value()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

