#!/usr/bin/env python3

from matplotlib.patches import Circle, Ellipse
import matplotlib.pyplot as plt

'''
一个圆: 在过圆心的垂直和水平线与圆的焦点上分别画四个圆。分形。
'''

def draw_circle(x, y, r):
	ax = plt.gca()
	cir = Circle(xy=(x, y), radius=r, alpha=0.5)
	ax.add_patch(cir)
	ax.plot()


def draw_fractal_circle(x, y, r):
	if r < 3.1:
		draw_circle(x, y, r)
		return

	x1, x2 = x - r, x + r
	y1, y2 = y - r, y + r
	r1 = r * 2 / 3

	draw_fractal_circle(x1, y, r1)
	draw_fractal_circle(x, y1, r1)
	draw_fractal_circle(x2, y, r1)
	draw_fractal_circle(x, y2, r1)

if __name__ == '__main__':
	fig = plt.figure(figsize=(9,9))
	ax = fig.add_subplot(1,1,1)
	ax.axis('equal')
	ax.axis('off')
	draw_fractal_circle(0.0, 0.0, 9.0)
	plt.show()
