#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

'''
谢尔宾斯基三角形(Sierpinski triangle)
'''

def plot_triangle(A, B, C):
	x = [A[0], B[0], C[0]]
	y = [A[1], B[1], C[1]]

	ax = plt.gca()
	ax.fill(x, y)

def plot_Sierpinski_triangle(A, B, C):
	l = np.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
	if l < 0.2:
		plot_triangle(A, B, C)
		return

	R = [(A[0] + C[0])/2, (A[1] + C[1])/2]
	P = [(A[0] + B[0])/2, (A[1] + B[1])/2]
	Q = [(B[0] + C[0])/2, (B[1] + C[1])/2]
	
	plot_Sierpinski_triangle(A, P, R)
	plot_Sierpinski_triangle(P, B, Q)
	plot_Sierpinski_triangle(R, Q, C)

if __name__ == '__main__':
	A = [1, 1]
	B = [7, 3]
	C = [3, 16]

	plot_Sierpinski_triangle(A, B, C)
	plt.axis('off')
	plt.show()
