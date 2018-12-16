# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import urllib
from PyQt5.QtWidgets import QMainWindow, QApplication
class GrafikGosterim(object):

    def __init__(self, gx1List, gx2List, cx1List ,cx2List):
        self.gx1List = gx1List
        self.gx2List = gx2List
        self.cx1List = cx1List
        self.cx2List = cx2List

    def Cizdir(self):

        plt.axes()
        gca = plt.gca()

        line = plt.Line2D((1, 0), (6, 5), lw=2.5)
        line1 = plt.Line2D((1, 5), (4, 2), lw=2.5)
        gca.add_line(line)
        gca.add_line(line1)

        plt.axis('scaled')
        plt.show()
                






