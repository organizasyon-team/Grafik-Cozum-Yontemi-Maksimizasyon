# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 91))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 28, 321, 61))
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
        self.btnKisitEkle.setGeometry(QtCore.QRect(290, 110, 41, 31))
        self.btnKisitEkle.setObjectName("btnKisitEkle")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 110, 271, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 271, 28))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sbx1 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.sbx1.setObjectName("sbx1")
        self.sbx1.setMinimum(-999)
        self.sbx1.setMaximum(999)
        self.horizontalLayout.addWidget(self.sbx1)
        self.lblx1 = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblx1.setObjectName("lblx1")
        self.horizontalLayout.addWidget(self.lblx1)
        self.sbx2 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.sbx2.setMinimum(-999)
        self.sbx2.setMaximum(999)
        self.sbx2.setObjectName("sbx2")
        self.horizontalLayout.addWidget(self.sbx2)
        self.lblx2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblx2.setObjectName("lblx2")
        self.horizontalLayout.addWidget(self.lblx2)
        self.sbz1 = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.sbz1.setObjectName("sbz1")
        self.horizontalLayout.addWidget(self.sbz1)
        self.lblX1X2 = QtWidgets.QLabel(self.centralwidget)
        self.lblX1X2.setGeometry(QtCore.QRect(10, 160, 121, 17))
        self.lblX1X2.setObjectName("lblX1X2")
        self.lblFonksiyon = QtWidgets.QLabel(self.centralwidget)
        self.lblFonksiyon.setGeometry(QtCore.QRect(10, 140, 131, 16))
        self.lblFonksiyon.setObjectName("lblFonksiyon")

        self.listKisitlar = QtWidgets.QListWidget(self.centralwidget)
        self.listKisitlar.setGeometry(QtCore.QRect(10, 180, 321, 311))
        self.listKisitlar.setObjectName("listKisitlar")

        self.btnHesapla = QtWidgets.QPushButton(self.centralwidget)
        self.btnHesapla.setGeometry(QtCore.QRect(170, 500, 161, 40))
        self.btnHesapla.setObjectName("btnHesapla")
        self.btnHesapla.setEnabled(False)

        self.btnCikar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCikar.setGeometry(QtCore.QRect(10, 500, 156, 41))
        self.btnCikar.setObjectName("btnCikar")
        self.btnCikar.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Events
        self.btnKisitEkle.clicked.connect(self.addKisit)
        self.btnCikar.clicked.connect(self.discardKisit)
        self.btnHesapla.clicked.connect(self.hesapla)
        self.listKisitlar.currentItemChanged.connect(self.changeListItem)

        #Lists
        self.x1 = []
        self.x2 = []
        self.z1 = []

        self.lines = []

        #Doğruların Çarpışma Noktaları (x1, x2)
        self.cX1 = []
        self.cX2 = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grafik Çözüm Programı (Maksimizasyon)"))
        self.groupBox.setTitle(_translate("MainWindow", "Amaç Fonksiyonu"))
        self.label.setText(_translate("MainWindow", "Zmax="))
        self.label_2.setText(_translate("MainWindow", "X1    +"))
        self.label_3.setText(_translate("MainWindow", "X2"))
        self.btnKisitEkle.setText(_translate("MainWindow", "Ekle"))
        self.lblx1.setText(_translate("MainWindow", "X1 +"))
        self.lblx2.setText(_translate("MainWindow", "X2 <="))
        self.lblX1X2.setText(_translate("MainWindow", "X1 >= 0,  X2 >= 0"))
        self.lblFonksiyon.setText(_translate("MainWindow", "Fonksiyon Kısıtları"))
        self.btnHesapla.setText(_translate("MainWindow", "Hesapla"))
        self.btnCikar.setText(_translate("MainWindow", "Kısıtı Çıkar"))

    def addKisit(self):
        x1Value = self.sbx1.value()
        x2Value = self.sbx2.value()
        z1Value = self.sbz1.value()
        self.sbx1.setValue(0)
        self.sbx2.setValue(0)
        self.sbz1.setValue(0)

        if(x1Value != 0 or x2Value != 0):
            self.x1.append(x1Value)
            self.x2.append(x2Value)
            self.z1.append(z1Value)

            if(len(self.x1) >= 2):
                self.btnHesapla.setEnabled(True)

            if(x2Value > 0):
                item = str(x1Value) + "x1 + " + str(x2Value) + "x2 <= " + str(z1Value)
            else:
                item = str(x1Value) + "x1 " + str(x2Value) + "x2 <= " + str(z1Value)
            self.listKisitlar.addItem(item)

    def discardKisit(self):
        listModel = self.listKisitlar.model()
        index_num = self.listKisitlar.indexFromItem(self.listKisitlar.selectedItems()[0]).row()
        print(index_num)
        listModel.removeRow(index_num)

        self.x1.remove(self.x1[index_num])
        self.x2.remove(self.x2[index_num])
        self.z1.remove(self.z1[index_num])

    def changeListItem(self):
        self.btnCikar.setEnabled(True)


    def hesapla(self):
        for i in range(0, len(self.x1)):
            for j in range(i + 1, len(self.x1)):
                L1 = self.line([0, self.z1[i] / self.x2[i]], [self.z1[i] / self.x1[i], 0])
                L2 = self.line([0, self.z1[j] / self.x2[j]], [self.z1[j] / self.x1[j], 0])
                R = self.intersection(L1, L2)
                if R:
                    self.cX1.append(R[0])
                    self.cX2.append(R[1])
                    #print ("Çakışma Noktası : ", R)
                    


    def line(self, p1, p2):
        A = (p1[1] - p2[1])
        B = (p2[0] - p1[0])
        C = (p1[0]*p2[1] - p2[0]*p1[1])
        return A, B, -C

    def intersection(self, L1, L2):
        D  = L1[0] * L2[1] - L1[1] * L2[0]
        Dx = L1[2] * L2[1] - L1[1] * L2[2]
        Dy = L1[0] * L2[2] - L1[2] * L2[0]
        if D != 0:
            x = Dx / D
            y = Dy / D
            return x,y
        else:
            return False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
