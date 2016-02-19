#!/usr/bin/env python3

import numpy as np
import pylab

def kochplot(X, Y):
	x1, x2 = X[0], X[1]
	y1, y2 = Y[0], Y[1]
	l = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	if l < 0.2:
		pylab.plot(X, Y, color='red', linewidth=1.0, linestyle='-')
	else:
		xa = x1 + (x2 - x1) / 3.0
		ya = y1 + (y2 - y1) / 3.0
		xc = x2 - (x2 - x1) / 3.0
		yc = y2 - (y2 - y1) / 3.0
		a = np.arcsin((y2 - y1) / l)
		b = np.arcsin((x2 - x1) / l)
		xb = (x1 + x2) / 2.0 - np.sqrt(3) * np.sin(a) * l / 6.0
		yb = (y1 + y2) / 2.0 + np.sqrt(3) * np.sin(b) * l / 6.0
		kochplot([x1, xa], [y1, ya])
		kochplot([xa, xb], [ya, yb])
		kochplot([xb, xc], [yb, yc])
		kochplot([xc, x2], [yc, y2])

#X = [2.0, 5.0, 10.0]
#Y = [5.2, np.sqrt(3)*5.0, 0.0]
X = [0.0, 5.0, 10.0]
Y = [0.0, np.sqrt(3)*5.0, 0.0]

pylab.figure(figsize=(8, 8), dpi=80)
pylab.axis('off')

kochplot([X[0], X[1]], [Y[0], Y[1]])
kochplot([X[1], X[2]], [Y[1], Y[2]])
kochplot([X[2], X[0]], [Y[2], Y[0]])
pylab.xlim(-4.0, 11.0)
pylab.ylim(-4.0, 11.0)
pylab.show()
