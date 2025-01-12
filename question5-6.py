
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1)
    
    )

edges = (
    (0,1),
    (0,2),
    (1,2)
   
    )
surface = (
    (0,1,2)
)


def Cube():
    glBegin(GL_LINES)
    for vertex in surface:
    
            glColor3fv((1,0,0))
    for edge in edges:
        
        for vertex in edge:
            glVertex3fv(verticies[vertex])
        

    glEnd()
def lines(x1,x2,x3,x4):
     return

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0,0, -5)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
