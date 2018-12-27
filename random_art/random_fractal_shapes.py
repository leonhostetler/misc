#! /usr/bin/env python
"""
Creates images with 'random' fractal shapes. Change the bounds on random
for num_vertices and alpha for even more varied "art".

Set num_vertices = 3, and alpha = 1.0 to get only (skewed) Sierpinski triangles.

Leon Hostetler, Feb. 3, 2017

USAGE: python random_fractal_shapes.py
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import random

# Main body of program

points = 100000  # The number of points to use.


def new_point(p, alpha):
    """
    This function takes in a point p, chooses a random vertex
    of the triangle, then returns the midpoint between p and
    the random vertex.
    """
    v = random.choice(vertices)     # Choose a random vertex
    mid = [0, 0]
    mid[0] = alpha*(p[0] + v[0])/2        # x-coordinate of midpoint
    mid[1] = alpha*(p[1] + v[1])/2        # y-coordinate of midpoint
    return mid

# Generate random vertices
def make_vertices():
    num_vertices = random.randint(3, 5)
    for h in range(num_vertices):
        vertx = random.uniform(-100.0, 100.0)
        verty = random.uniform(-100.0, 100.0)
        vert = [vertx, verty]
        vertices.append(vert)

    # Plot the vertices as well
    for j in range(len(vertices)):
        X.append(vertices[j][0])
    for j in range(len(vertices)):
        Y.append(vertices[j][1])


# Generate a large number of points
def generate_points(p, ps, alpha):
    for j in range(ps):
        p = new_point(p, alpha)
        x.append(p[0])
        y.append(p[1])


def make_image(run, alpha):
    plt.rc('text', usetex=True)
    plt.scatter(x, y, c='k', s=.001)
    plt.scatter(X, Y)
    plt.axis('Off')
    plt.axes().set_aspect('equal')
    myTitle = r"$\alpha = $ " + str(alpha)
    plt.title(myTitle)
    filename = "random_art" + str(run) + ".png"
    plt.savefig("random_art/"+filename)
    plt.clf()


for i in range(10):  # The number of images to make
    x = []  # A list of x-coordinates
    y = []  # A list of y-coordinates
    X = []
    Y = []
    vertices = []
    alpha = random.uniform(0.5, 1.5)  # Midpoint multiplier

    # Set the starting point
    point = [0, 0]
    x.append(point[0])
    y.append(point[1])
    make_vertices()
    generate_points(point, points, alpha)
    print("Images Produced: ", i+1)
    make_image(i, alpha)
