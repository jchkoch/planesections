# -*- coding: utf-8 -*-
R"""
Created on Sun May 23 01:00:41 2021

@author: Christian
Manually used to check if loads are stacking properly!
"""



import planesections as ps
from planesections.units.metric import m, kN
import numpy as np
# import pytest

x = np.array([0,5])
labels = ['A', 'B']
fixities = [np.array([1,1,1]), np.array([1,1,1])]

L       = 5*m
x       = np.linspace(0, L, 80)
beam    = ps.EulerBeam(x)

pinned = [1,1,0]
fixed = [1,1,1]
beam.setFixity(0.4, pinned, label = 'A')
beam.setFixity(L, fixed, label = 'B')

P = -2*kN
M = 5*kN*m
qDist = np.array([0., -kN/m])
qLin = np.array([[0.,0.],[-kN/m, kN/m]])
qLin2 = np.array([[0.,0.],[0.4*kN/m, -3*kN/m]])
qLin3 = np.array([[0.,0.],[-1*kN/m, -3*kN/m]])

beam.addDistLoad(0, 2, qDist, label='test') 
beam.addLinLoad(2, 3, qLin) 
beam.addLinLoad(0, 1, qLin2)
beam.addLinLoad(0, 1, qLin3) 
# beam.addLinLoad(0, 1, -qLin) 

# beam.addDistLoad(2.8, 3.5, qDist)

# beam.addLinLoadVertical(3, 4.5, qLin)
# beam.addLinLoadVertical(3, 4.5, qLin*2)

ps.plotBeamDiagram(beam, labelForce=True)

