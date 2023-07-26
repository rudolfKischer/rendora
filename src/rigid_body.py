from src.kinematic import *
from src.transform  import *
from src.collider import *
from src.utils.vector import *
from copy import deepcopy

class Rigid_Body(Element):
        
    def __init__(self,
                 transform = None,
                 kinematic = None,
                 collider = None,
                 ):
        if not transform:
            transform = Transform()
        if not kinematic:
            kinematic = Kinematic()

        super().__init__(transform)
        self.kinematic = kinematic
        self.add_child_element(collider, 'collider')
    
    def update(self, delta_time):
        self.transform.position += self.kinematic.velocity * delta_time
        self.kinematic.velocity += self.kinematic.acceleration * delta_time

        self.parent.transform = deepcopy(self.transform)

    def sphere_collision(self, other_body):
        # return self.collider.sphere_collision(other_body)
        collision_distance = self.collider.radius + other_body.collider.radius
        distance = get_distance(self.parent.transform.position, other_body.transform.position)
        return distance <= collision_distance
    
    def sphere_line_collision(self, line):
        # return self.collider.sphere_line_collision(line)
        collision_distance = self.collider.radius
        position = self.parent.transform.position
        p1 = line.point_1
        p2 = line.point_2
        distance = get_distance_to_line(position, p1, p2)
        error = 0.01
        return distance - error <= collision_distance
    
    def resolve_sphere_line_collision(self, line):
        #get line vector normal
        p_1 = line.point_1
        p_2 = line.point_2
        line_normal = get_2d_line_normal(p_1,p_2)
        vel = self.kinematic.velocity
        reflected_velocity = get_reflected_vec(vel, line_normal)


        # buffer translation
        # prevents oscilattion
        proj = normalize(projection(vel, line_normal))
        buffer = 0.04
        self.transform.position = self.parent.transform.position - (proj * buffer)

        self.kinematic.velocity = reflected_velocity

        
        

    def collision(self, other_body):
        c1 = self.collider
        c2 = other_body.collider
        if isinstance(c1, BoundingSphere) and isinstance(c2, BoundingSphere):
            return self.sphere_collision(other_body)
        
        return False

        
            


        