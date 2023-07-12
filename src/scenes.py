from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from src.draw import square, triangle
import numpy as np
import time

def default_scene():
    # square([(-0.5, 0.5), (0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)]) # white square

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
