from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from src.draw import square, triangle, surface
import numpy as np
import time
from src.element import Element, Surface, Polygon
from time import time
from math import sin, cos, pi

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
