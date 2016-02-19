#!/usr/bin/env python3

import numpy as np
import pylab

def plotdragon(X, Y):
	x1, x2 = X[0], X[1]
	y1, y2 = Y[0], Y[1]
	l = np.sqrt((x1-x2)**2 + (y1-y2)**2)
	if l < 0.3:
		pylab.plot(X, Y, color='green')
	else:
		a = np.arcsin((y2 - y1) / l)
		b = np.arcsin((x2 - x1) / l)
		xt = (x1 + x2) / 2.0 - l * np.sin(a) / 2.0
		yt = (y1 + y2) / 2.0 + l * np.sin(b) / 2.0
		plotdragon([x1, xt], [y1, yt])
		plotdragon([x2, xt], [y2, yt])

X = [1.0, 15.0]
Y = [4.0, 15.0]
pylab.figure(figsize=(8, 8))
pylab.axis('off')
pylab.xlim(-13, 24)
pylab.ylim(-13, 24)
plotdragon(X, Y)
pylab.show()
