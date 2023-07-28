from src.element import Element
from time import time

class Scene(Element):
    
    def __init__(self, setup_f=None, update_f=None):
        super().__init__()
        if setup_f:
            self.setup = setup_f
        if update_f:
          self.update = update_f
        self.prev_time = time()
    
    def _update(self):
        current_time = time()
        delta_time = current_time - self.prev_time
        self.prev_time = current_time
        self.update(delta_time)
    

    