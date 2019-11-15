#! /usr/bin/env python
"""
Visualize a basic 3D lattice. Run using the command:

    python lattice_basic.py

Need to run it in an environment that has vpython installed.

Leon Hostetler, Nov. 2019

"""
from vpython import vector, sphere, cylinder, color, canvas, distant_light, arrow, label

# Parameters
lattice_size = 5
site_radius = 0.1
link_radius = 0.05


# Site and link colors in RGB (decimal) values
link_color = vector(.26, .75, .96)
site_color = vector(.14, .03, .96)

# Canvas and background color
scene = canvas(title='Lattice',
     width=1000, height=700,
     center=vector(0,0,0), background=color.white)

# Lighting
scene.lights = []
distant_light(direction=vector(2,2,2), color=color.gray(0.9))

# Generate the lattice
for i in range(lattice_size + 1):
    for j in range(lattice_size + 1):
        for k in range(lattice_size + 1):
            sphere(pos=vector(i,j,k),radius=site_radius, color=site_color)
            cylinder(pos=vector(i,j,k), axis=vector(1,0,0), radius=link_radius, color=link_color)
            cylinder(pos=vector(i,j,k), axis=vector(0,1,0), radius=link_radius, color=link_color)
            cylinder(pos=vector(i,j,k), axis=vector(0,0,1), radius=link_radius, color=link_color)

# Create origin/axes
arrow(pos=vector(-1,-1,-1), axis=vector(0,0,1), radius=.1, color=color.green)
arrow(pos=vector(-1,-1,-1), axis=vector(0,1,0), radius=.1, color=color.green)
arrow(pos=vector(-1,-1,-1), axis=vector(1,0,0), radius=.1, color=color.green)
label(pos=vector(0,-1,-1), text='x')
label(pos=vector(-1,0,-1), text='y')
label(pos=vector(-1,-1,0), text='z')
