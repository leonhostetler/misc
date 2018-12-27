#! /usr/bin/env python
"""
Plot fractal shapes using an implementation of random.

Leon Hostetler, Feb. 3, 2017

USAGE: python fractal_shapes.py
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import random

# Main body of program

points = 100000  # The number of points to use.

x = []  # A list of x-coordinates
y = []  # A list of y-coordinates

# Set the starting point
point = [0, 0]
x.append(point[0])
y.append(point[1])

# Vertices of the fractal shape. Uncomment different lines for different shapes.
#vertices = [[-1.0, 0.0], [0.0, np.sqrt(3)], [1.0, 0.0]] # Sierpinski triangle
vertices = [[-100.0, 100.0], [100.0, 100.0], [-100.0, -100.0], [100.0, -100.0], [0, 0]] #Square
#vertices = [[-100.0, 100.0], [0.0, 100.0], [100.0, 100, 0], [-100.0, -100.0], [0.0, -100.0], [100.0, -100, 0]] # Square 2
#vertices = [[-100.0, 100.0], [-33.3, 100.0], [33.3, 100.0], [100.0, 100, 0], [-100.0, -100.0], [-33.3, -100.0], [33.3, -100.0], [100.0, -100, 0]] #Square 3


def new_point(p):
    """
    This function takes in a point p, chooses a random vertex
    of the triangle, then returns the midpoint between p and
    the random vertex.
    """
    v = random.choice(vertices)     # Choose a random vertex
    mid = [0, 0]
    mid[0] = (p[0] + v[0])/2        # x-coordinate of midpoint
    mid[1] = (p[1] + v[1])/2        # y-coordinate of midpoint
    return mid

# Generate a large number of points
for i in range(points):
    point = new_point(point)
    x.append(point[0])
    y.append(point[1])

# Plot the vertices as well
X = []
Y = []
for i in range(len(vertices)):
    X.append(vertices[i][0])
for i in range(len(vertices)):
    Y.append(vertices[i][1])

# Plot the results
plt.scatter(x, y, c='k', s=.001)
plt.scatter(X, Y)
plt.axis('Off')
plt.axes().set_aspect('equal')
#plt.savefig("shape.png")
plt.show()
