import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
	(0,-1,0.8),
	(0,1,0.8),
	(-1,1,0.8),
	(-1,-1,0.8),
	(0,-1,1),
	(0,1,1),
	(-1,-1,1),
	(-1,1,1)
	)

edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7)
	)

surfaces = (
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6)
	)

colors = (
	(0,0,1),
	(0,0,1),
	(0,0,0),
	(0,0,1),
	(0,0,1),
	(0,0,1),
	)

def drawCube():
	glBegin(GL_QUADS)
	x = -1
	for surface in surfaces:
		x+=1
		for vertex in surface:
			glColor3fv(colors[x])
			glVertex3fv(verticies[vertex])	
	glEnd()

	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(verticies[vertex])
	glEnd()

pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
gluPerspective(45,(display[0]/display[1]), 0.1 ,50.0)
glTranslatef(0.0,0.0,-5)
glRotatef(0,0,0,0)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	glRotatef(1,3,1,1)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	drawCube();
	pygame.display.flip()
	pygame.time.wait(10)
