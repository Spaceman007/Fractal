#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

'''
Arboresent肺
'''

def plot_arboresent_triangle(A, B, C, coe):
	A1 = [B[0] + (C[0] - B[0])*coe, B[1] + (C[1] - B[1])*coe]
	A2 = [C[0] - (C[0] - B[0])*coe, C[1] - (C[1] - B[1])*coe]

	if np.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2) < 0.2:
		ax = plt.gca()
		ax.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]])
		return

	plot_arboresent_triangle(A1, B, A, coe)
	plot_arboresent_triangle(A2, A, C, coe)

def plot_arboresent(l, alpha, beta):
	O = [0, 0]
	A = [-l * np.sin(alpha), l * np.cos(alpha)]
	B = [l * np.sin(alpha), l * np.cos(alpha)]

	l1 = l / np.cos(beta) / 2
	A1 = [-l1 * np.sin(alpha + beta), l1 * np.cos(alpha + beta)]
	B1 = [l1 * np.sin(alpha + beta), l1 * np.cos(alpha + beta)]

	l2 = l1 / np.cos(beta) / 2

	coe = l2 / l

	plot_arboresent_triangle(A1, A, O, coe)
	plot_arboresent_triangle(B1, B, O, coe)

if __name__ == '__main__':
	plt.figure(figsize=(9, 9))
	plot_arboresent(7, 0.05, 0.75)
	plt.axis('off')
	plt.show()
