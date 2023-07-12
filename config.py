from src import scenes

# WINDOW SETTINGS
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_CAPTION = "OpenGL Coding Practice"
WINDOW_POSITION = (0, 0)

#SCENE SETTINGS
# SCENE_FUNCTION = scenes.default_scene
SCENE_FUNCTION = scenes.polygon_test

# VIEW SETTINGS
# PROJECTION_MODE = "ORTHOGRAPHIC"

PROJECTION_MODE = True
PERSPECTIVE_FOV = 45.0
PERSPECTIVE_NEAR_CLIP = 0.1
PERSPECTIVE_FAR_CLIP = 100.0
PERSPECTIVE_DEFAULT_CAMERA_POSITION = (0.0, 0.0, 0.0)
PERSPECTIVE_DEFAULT_CAMERA_LOOK_AT_DIRECTION = (0.0, 0.0, -1.0)

