#!/usr/bin/env python3

import numpy as np
import pylab
import random

'''
分形树: 在一条线段的末端分出两段
'''

def get_random_color():
	dic = {0:'b', 1:'g', 2:'r', 3:'c', 4:'m', 5:'y', 6:'k', 7:'w'}
	i = random.randint(0, 6)
	return(dic[i])

def plot_tree(P, Q, ang=0.5, color='g'):
	xp, yp = P[0], P[1]
	xq, yq = Q[0], Q[1]

	l = np.sqrt((xp - xq)**2 + (yp - yq)**2)
	if l < 0.6:
		return

	# 求角度
	ang_b = np.arccos((xq - xp) / l)
	if yq < yp:
		ang_b = 2*np.pi - ang_b

	# 求新的坐标
	xq1 = xq + l*np.cos(ang_b + ang) * 4 / 5
	yq1 = yq + l*np.sin(ang_b + ang) * 4 / 5
	xq2 = xq + l*np.cos(ang_b - ang) * 4 / 5
	yq2 = yq + l*np.sin(ang_b - ang) * 4 / 5
	
	pylab.plot([xp, xq], [yp, yq], color=color)

	# 画新线段
	new_color = get_random_color()
	plot_tree(Q, [xq1, yq1], ang, new_color)
	plot_tree(Q, [xq2, yq2], ang, new_color)

if __name__ == "__main__":
	P = [5.0, 0.0]
	Q = [3.0, 6.0]
	pylab.figure(figsize=(8,8))
	pylab.axis('off')
	plot_tree(P, Q, 0.32, 'g')
	pylab.show()
