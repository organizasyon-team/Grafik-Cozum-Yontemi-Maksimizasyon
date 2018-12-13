import matplotlib.pyplot as plt
import numpy as np
import urllib
from matplotlib import style

style.use("ggplot")

x1_1=[0,4]
x2_1=[15,0]

x1_2=[0,8]
x2_2=[8,0]

plt.axis([0, 6, 0, 20])
d1=plt.plot(x1_1, x2_1, label='Denklem 1')
d2=plt.plot(x1_2, x2_2, label="Denklem 2")



plt.title('Maksimizasyon Grafiği')
plt.xlabel('X1')
plt.ylabel('X2')

plt.legend() #show the label

plt.show() #run the graphic





