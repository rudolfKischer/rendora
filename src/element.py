import numpy as np

from src.utils.matrix import get_model_matrix
from src.transform import Transform
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Element(object):
    """
    The most general representation of something that can persist in a scene.
    These are things like models, lights, cameras, etc.
    They have a position, an orientation, and a scale.
    They can be composed of other elements.
    """
    
    transform = Transform() # position, orientation, and scale of an object
    parent = None
    children = []


class Surface(Element):
    points = np.array([])
    colors = np.array([])
    point_normals = np.array([])

    def __init__(self, points, colors, point_normals = np.array([])):
        self.points = points
        self.colors = colors
        self.point_normals = point_normals

class Polygon(Surface):
    """
    Represents a polygon.
    """
    OPENGL_MODE = GL_POLYGON
    


    

            

    


    
    
    

    