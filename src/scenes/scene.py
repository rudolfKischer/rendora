from src.element import Element
from time import time

DEFAULT_PERSPECTIVE_SETTINGS = { 
    "PROJECTION_MODE": False,
    "PERSPECTIVE_FOV": 45.0,
    "PERSPECTIVE_NEAR_CLIP": 0.1,
    "PERSPECTIVE_FAR_CLIP": 100.0,
    "PERSPECTIVE_DEFAULT_CAMERA_POSITION": (0.0, 0.0, 0.0),
    "PERSPECTIVE_DEFAULT_CAMERA_LOOK_AT_DIRECTION": (0.0, 0.0, -1.0)
}
class Scene(Element):
    
    def __init__(self, setup_f=None, update_f=None):
        super().__init__()
        if setup_f:
            self.setup = setup_f
        if update_f:
          self.update = update_f
        self.prev_time = time()

        for setting, value in DEFAULT_PERSPECTIVE_SETTINGS.items():
            self.__dict__[setting] = DEFAULT_PERSPECTIVE_SETTINGS[setting]
    
    def _update(self):
        current_time = time()
        delta_time = current_time - self.prev_time
        self.prev_time = current_time
        self.update(delta_time)
    

    