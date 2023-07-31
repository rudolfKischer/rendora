from .element import *
from .physics.rigid_body import *
import src.rendering.renderlet as renderlet

class Entity(Element):
    
    def __init__(self,
                 renderlet,
                 transform = None,
                 kinematic = None,
                 collider = None,
                 ):
        
        super().__init__(
            transform = transform,
        )

        rigid_body = Rigid_Body(kinematic=kinematic, collider=collider)
        self.add_child_element(rigid_body, 'rigid_body')
        self.add_child_element(renderlet, 'renderlet')
    
class Circle(Entity):
    
    def __init__(self, radius, colors):
        super().__init__(
            renderlet.Circle(radius, colors),
            collider = BoundingSphere(radius=radius)            
        )
        self.radius = radius 
    
    def update(self, delta_time):
        self.rigid_body.update(delta_time)
        self.renderlet.render()
    

        
