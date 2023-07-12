from src.utils.matrix import get_model_matrix
import numpy as np

class Transform(object):
    """
    Represents a transformation space.
    Holds a position, an orientation, and a scale.
    """

    def __init__(self, 
                 position = np.zeros(3),
                 orientation = np.zeros(3),
                 scale = np.ones(3)
                 ):
        self._properties = {
            "position": position,
            "orientation": orientation,
            "scale": scale,
            "transform_matrix": get_model_matrix(position, orientation, scale),
        }
        self.update_flag = True
    
    def __getattr__(self, name):
        return self._properties[name]

    def __setattr__(self, name, value):
        if name == "_properties":
            self.__dict__[name] = value
        if name == "update_flag":
            self.__dict__[name] = value
        else:
            self._properties[name] = value
            self.update_flag = True

    def update_transform_matrix(self):
        """
        Updates the transform matrix for this element.
        """
        self.transform_matrix = get_model_matrix(self.position, self.orientation, self.scale)
        self.update_flag = False
    
    def get_transform_matrix(self):
        """
        Returns the transform matrix for this element.
        """
        # if the position, scale, or orientation have changed, update the transform matrix
        if self.update_flag:
            self.update_transform_matrix()
        return self.transform_matrix
    
    def transform(self, transform):
        """
        given a transform, manipulates the position, orientation, and scale of this transform.
        """
        self.position = self.position + transform.position
        self.orientation = self.orientation + transform.orientation
        self.scale = self.scale + transform.scale
        self.update_flag = True