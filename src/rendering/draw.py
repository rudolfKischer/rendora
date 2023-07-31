from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

from src.utils.vector import reshape_vectors

def square(points, colors = [(1.0, 1.0, 1.0)]):
    points = reshape_vectors(points, 3)
    colors = reshape_vectors(colors, 3)
    colors_len = colors.shape[0]
    glBegin(GL_QUADS)
    for i in range(4):
        glColor3fv(colors[i % colors_len])
        glVertex3fv(points[i])
    glEnd()

def triangle(points, colors):
    points = reshape_vectors(points, 3)
    colors = reshape_vectors(colors, 3)
    colors_len = colors.shape[0]
    glBegin(GL_TRIANGLES)
    for i in range(3):
        glColor3fv(colors[i % colors_len])
        glVertex3fv(points[i])
    glEnd()

def surface(surface):
    points = surface.points
    points = reshape_vectors(points, 3, 0.0)
    points = reshape_vectors(points, 4, 1.0)
    points = np.transpose(points)
    transform_matrix = surface.transform.get_transform_matrix()
    points = np.matmul(transform_matrix, points)
    points = np.transpose(points)

    points = reshape_vectors(points, 3)

    colors = surface.colors
    colors = reshape_vectors(colors, 3)
    colors_len = colors.shape[0]

    glBegin(surface.OPENGL_MODE)
    for i in range(points.shape[0]):
        glColor3fv(colors[i % colors_len])
        glVertex3fv(points[i])
    glEnd()