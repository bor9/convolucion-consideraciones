import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import scipy.signal
import math

from matplotlib import rc

__author__ = 'ernesto'

# if use latex or mathtext
rc('text', usetex=False)


def get_abscissa(m, n, y):
    return (y - n) / m


#
# PLOTS
#
# axis parameters
xmin = -8
xmax = 8
ymin = -7
ymax = 7

fmax = 5.5
fmin = -6.5

font_size = 14

# ticks length
tl = 0.3

# baseline of x label
x_bl = -1.2
# margin and baseline of y label
y_m = 0.5
y_bl = ymax-0.2

fig = plt.figure(1, figsize=(9, 7), frameon=False)
#
# f(t) = 2t + 4
#
m = 2
n = 4
ax = plt.subplot2grid((6, 8), (0, 0), rowspan=3, colspan=4)
plt.axis([xmin, xmax, ymin, ymax])

# axis arrows
plt.annotate("", xytext=(xmin, 0), xycoords='data', xy=(xmax, 0), textcoords='data', color='black',
             arrowprops=dict(width=0.1, headwidth=5, headlength=7, color='black', shrink=0.002))
plt.annotate("", xytext=(0, ymin), xycoords='data', xy=(0, ymax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=7, facecolor='black', shrink=0.002))

# f(t)
plt.plot([get_abscissa(m, n, fmin), get_abscissa(m, n, fmax)], [fmin, fmax], 'k', linewidth=2)
# xticks
for xi in range(xmin+1, xmax):
    plt.plot([xi, xi], [0, tl], 'k', linewidth=0.5)
# yticks
for yi in range(ymin+1, ymax):
    plt.plot([0, tl], [yi, yi], 'k', linewidth=0.5)

# labels
plt.text(xmax, x_bl, r'$t$', fontsize=font_size, ha='right', va='baseline')
plt.text(y_m, y_bl, r'$f(t)=2t+4$', fontsize=font_size, ha='left', va='baseline')
plt.text(-n/m+0.1, 0.5, r'$-2$', fontsize=font_size, ha='right', va='baseline')
plt.text(y_m, n, r'$4$', fontsize=font_size, ha='left', va='center')

plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')

#
# g(t) = f(t-5) = 2t - 6
#
m = 2
n = -6
ax = plt.subplot2grid((6, 8), (0, 4), rowspan=3, colspan=4)
plt.axis([xmin, xmax, ymin, ymax])

# axis arrows
plt.annotate("", xytext=(xmin, 0), xycoords='data', xy=(xmax, 0), textcoords='data', color='black',
             arrowprops=dict(width=0.1, headwidth=5, headlength=7, color='black', shrink=0.002))
plt.annotate("", xytext=(0, ymin), xycoords='data', xy=(0, ymax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=7, facecolor='black', shrink=0.002))

# g(t)
plt.plot([get_abscissa(m, n, fmin), get_abscissa(m, n, fmax)], [fmin, fmax], 'k', linewidth=2)
# xticks
for xi in range(xmin+1, xmax):
    plt.plot([xi, xi], [0, tl], 'k', linewidth=0.5)
# yticks
for yi in range(ymin+1, ymax):
    plt.plot([0, tl], [yi, yi], 'k', linewidth=0.5)

# labels
plt.text(xmax, x_bl, r'$t$', fontsize=font_size, ha='right', va='baseline')
plt.text(y_m, y_bl, r'$g(t)=f(t-5)$', fontsize=font_size, ha='left', va='baseline')
plt.text(-n/m+0.1, 0.5, r'$3$', fontsize=font_size, ha='right', va='baseline')
plt.text(y_m, n, r'$-6$', fontsize=font_size, ha='left', va='center')

plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')

#
# h(t) = g(-t) = -2t - 6
#
m = -2
n = -6
ax = plt.subplot2grid((6, 8), (3, 0), rowspan=3, colspan=4)
plt.axis([xmin, xmax, ymin, ymax])

# axis arrows
plt.annotate("", xytext=(xmin, 0), xycoords='data', xy=(xmax, 0), textcoords='data', color='black',
             arrowprops=dict(width=0.1, headwidth=5, headlength=7, color='black', shrink=0.002))
plt.annotate("", xytext=(0, ymin), xycoords='data', xy=(0, ymax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=7, facecolor='black', shrink=0.002))

# h(t)
plt.plot([get_abscissa(m, n, fmin), get_abscissa(m, n, fmax)], [fmin, fmax], 'k', linewidth=2)
# xticks
for xi in range(xmin+1, xmax):
    plt.plot([xi, xi], [0, tl], 'k', linewidth=0.5)
# yticks
for yi in range(ymin+1, ymax):
    plt.plot([0, tl], [yi, yi], 'k', linewidth=0.5)

# labels
plt.text(xmax, x_bl, r'$t$', fontsize=font_size, ha='right', va='baseline')
plt.text(y_m, y_bl, r'$h(t)=g(-t)$', fontsize=font_size, ha='left', va='baseline')
plt.text(-n/m+0.1, x_bl, r'$-3$', fontsize=font_size, ha='right', va='baseline')
plt.text(y_m, n, r'$-6$', fontsize=font_size, ha='left', va='center')

plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')


#
# i(t) = h(t-4) = -2t + 2
#
m = -2
n = 2
ax = plt.subplot2grid((6, 8), (3, 4), rowspan=3, colspan=4)
plt.axis([xmin, xmax, ymin, ymax])

# axis arrows
plt.annotate("", xytext=(xmin, 0), xycoords='data', xy=(xmax, 0), textcoords='data', color='black',
             arrowprops=dict(width=0.1, headwidth=5, headlength=7, color='black', shrink=0.002))
plt.annotate("", xytext=(0, ymin), xycoords='data', xy=(0, ymax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=7, facecolor='black', shrink=0.002))

# h(t)
plt.plot([get_abscissa(m, n, fmin), get_abscissa(m, n, fmax)], [fmin, fmax], 'k', linewidth=2)
# xticks
for xi in range(xmin+1, xmax):
    plt.plot([xi, xi], [0, tl], 'k', linewidth=0.5)
# yticks
for yi in range(ymin+1, ymax):
    plt.plot([0, tl], [yi, yi], 'k', linewidth=0.5)

# labels
plt.text(xmax, x_bl, r'$t$', fontsize=font_size, ha='right', va='baseline')
plt.text(y_m, y_bl, r'$i(t)=h(t-4)$', fontsize=font_size, ha='left', va='baseline')
plt.text(-n/m-0.1, x_bl, r'$1$', fontsize=font_size, ha='center', va='baseline')
plt.text(-y_m, n, r'$2$', fontsize=font_size, ha='right', va='center')

plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')


plt.savefig('function_transformations.eps', format='eps', bbox_inches='tight')
plt.show()

