from src.element import *
import numpy as np
from .utils.vector import *

class Collider(Element):
    
    def __init__(self, transform=None):
        super().__init__(transform=transform)

class LineSegmentCollider(Collider):
    
    def __init__(self, point_1, point_2, transform=None):
        super().__init__(transform)
        self.point_1 = point_1
        self.point_2 = point_2
    

    


class BoundingBox(Collider):
    
    def __init__(self,
                 corner_1= (np.ones(3) * -1),
                 corner_2= np.ones(3)
                 ):
        self.corner_1 = corner_1
        self.corner_2 = corner_2


class BoundingSurface(Collider):
    
    def __init__(self):
        pass

class BoundingSphere(Collider):
    
    def __init__(self, radius=1.0, transform=None):
        super().__init__(transform=transform)
        self.radius = radius

    # def sphere_collision(self, other_body):
    #     collision_distance = self.radius + other_body.collider.radius
    #     distance = get_distance(self.get_transform().position, other_body.transform.position)
    #     return distance <= collision_distance
    
    # def sphere_line_collision(self, line):
    #     collision_distance = self.radius
    #     position = self.get_transform().position
    #     p1 = line.point_1
    #     p2 = line.point_2
    #     distance = get_distance_to_line(position, p1, p2)
    #     error = 0.01
    #     return distance - error <= collision_distance
