import matplotlib.pyplot as plt
from scipy.linalg import solve
import numpy as np
from matplotlib.patches import Circle

'''
求三角形外接圆和内切圆
'''

def plot_triangle(A, B, C):
	x = [A[0], B[0], C[0], A[0]]
	y = [A[1], B[1], C[1], A[1]]

	ax = plt.gca()
	ax.plot(x, y, linewidth=2)

def draw_circle(x, y, r):
	ax = plt.gca()
	cir = Circle(xy=(x, y), radius=r, alpha=0.5)
	ax.add_patch(cir)
	ax.plot()

# 外接圆
def get_outer_circle(A, B, C):
	xa, ya = A[0], A[1]
	xb, yb = B[0], B[1]
	xc, yc = C[0], C[1]

	# 两条边的中点
	x1, y1 = (xa + xb) / 2.0, (ya + yb) / 2.0
	x2, y2 = (xb + xc) / 2.0, (yb + yc) / 2.0

	ka = (yb - ya) / (xb - xa) if xb != xa else None
	kb = (yc - yb) / (xc - xb) if xc != xb else None
	
	alpha = np.arctan(ka) if ka != None else np.pi / 2
	beta  = np.arctan(kb) if kb != None else np.pi / 2

	# 两条垂直平分线的斜率
	k1 = np.tan(alpha + np.pi / 2)
	k2 = np.tan(beta + np.pi / 2)

	# 圆心
	y, x = solve([[1.0, -k1], [1.0, -k2]], [y1 - k1 * x1, y2 - k2 * x2])
	# 半径
	r1 = np.sqrt((x - xa)**2 + (y - ya)**2)

	return(x, y, r1)

# 内切圆
def get_inner_circle(A, B, C):
	xa, ya = A[0], A[1]
	xb, yb = B[0], B[1]
	xc, yc = C[0], C[1]

	ka = (yb - ya) / (xb - xa) if xb != xa else None
	kb = (yc - yb) / (xc - xb) if xc != xb else None
	
	alpha = np.arctan(ka) if ka != None else np.pi / 2
	beta  = np.arctan(kb) if kb != None else np.pi / 2

	a = np.sqrt((xb - xc)**2 + (yb - yc)**2)
	b = np.sqrt((xa - xc)**2 + (ya - yc)**2)
	c = np.sqrt((xa - xb)**2 + (ya - yb)**2)

	ang_a = np.arccos((b**2 + c**2 - a**2) / (2 * b * c))
	ang_b = np.arccos((a**2 + c**2 - b**2) / (2 * a * c))

	# 两条角平分线的斜率
	k1 = np.tan(alpha + ang_a / 2)
	k2 = np.tan(beta + ang_b / 2)
	kv = np.tan(alpha + np.pi / 2)
	
	# 求圆心
	y, x = solve([[1.0, -k1], [1.0, -k2]], [ya - k1 * xa, yb - k2 * xb])
	ym, xm = solve([[1.0, -ka], [1.0, -kv]], [ya - ka * xa, y - kv * x])
	r1 = np.sqrt((x - xm)**2 + (y - ym)**2)

	return(x, y, r1)

if __name__ == '__main__':
	A = (1., 1.)
	B = (5., 2.)
	C = (5., 5.)

	plt.axis('equal')
	plt.axis('off')
	plot_triangle(A, B, C)

	x, y, r1 = get_outer_circle(A, B, C)
	plt.plot(x, y, 'ro')
	draw_circle(x, y, r1)

	x_inner, y_inner, r_inner = get_inner_circle(A, B, C)
	plt.plot(x_inner, y_inner, 'ro')
	draw_circle(x_inner, y_inner, r_inner)

	plt.show()
