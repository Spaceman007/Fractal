#!/usr/bin/env python3

import numpy as np
import pylab

'''
分形树：在2/3处和末端长出4个branches，同时末端偏移一个角度延伸一段距离
'''

def get_new_point(P, Q, left, ang, coe=0.7):
	xp, yp = P[0], P[1]
	xq, yq = Q[0], Q[1]

	l = np.sqrt((xp - xq)**2 + (yp - yq)**2)

	# 求角度
	ang_b = np.arccos((xq - xp) / l)
	if yq < yp: 
		ang_b = 2*np.pi - ang_b

	# 求新的坐标
	if left:
		xqn = xq + l*np.cos(ang_b + ang) * coe
		yqn = yq + l*np.sin(ang_b + ang) * coe
	else:
		xqn = xq + l*np.cos(ang_b - ang) * coe
		yqn = yq + l*np.sin(ang_b - ang) * coe

	return [xqn, yqn]
	
def plot_tree(P, Q, a1, a2,  b):
	xp, yp = P[0], P[1]
	xq, yq = Q[0], Q[1]

	l = np.sqrt((xp-xq)**2 + (yp-yq)**2)
	if l < 0.3:
		return

	#P1
	xp1, yp1 = xp + (xq - xp) * 2 / 3, yp + (yq - yp) * 2 / 3

	Nd1 = get_new_point(P, [xp1, yp1], True, a1, 0.8)
	Nd2 = get_new_point(P, [xp1, yp1], False, a1, 0.8)

	Nu1 = get_new_point(P, Q, True, a2, 0.3)
	Nu2 = get_new_point(P, Q, False, a2, 0.3)

	Q1 = get_new_point(P, Q, True, b, 0.7)

	#画线
	pylab.plot([xp, xq], [yp, yq], color='g') # PQ
	
	plot_tree([xp1, yp1], Nd1, a1, a2, b)
	plot_tree([xp1, yp1], Nd2, a1, a2, b)
	plot_tree(Q, Nu1, a1, a2, b)
	plot_tree(Q, Nu2, a1, a2, b)
	plot_tree(Q, Q1, a1, a2, b)

if __name__ == "__main__":
	P = [5.0, 0.0]
	Q = [3.0, 9.0]
	pylab.figure(figsize=(8,8))
	pylab.axis('off')
	plot_tree(P, Q, 0.8, 0.3, 0.4)
	pylab.show()
