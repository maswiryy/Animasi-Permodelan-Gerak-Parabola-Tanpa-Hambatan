""" Sebuah program untuk membuat animasi simulasi gerak parabola yang kecepatan dan sudut elevasinya ditentukan oleh input user.
#maswiryy

import math
from math import sin, cos, radians
import matplotlib.pyplot as plt
import numpy as np


Vo = float(input("Masukkan nilai kecepatan awal(m/s): "))
theta = float(input("Masukkan sudut awal pelemparan bola(°) :"))


g = 9.8
t_total = 2 * Vo * sin(radians(theta)) / g
jarak = math.pow(Vo, 2) * sin(radians(2 * theta)) / g
h_max = math.pow(Vo, 2) * math.pow(sin(radians(theta)), 2) / (2 * g)
Vox = Vo*cos(radians(theta))
Voy = Vo*sin(radians(theta))

step = 45

time = np.linspace(0.0, t_total, step)

plt.figure(1)
plt.suptitle('Animasi Permodelan Gerak Parabola Tanpa Hambatan')
plt.xlabel("Jarak horizontal (m)")
plt.ylabel("Ketinggian (m)")
plt.grid()

for t in time:
    x1 = Vox*t
    y1 = Voy*t - 0.5*g*np.power(t, 2)
    plt.annotate('%.2f s' % t, xy=(x1, y1), horizontalalignment='center', verticalalignment='bottom',fontsize='8')
    plt.plot([x1], [y1], 'go', markersize=6)
    plt.pause(t_total/step)

plt.show()

print('Total waktu =' ,t_total)
print('Ketinggian maksimum yanag ditempuh=', h_max)
print('Jarak horizontal maksimum yang ditempuh=' ,jarak)

