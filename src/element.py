import numpy as np

from src.utils.matrix import get_model_matrix
from src.transform import Transform
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import config 
from copy import deepcopy


class Element(object):
    """
    The most general representation of something that can persist in a scene.
    These are things like models, lights, cameras, etc.
    They have a position, an orientation, and a scale.
    They can be composed of other elements.
    """
  

    def __init__(self, transform=None):
        if transform is None:
            transform = Transform()
        self.children = {}
        self.transform = transform
        self.parent = None
    
    def __getattr__(self, name):
        if 'children' in self.__dict__.keys():
            if name in self.children.keys():
                return self.children[name]
        return self.__dict__[name]
    
    def __setattr__(self, name, value):
        if 'children' in self.__dict__.keys():
            if name in self.children.keys():
                self.children[name] = value
                return
        self.__dict__[name] = value
        return 

    def get_transform(self):
        """
        Returns a copy of transform after applying the parents transform
        """
        copy_transform = deepcopy(self.transform)
        if self.parent:
            copy_transform.transform(self.parent.get_transform())
        return copy_transform

    def get_transform_matrix(self):
        """
        Returns the transform matrix after applying the parent's transform matrix.
        """
        if self.parent is None:
            return self.transform.get_transform_matrix()
        else:
            return np.matmul(self.parent.get_transform_matrix(), self.transform.get_transform_matrix())
    
    def get_new_born_name(self):
        children = self.children.keys()
        num_of_children = len(children)
        new_born_number = num_of_children
        while(True):
            new_born_number += 1
            new_born_name = f'_{new_born_number}'
            if new_born_name in children:
                continue
            return new_born_name

    def add_child_element(self, new_child, name=None):
        children_names = self.children.keys()
        if name in children_names:
            raise KeyError(name)
        if not name:
            name = self.get_new_born_name()
        self.children[name] = new_child
        new_child.parent = self
    
    def update(self):
        for child in self.children:
            child.update()
        
            

        

    def __str__(self) -> str:
        return "Element: " + str(self.transform)



        
    


    

            

    


    
    
    

    