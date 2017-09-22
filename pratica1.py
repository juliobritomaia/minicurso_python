#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:29:13 2017

@author: labsim
"""
#Definindo as variaveis e equaçoes

import numpy as np
import matplotlib.pyplot as plt

i1,i2 = .8, .3

theta = np.linspace(-3,3, 1000)

l11 = (3 + np.cos(2*theta))*.001
l22 = .3*np.cos(theta)
l12 = 30 + (10*np.cos(2*theta))

W = .5*l11*i1**2 + l12*i1*i2 + .5*l22*i2**2
T_total = np.diff(W)

W_relut = .5*l11*(i1**2) + .5*l22*(i2**2)
W_mutuo = l12*i1*i2

T_r = np.diff(W_relut)
T_m = np.diff(W_mutuo)

#Plotando graficos

plt.figure(1,[10,7])
plt.subplot(311)
plt.plot(theta[0:len(theta)-1], T_total, 'r')
plt.title("Torque Total")
plt.ylabel("Torque [N-m]")
plt.xlabel("$\Theta$ [radians]")
plt.grid()

plt.subplot(312)
plt.plot(theta[0:len(theta)-1], T_r, 'b')
plt.title("Torque Relutancia")
plt.ylabel("Torque [N.m]")
plt.xlabel("$\Theta$ [radians]")
plt.grid()

plt.subplot(313)
plt.plot(theta[0:len(theta)-1], T_m, 'g')
plt.title("Torque Mutuo")
plt.ylabel("Torque [N.m]")
plt.xlabel("$\Theta$ [radians]")
plt.grid()

plt.tight_layout()
plt.show()