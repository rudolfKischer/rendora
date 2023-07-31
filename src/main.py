#OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#local
from config import *
import numpy as np

def projection_mode():
    aspect_ratio = float(WINDOW_WIDTH) / float(WINDOW_HEIGHT)
    gluPerspective(SCENE.PERSPECTIVE_FOV, 
                  aspect_ratio, 
                  SCENE.PERSPECTIVE_NEAR_CLIP, 
                  SCENE.PERSPECTIVE_FAR_CLIP)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    camera_position = SCENE.PERSPECTIVE_DEFAULT_CAMERA_POSITION
    up_vector = (0.0, 1.0, 0.0)
    look_at_vector = SCENE.PERSPECTIVE_DEFAULT_CAMERA_LOOK_AT_DIRECTION
    gluLookAt(*camera_position, *look_at_vector, *up_vector)
    glTranslatef(*camera_position)
    

def iterate():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if SCENE.PROJECTION_MODE:
        projection_mode()
    else:
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)


    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    SCENE._update()
    glutSwapBuffers()

def initialize():
    #setup openGL
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(*WINDOW_POSITION)

    #setup Scene
    SCENE.setup()


def main():
    initialize()
    wind = glutCreateWindow(WINDOW_CAPTION)
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutMainLoop()