import numpy as np

class Kinematic():
    
    def __init__(self,
                 velocity=np.zeros(3),
                 angular_velocity=np.zeros(3),
                 acceleration=np.zeros(3),
                 ):
        self.velocity = velocity
        self.angular_velocity = angular_velocity
        self.acceleration = acceleration

    