#! /usr/bin/env python
"""
Staggered sign function visualization. Run using the command:

    python lattice_staggered-phases.py

Need to run it in an environment that has vpython installed.

Leon Hostetler, Nov. 2019

"""
import numpy as np
from vpython import vector, sphere, cylinder, color, canvas, distant_light, arrow, label

#########################################################################
###                          FUNCTIONS
#########################################################################

def color_sites(site_color_matrix, lattice_size):
    """
        Edit this function to color the lattice sites as you wish
    """
    for i in range(lattice_size):
        for j in range(lattice_size):
            for k in range(lattice_size):
                site_color_matrix[i,j,k] = vector(0,1,0)


def color_links(xlinks_color, ylinks_color, zlinks_color, lattice_size):
    """
        Edit this function to color the lattice links as you wish
    """
    for i in range(lattice_size):
        for j in range(lattice_size):
            for k in range(lattice_size):
                xlinks_color[i,j,k] = vector(0,0,1)

                if i%2==0:
                    ylinks_color[i,j,k] = vector(0,0,1)
                else:
                    ylinks_color[i,j,k] = vector(1,0,0)

                if (i+j)%2==0:
                    zlinks_color[i,j,k] = vector(0,0,1)
                else:
                    zlinks_color[i,j,k] = vector(1,0,0)


def size_sites(site_radius, lattice_size):
    """
        Edit this function to size the lattice sites as you wish
    """
    for i in range(lattice_size):
        for j in range(lattice_size):
            for k in range(lattice_size):
                site_radius[i,j,k] = 0.0*site_radius[i,j,k]


def size_links(xlinks_size, ylinks_size, zlinks_size, lattice_size):
    """
        Edit this function to size the lattice link radii as you wish
    """
    for i in range(lattice_size):
        for j in range(lattice_size):
            for k in range(lattice_size):
                if i%2==0 or i==0:
                    xlinks_size[i,j,k] = 0.05*xlinks_size[i,j,k]
                else:
                    xlinks_size[i,j,k] = 0.005*xlinks_size[i,j,k]

                if j%2==0 or j==0:
                    ylinks_size[i,j,k] = 0.05*ylinks_size[i,j,k]
                else:
                    ylinks_size[i,j,k] = 0.005*ylinks_size[i,j,k]

                if k%2==0 or k==0:
                    zlinks_size[i,j,k] = 0.05*zlinks_size[i,j,k]
                else:
                    zlinks_size[i,j,k] = 0.005*zlinks_size[i,j,k]

#########################################################################
###                          MAIN PROGRAM
#########################################################################

# Parameters
lattice_size = 11       # Lattice size
op = 2                  # Opacity parameter
show_axes = 0           # 1=true, 0=false

# Canvas and background color
scene = canvas(title='Lattice',
     width=1000, height=700,
     center=vector(0,0,0), background=color.white)

# Lighting
scene.lights = []
distant_light(direction=vector(-2,-2,-2), color=color.gray(0.9))

# Set up arrays
site_radii = np.ones((lattice_size,lattice_size,lattice_size))
site_color = np.zeros((lattice_size,lattice_size,lattice_size), dtype=vector)
link_radii_x = np.ones((lattice_size,lattice_size,lattice_size))
link_radii_y = np.ones((lattice_size,lattice_size,lattice_size))
link_radii_z = np.ones((lattice_size,lattice_size,lattice_size))
linkx_color = np.zeros((lattice_size,lattice_size,lattice_size), dtype=vector)
linky_color = np.zeros((lattice_size,lattice_size,lattice_size), dtype=vector)
linkz_color = np.zeros((lattice_size,lattice_size,lattice_size), dtype=vector)

# Color and size the sites and links
color_sites(site_color, lattice_size)
color_links(linkx_color, linky_color, linkz_color, lattice_size)
size_sites(site_radii, lattice_size)
size_links(link_radii_x, link_radii_y, link_radii_z, lattice_size)


# Generate lattice
for i in range(lattice_size+1):
    for j in range(lattice_size+1):
        for k in range(lattice_size+1):
            op_factor = 6/((i+1)**op + (j+1)**op + (k+1)**op)
            sphere(pos=vector(i,j,k),
                    radius=site_radii[i-1,j-1,k-1],
                    color=site_color[i-1,j-1,k-1],
                    opacity=op_factor)

for i in range(lattice_size):
    for j in range(lattice_size):
        for k in range(lattice_size):
            op_factor = 6/((i+1)**op + (j+1)**op + (k+1)**op)
            cylinder(pos=vector(i,j,k),
                    axis=vector(1,0,0),
                    radius=link_radii_x[i,j,k],
                    color=linkx_color[i,j,k],
                    opacity=op_factor)
            cylinder(pos=vector(i,j,k),
                    axis=vector(0,1,0),
                    radius=link_radii_y[i,j,k],
                    color=linky_color[i,j,k],
                    opacity=op_factor)
            cylinder(pos=vector(i,j,k),
                    axis=vector(0,0,1),
                    radius=link_radii_z[i,j,k],
                    color=linkz_color[i,j,k],
                    opacity=op_factor)

# Create origin/axes
if(show_axes):
    arrow(pos=vector(-1,-1,-1), axis=vector(0,0,1), radius=.1, color=color.green)
    arrow(pos=vector(-1,-1,-1), axis=vector(0,1,0), radius=.1, color=color.green)
    arrow(pos=vector(-1,-1,-1), axis=vector(1,0,0), radius=.1, color=color.green)
    label(pos=vector(0,-1,-1), text='x')
    label(pos=vector(-1,0,-1), text='y')
    label(pos=vector(-1,-1,0), text='z')
