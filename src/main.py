#OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#local
from config import *

def iterate():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    SCENE_FUNCTION()
    glutSwapBuffers()

def initialize():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(*WINDOW_POSITION)

def main():
    initialize()
    wind = glutCreateWindow(WINDOW_CAPTION)
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutMainLoop()