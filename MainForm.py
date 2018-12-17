# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


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

        # Events
        self.btnKisitEkle.clicked.connect(self.addKisit)
        self.btnCikar.clicked.connect(self.discardKisit)
        self.btnHesapla.clicked.connect(self.hesapla)
        self.listKisitlar.currentItemChanged.connect(self.changeListItem)

        # Lists
        self.x1 = []
        self.x2 = []
        self.z1 = []

        # GrafikList
        self.gx1 = []
        self.gx2 = []

        # Doğruların Çarpışma Noktaları (x1, x2)
        self.cX1 = []
        self.cX2 = []

        # Çakışma nokta değerleri
        self.cValues = []

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

        if (x1Value != 0 or x2Value != 0):
            self.x1.append(x1Value)
            self.x2.append(x2Value)
            self.z1.append(z1Value)

            if(x1Value == 0):
                self.gx1.append(0)
            else:
                self.gx1.append(z1Value / x1Value)
            self.gx2.append(z1Value / x2Value)

            if (len(self.x1) >= 2):
                self.btnHesapla.setEnabled(True)

            if (x2Value > 0):
                item = str(x1Value) + "x1 + " + str(x2Value) + "x2 <= " + str(z1Value)
            else:
                item = str(x1Value) + "x1 " + str(x2Value) + "x2 <= " + str(z1Value)
            self.listKisitlar.addItem(item)

    def discardKisit(self):
        listModel = self.listKisitlar.model()
        index_num = self.listKisitlar.indexFromItem(self.listKisitlar.selectedItems()[0]).row()
        listModel.removeRow(index_num)

        self.x1.remove(self.x1[index_num])
        self.x2.remove(self.x2[index_num])
        self.z1.remove(self.z1[index_num])
        self.gx1.remove(self.gx1[index_num])
        self.gx2.remove(self.gx2[index_num])

    def changeListItem(self):
        self.btnCikar.setEnabled(True)

    def hesapla(self):
        # Listelerdeki önceki değerleri sil
        self.cValues[:] = []
        self.cX1[:] = []
        self.cX2[:] = []
        
        for i in range(0, len(self.x1) - 1):
            for j in range(i + 1, len(self.x1)):
                # Çakışan doğruların ortak çözümü ile x1 ve x2 değerlerinin bulunması
                A = np.array([[self.x1[i], self.x2[i]], [self.x1[j], self.x2[j]]])
                B = np.array([[self.z1[i]], [self.z1[j]]])
                C = np.dot(np.linalg.inv(A), B)

                if C[0] > 0 or C[1] > 0:
                    isOptimum = False
                    for j in range(0, len(self.x1)):
                        sonuc = C[0] * self.x1[j] + C[1] * self.x2[j]
                        if(sonuc <= self.z1[j]):
                            isOptimum = True
                        else:
                            isOptimum = False
                            break

                    if(isOptimum):
                        self.cX1.append(C[0])
                        self.cX2.append(C[1])

                        # Bulunan x1 ve x2 değerlerinin Zmaksda yerine yazılması
                        cValue = self.zmaksX1.value() * C[0] + self.zmaksX2.value() * C[1]
                        self.cValues.append(cValue[0])
                        print(cValue[0])
        enBuyukX = 0
        enBuyukY = 0
        enKucukX = 999
        enKucukY = 999
        for i in range(0, len(self.gx1)):
            if enBuyukX < self.gx1[i]:
                enBuyukX = self.gx1[i]
            if enBuyukY < self.gx2[i]:
                enBuyukY = self.gx2[i]
            if enKucukX > self.gx1[i] and self.gx1[i]>0:
                enKucukX = self.gx1[i]
            if enKucukY > self.gx2[i] and self.gx2[i]>0:
                enKucukY = self.gx2[i]
        style.use('ggplot')
        plt.plot([0,0],[enBuyukX,0], color = 'k' ,lw = 3)
        ax = plt.axes()
        ax.arrow(0,0,enBuyukX,0, head_width = 0.2, head_length = 0.2, fc = 'k', ec = 'k')
        plt.plot([0,enBuyukY],[0,0], color = 'k' ,lw = 3)
        ax.arrow(0,0,0,enBuyukY, head_width = 0.2, head_length = 0.2, fc = 'k', ec = 'k')

        for i in range(0, len(self.gx1)):
            if self.gx1[i] == 0:
                plt.plot([self.gx2[i] + 5, self.gx1[i]],[self.gx2[i], self.gx2[i]], label=str(self.x1[i]) + "x1 + " + str(self.x2[i]) + "x2 <= " + str(self.z1[i]))
            elif self.gx1[i] < 0 or self.gx2[i] < 0:
                plt.plot([5, self.gx1[i]], [self.gx2[i] + 5, 0], label=str(self.x1[i]) + "x1 + " + str(self.x2[i]) + "x2 <= " + str(self.z1[i]))
            else:
                plt.plot([0, self.gx1[i]], [self.gx2[i], 0], label=str(self.x1[i]) + "x1 + " + str(self.x2[i]) + "x2 <= " + str(self.z1[i]))
        print("Cakisma Sayi  : " + str(len(self.cX1)))

        plt.scatter([0,0],[enKucukY,0], s=100)
        plt.scatter([0, enKucukX], [0, 0], s=100)
        
        for i in range(0, len(self.cX1)):
            plt.scatter(self.cX1[i],self.cX2[i], s=100,label=chr(65+i) + " : " + str(self.cValues[i]))

        
            
        
        plt.title("Maksimizasyon Grafigi")
        plt.xlabel("X1")
        plt.ylabel("X2")

        plt.legend()  # show the label

        plt.show()  # run the graphic


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())