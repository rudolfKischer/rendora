from ..element import Element
from..transform import Transform
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

from ..utils.vector import reshape_vectors

class Renderlet(Element):
    """
    A renderable element. Anything that can be drawn to the screen.
    This can be a surface, line, mesh, shape, etc.
    Must have a draw function
    Needs to have an opengl drawing mode
    """

    def __init__(self, 
                 points, 
                 colors,
                 RENDER_MODE,
                 point_normals = np.array([]),
                 transform = None
                 ):
        super().__init__(transform=transform)
        self.points = points
        self.colors = colors
        self.point_normals = point_normals
        self.OPENGL_MODE = RENDER_MODE
    
    def get_transformed_points(self):
        points = self.points
        points = reshape_vectors(points, 3, 0.0)
        points = reshape_vectors(points, 4, 1.0)
        points = np.transpose(points)
        transform_matrix = self.get_transform_matrix()
        points = np.matmul(transform_matrix, points)
        points = np.transpose(points)
        points = reshape_vectors(points, 3)
        return points

    def render(self):
        points = self.get_transformed_points()
        colors = self.colors
        colors = reshape_vectors(colors, 3)
        colors_len = colors.shape[0]
        glBegin(self.OPENGL_MODE)
        for i in range(points.shape[0]):
            glColor3fv(colors[i % colors_len])
            glVertex3fv(points[i])
        glEnd()
        
    
class Polygon(Renderlet):
    """
    Represents a polygon.
    """

    def __init__(self, 
              points, 
              colors,
              point_normals = np.array([]),
              transform=None
        ):
        super().__init__(points,
                    colors,
                    GL_POLYGON,
                    point_normals=point_normals,
                    transform=transform
        )

class Circle(Renderlet):
    """
    Represents a circle.
    """

    def __init__(self, 
              radius,
              colors,
              transform = None
        ):
        # generate points
        points = self.generate_points(self.get_num_segments(), radius=radius)
        super().__init__(points,
                      colors,
                      GL_LINE_LOOP,
                      transform = transform
        )
        self.radius = radius
        

    def __str__(self) -> str:
        #output the position of the circle and the radius
        string = "Circle: " + str(self.transform.position) + " " + str(self.radius)
        return string
    
    def generate_points(self, segments, radius):
        """
        Generates the points for the circle.
        segments = number of segments
        """
        points = np.zeros((segments, 3))
        for i in range(segments):
            theta = 2.0 * np.pi * float(i) / float(segments)
            x = radius * np.cos(theta)
            y = radius * np.sin(theta)
            z = 0.0
            # add the point to the points array
            # points should be a 2 dimensional array
            points[i] = np.array([x, y, z])
        return points
    
    def get_num_segments(self): 
        #TODO: use size of circle on screen to determine number of segments
        return 30


        
        
    

        