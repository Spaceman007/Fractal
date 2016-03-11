#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure

'''
谢尔宾斯基地毯(Sierpinski carpet)
'''

# A,B 是对角点
def plot_rectangle(A, B):
	x = [A[0],B[0],B[0],A[0]]
	y = [A[1],A[1],B[1],B[1]]

	ax = plt.gca()
	ax.fill(x, y, color='g')
	#ax.fill(x, y)

def plot_Sierpinski_carpet(A, B):
	
	if min(np.abs(A[0] - B[0]), np.abs( A[1] - B[1])) < 0.2:
		return

	x1 = A[0] + (B[0] - A[0])/3
	x2 = A[0] + (B[0] - A[0])*2/3
	y1 = A[1] + (B[1] - A[1])/3
	y2 = A[1] + (B[1] - A[1])*2/3

	A1 = [x1, y1]
	B1 = [x2, y2]

	plot_rectangle(A1, B1)

	plot_Sierpinski_carpet(A, A1)
	plot_Sierpinski_carpet(A1, [x2, A[1]])
	plot_Sierpinski_carpet([x2, y1], [B[0], A[1]])
	plot_Sierpinski_carpet(B1, [B[0], y1])
	plot_Sierpinski_carpet(B1, B)
	plot_Sierpinski_carpet(B1, [x1, B[1]])
	plot_Sierpinski_carpet([A[0], B[1]], [x1, y2])
	plot_Sierpinski_carpet(A1, [A[0], y2])

if __name__ == '__main__':
	A = [3,3]
	B = [12,12]
	#matplotlib.figure.Figure(figsize=(8,8))
	plt.figure(figsize=(8,8))
	plot_Sierpinski_carpet(A, B)
	plt.axis('off')
	plt.show()
