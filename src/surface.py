from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from src.element import *

class Surface(Element):

    def __init__(self, points, colors, point_normals = np.array([])):
        super().__init__()
        self.points = points
        self.colors = colors
        self.point_normals = point_normals

class Polygon(Surface):
    """
    Represents a polygon.
    """
    OPENGL_MODE = GL_POLYGON

class Circle(Surface):
    """
    Represents a circle.
    """
    OPENGL_MODE = GL_LINE_LOOP

    def __str__(self) -> str:
        #output the position of the circle and the radius
        string = "Circle: " + str(self.transform.position) + " " + str(self.radius)
        return string
    
    def generate_points(self, segments):
        """
        Generates the points for the circle.
        segments = number of segments
        """
        center = self.transform.position
        points = np.zeros((segments, 3))
        for i in range(segments):
            theta = 2.0 * np.pi * float(i) / float(segments)
            x = self.radius * np.cos(theta) + center[0]
            y = self.radius * np.sin(theta) + center[1]
            z = center[2]
            # add the point to the points array
            # points should be a 2 dimensional array
            points[i] = np.array([x, y, z])
        self.points = points
    
    def get_num_segments(self): 
        #TODO: use size of circle on screen to determine number of segments
        return 30

    def __init__(self, radius, colors):
        # generate points
        self.radius = radius
        self.colors = colors

        super().__init__([], self.colors)
        self.generate_points(self.get_num_segments())