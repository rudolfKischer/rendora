from .scene import *
import numpy as np
from src.utils.vector import normalize, extend_vectors
from src.entities import Circle
from src.collider import LineSegmentCollider
from src.utils.random import *
from src.scenes.setup_functions import create_borders

from OpenGL.GLUT import *
from OpenGL.GLU import *
from src.draw import square, triangle, surface
from ..surface import Surface, Polygon
from ..entities import Circle
from ..collider import LineSegmentCollider
import numpy as np
import time
from src.element import Element
from time import time
from math import sin, cos, pi
from ..utils.vector import *

class CircleTest(Scene):
    
    def __init__(self, num_circles = 10, circle_speed = 2.5):
        super().__init__()
        self.num_circles = num_circles
        self.speed = circle_speed
    
        
    def generate_circle(self):
        #generate a circle with a random color and a random size
        rand_val = rand()
        radius = rand_val * 0.05 + 0.05
        circle = Circle(radius = radius , colors = [[(rand_val),(0.0),(1-rand_val)]])

        #generate a random velocity
        direction = normalize(extend_vectors(np.array([rand_vec(2, include_negative=True)]), 3, 0.0)[0])
        circle.rigid_body.kinematic.velocity = direction * self.speed
        return circle

    def setup(self):
        full_border = create_borders()
        self.add_child_element(full_border, "border")

        circles = Element()
        for i in range(self.num_circles):
            circle = self.generate_circle()
            circles.add_child_element(circle)
        
        self.add_child_element(circles, "circles")
    
    def update(self, delta_time):
        
        circles = self.children["circles"].children.values()
        borders = self.children["border"].children.values()

        for circle in circles:
            for border in borders:
                if circle.rigid_body.sphere_line_collision(border):
                    circle.rigid_body.resolve_sphere_line_collision(border)

            # circle.rigid_body.kinematic.velocity[1] -= 1.8 * delta_time
            circle.update(delta_time)
        
        for circle_1 in circles:
            for circle_2 in circles:
                if circle_1 == circle_2:
                    continue
                if circle_1.rigid_body.sphere_collision(circle_2.rigid_body):
                    circle_1.rigid_body.resolve_sphere_collision(circle_2.rigid_body)

class PolygonTest(Scene):
    
    def __init__(self):
        super().__init__()
    
    def setup(self):
        pass
    
    def update(self, delta_time):
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

class DefaultScene(Scene):
    
    def __init__(self):
        super().__init__()
    
    def setup(self):
        pass
    
    def update(self, delta_time):
        #traw a color interpolated square, red, green, blue, yellow
        square_points = [(-0.5, 0.5), (0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)]
        square_colors = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0, 0, 1), (1, 1, 0)]

        #rotate the points based on the time

        square_points = np.array(square_points)
        square_points = np.transpose(square_points)
        # use the fractional part of the time to rotate the square
        time_fraction = ((time() * 0.1) % 1) * 2 * np.pi
        rotation_matrix = np.array([[np.cos(time_fraction), -np.sin(time_fraction)], [np.sin(time_fraction), np.cos(time_fraction)]])
        square_points = np.matmul(rotation_matrix, square_points)
        square_points = np.transpose(square_points)

        square(square_points,
                  square_colors)