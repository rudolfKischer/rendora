from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from src.draw import square, triangle, surface
from .entities import Circle
from .collider import LineSegmentCollider
import numpy as np
import time
from src.element import Element
from time import time
from math import sin, cos, pi
from .utils.vector import *

prev_time = time()

def default_scene():

    #traw a color interpolated square, red, green, blue, yellow
    square_points = [(-0.5, 0.5), (0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)]
    square_colors = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0, 0, 1), (1, 1, 0)]

    #rotate the points based on the time

    square_points = np.array(square_points)
    square_points = np.transpose(square_points)
    # use the fractional part of the time to rotate the square
    time_fraction = ((time.time() * 0.1) % 1) * 2 * np.pi
    rotation_matrix = np.array([[np.cos(time_fraction), -np.sin(time_fraction)], [np.sin(time_fraction), np.cos(time_fraction)]])
    square_points = np.matmul(rotation_matrix, square_points)
    square_points = np.transpose(square_points)

    square(square_points,
              square_colors)

def polygon_test():
    # # draw a triangle
    fractional_time = ((time() * 0.3) % 1)
    period = fractional_time  * 2 * np.pi
    triangle_points = [(-0.5, 0.5), (0.5, 0.5), (0.0, -0.5)]
    frequency = 0.5
    wave_0 = sin(period) * 0.5 + 0.5
    wave_c_0 = cos(period) * 0.5 + 0.5
    wave_1 = (sin(period * frequency* 0.1) * 0.5 + 0.5) * wave_0 * wave_0 
    wave_2 = (cos(period * frequency * 0.3) * 0.5 + 0.5) * wave_1 * wave_0

    triangle_colors = [( 1 - wave_1, wave_2, 0.5), (0.5, wave_1, 1 - wave_2), (wave_1, 0.5,  1 - wave_2)]
    triangle = Polygon(triangle_points, triangle_colors)


    triangle.transform.position = np.array([0.0, 0.0 , -1 - 5.0 * wave_0])
    triangle.transform.orientation = np.array([0.0, 0.0, 0.0])
    triangle.transform.scale = np.array([1.0, 1.0, 1.0])

    surface(triangle)


speed = 2.5

circles = []

borders = [
    LineSegmentCollider(np.array([-1,1,0]),np.array([1,1,0])),
    LineSegmentCollider(np.array([-1,-1,0]),np.array([1,-1,0])),
    LineSegmentCollider(np.array([1,1,0]),np.array([1,-1,0])),
    LineSegmentCollider(np.array([-1,1,0]),np.array([-1,-1,0]))
]

num_circles = 30

for i in range(num_circles):
    rand_z = np.random.uniform(0.0, 0.1)
    circle = Circle(rand_z, [[np.random.uniform(0.0, 1.0), 
                              np.random.uniform(0.0, 1.0), 
                              np.random.uniform(0.0, 1.0)]])
    # generate two random numbers between -1 and 1
    #they should be different evertime the loop happens
    rand_x = np.random.uniform(-1.0, 1.0)
    rand_y = np.random.uniform(-1.0, 1.0)
    direction = normalize(np.array([rand_x, rand_y, 0.0]))
    circle.rigid_body.kinematic.velocity = direction * speed
    circles.append(circle)



def circle_test():
    # draw a circle of radius 0.5, centered at (0, 0, 0) with the colour red
    global prev_time, circles, borders

    #get the time that has passed since the last frame
    current_time = time()
    delta_time = current_time - prev_time
    prev_time = current_time

    for circle in circles:
        for border in borders:
            if circle.rigid_body.sphere_line_collision(border):
                circle.rigid_body.resolve_sphere_line_collision(border)

        # circle.rigid_body.kinematic.velocity[1] -= 1.8 * delta_time
        circle.update(delta_time)  