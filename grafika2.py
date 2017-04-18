#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

import string
__version__ = string.split('$Revision: 1.1.1.1 $')[1]
__date__ = string.join(string.split('$Date: 2007/02/15 19:25:21 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'

#
# Ported to PyOpenGL 2.0 by Tarn Weisner Burton 10May2001
#
# This code was created by Richard Campbell '99 (ported to Python/PyOpenGL by John Ferguson 2000)
#
# The port was based on the PyOpenGL tutorial module: dots.py  
#
# If you've found this code useful, please let me know (email John Ferguson at hakuin@voicenet.com).
#
# See original source and C based tutorial at http://nehe.gamedev.net
#
# Note:
# -----
# This code is not a good example of Python and using OO techniques.  It is a simple and direct
# exposition of how to use the Open GL API in Python via the PyOpenGL package.  It also uses GLUT,
# which in my opinion is a high quality library in that it makes my work simpler.  Due to using
# these APIs, this code is more like a C program using function based programming (which Python
# is in fact based upon, note the use of closures and lambda) than a "good" OO program.
#
# To run this code get and install OpenGL, GLUT, PyOpenGL (see http://www.python.org), and PyNumeric.
# Installing PyNumeric means having a C compiler that is configured properly, or so I found.  For 
# Win32 this assumes VC++, I poked through the setup.py for Numeric, and chased through disutils code
# and noticed what seemed to be hard coded preferences for VC++ in the case of a Win32 OS.  However,
# I am new to Python and know little about disutils, so I may just be not using it right.
#
# BTW, since this is Python make sure you use tabs or spaces to indent, I had numerous problems since I 
# was using editors that were not sensitive to Python.
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small 
	    Height = 1

    glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawCircle(radius, degree, r, g, b,z):

	DEG2RAD = 3.14159/180;
	glBegin(GL_LINE_STRIP) 
	glColor3f(r, g, b) 
	import math
	for i in range(0,degree):
		degInRad = i*DEG2RAD;
		glVertex3f(math.cos(degInRad)*radius,math.sin(degInRad)*radius,z);
	glEnd()

def DrawCirclePart(radius, degree, r, g, b):

	DEG2RAD = 3.14159/180;
	glBegin(GL_LINE_STRIP) 
	glColor3f(r, g, b) 
	import math
	for i in range(0,degree):
		degInRad = i*DEG2RAD;
		glVertex3f(math.cos(degInRad)*radius,math.sin(degInRad)*radius,0.5);
	glEnd()


def DrawSun(radius, degree):
	glBegin(GL_TRIANGLE_FAN) 
	DEG2RAD = 3.14159/180;
	glColor3f(1,0,0);
	glVertex3f(0.0, 0.0,1);

	glColor3f(1.0, 0.7, 0.0) 
	import math
	for i in range(0,degree):
		degInRad = i*DEG2RAD;
		glVertex3f(math.cos(degInRad)*radius,math.sin(degInRad)*radius,1);
	glEnd()

def DrawAwan(radius, degree):
	glBegin(GL_TRIANGLE_FAN) 
	DEG2RAD = 3.14159/180;
	glColor3f(1,1,1);
	glVertex3f(0.0, 0.0,1);

	glColor3f(0.84, 0.98, 1.0) 
	import math
	for i in range(0,degree):
		degInRad = i*DEG2RAD;
		glVertex3f(math.cos(degInRad)*radius,math.sin(degInRad)*radius,1);
	glEnd()

def DrawCircleRing(radius):
	
	DEG2RAD = 3.14159/180;

	glColor3f(1.0, 0.7, 0.0) 
	import math
	for i in range(0,360):
		if (i % 30 == 19):
			glLineWidth(10);	
			glBegin(GL_LINES) 
			degInRad = i*DEG2RAD;

			glVertex3f(math.cos(degInRad)*radius,math.sin(degInRad)*radius,1);
			glVertex3f(math.cos(degInRad)*radius + 0.25*math.cos(degInRad)*(radius+0.1),math.sin(degInRad)*radius+0.25*math.sin(degInRad)*(radius+0.1),1);
			glEnd()


def DrawPelangi():
	r = 1; 
	g = 0; 
	b = 0;
	radius = 0.025
	degree = 130
	
	#Merah ke Kuning
	red = 1
	green = 0	
	for i in xrange(1,20):
		green = float(i) / 20
		DrawCirclePart(1+i*radius,degree,red,green,0);

	#Kuning ke Hijau
	red = 1
	green = 1
	for i in xrange(1,20):
		red = 1 - (float(i) / 20)
		DrawCirclePart(1+(19+i)*radius,degree,red,green,0);

	#Hijau ke Biru
	blue = 0
	green = 1
	for i in xrange(1,20):
		green = 1 - (float(i) / 20)
		blue = (float(i) / 20)
		DrawCirclePart(1+(38+i)*radius,degree,0,green,blue);

# The main drawing function. 
def DrawGLScene():
	# Clear The Screen And The Depth Buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()					# Reset The View 

	# Move Left 1.5 units and into the screen 6.0 units.
	glTranslatef(-1.5, 0.5, -6.0)
	# DrawPelangi(1,1,5,5)

	
	glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
	glColor3f(1, 0.7, 0.50)            # Bluish shade
	glVertex3f(-10.0, 4.0, 0.0)          # Top Left
	glVertex3f(8.0, 4.0, 0.0)           # Top Right
	glColor3f(0.3, 0.9, 1.0)            # Bluish shade
	glVertex3f(8.0, -4.0, 0.0)          # Bottom Right
	glVertex3f(-7.0, -4.0, 0.0)         # Bottom Left
	glEnd()

	#Matahari
	glTranslatef(2.5, 1.3, 0)


	glTranslatef(-2.5, -2.3, 0)
	# gambar pohon
	glColor3f(0.82,0.41,0.11)            # Bluish shade
	glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
	glVertex3f(4.0, -1.0, 0.725)          # Top Left
	glVertex3f(3.8, -1.0, 0.725)           # Top Right
	glVertex3f(3.8, -2.4, 0.725)          # Bottom Right
	glVertex3f(4.0, -2.4, 0.725)         # Bottom Left
	glEnd()

	# gambar daun - daun
	glBegin(GL_POLYGON)                 # Start drawing a polygon
	glColor3f(0.0, 0.5, 0.0)            # green
	glVertex3f(3.85, 0.0, 0.75)           # Top
	glColor3f(0.0, 0.0, 0.0)            # Green
	glVertex3f(4.25, -1.5, 0.75)          # Bottom Right
	glColor3f(0.0, 0.0, 0.0)            # green
	glVertex3f(3.45, -1.5, 0.75)         # Bottom Left
	glEnd()                             # We are done with the polygon

	# gambar daun - daun
	glBegin(GL_POLYGON)                 # Start drawing a polygon
	glColor3f(0.0, 0.5, 0.0)            # green
	glVertex3f(3.85, 0.5, 0.85)           # Top
	glColor3f(0.0, 0.5, 0.0)            # Green
	glVertex3f(4.25, -1.0, 0.85)          # Bottom Right
	glColor3f(0.0, 0.0, 0.0)            # green
	glVertex3f(3.45, -1.0, 0.85)         # Bottom Left
	glEnd()                             # We are done with the polygon

	glTranslatef(0.5, 1.8, 0)
	# gambar gunung segitiga kiri
	glBegin(GL_POLYGON)                 # Start drawing a polygon
	glColor3f(0.0, 1.0, 0.0)            # green
	glVertex3f(0.0, -1.0, 0.6)           # Top
	glColor3f(0.0, 0.0, 0.0)            # Green
	glVertex3f(2.8, -3.7, 0.6)          # Bottom Right
	glColor3f(0.0, 0.0, 0.0)            # green
	glVertex3f(-2.8, -3.7, 0.6)         # Bottom Left
	glEnd()                             # We are done with the polygon

	# gambar gunung segitiga kanan
	glBegin(GL_POLYGON)                 # Start drawing a polygon
	glColor3f(0.0, 1.0, 0.0)            # green
	glVertex3f(3.0, -1.0, 0.7)           # Top
	glColor3f(0.0, 0.0, 0.0)            # Green
	glVertex3f(4.8, -3.7, 0.7)          # Bottom Right
	glColor3f(0.0, 0.0, 0.0)            # green
	glVertex3f(0.2, -3.7, 0.7)         # Bottom Left
	glEnd()                             # We are done with the polygon


	glTranslatef(-0.7,0,0) # mataharinya gw geser dikit yak

	glTranslatef(1.5, 0.5, 0)
	DrawSun(0.4,361)
	DrawCircleRing(0.5)

	glTranslatef(0.7,0,0) # mataharinya gw geser dikit yak


	############################################################################################################
	# gambar awan!!!
	# kode Dyas, maap chaos, blom terlalu ngerti

	# awan 1

	xAwan1 = 1.6
	yAwan1 = -0.25
	zAwan1 = 0
	ukuran = 0.3

	# buletan
	geserX = xAwan1
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*7/4
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran*0.75,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*9.5/4
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran/2,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran/2
	geserY = yAwan1 + ukuran*1.5/4
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran/2
	geserY = yAwan1 - ukuran*1.5/4
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*5/4
	geserY = yAwan1 + ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*5/4
	geserY = yAwan1 - ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 - ukuran/2
	geserY = yAwan1 + ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 - ukuran/2
	geserY = yAwan1 - ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya


	# awan 2

	xAwan1 = 0.3
	yAwan1 = -1.2
	zAwan1 = 0
	ukuran = 0.25

	# buletan
	geserX = xAwan1
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*7/4
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran*0.75,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*9.5/4
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran/2,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran/2
	geserY = yAwan1 + ukuran*1.5/4
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran/2
	geserY = yAwan1 - ukuran*1.5/4
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*5/4
	geserY = yAwan1 + ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*5/4
	geserY = yAwan1 - ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 - ukuran/2
	geserY = yAwan1 + ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 - ukuran/2
	geserY = yAwan1 - ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# awan 3

	xAwan1 = 1.9
	yAwan1 = -1.3
	zAwan1 = 0
	ukuran = 0.2

	# buletan
	geserX = xAwan1
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*7/4
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran*0.75,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*9.5/4
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran/2,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran/2
	geserY = yAwan1 + ukuran*1.5/4
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran/2
	geserY = yAwan1 - ukuran*1.5/4
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*5/4
	geserY = yAwan1 + ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*5/4
	geserY = yAwan1 - ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 - ukuran/2
	geserY = yAwan1 + ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 - ukuran/2
	geserY = yAwan1 - ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# awan 4

	xAwan1 = 0.6
	yAwan1 = -0.55
	zAwan1 = 0
	ukuran = 0.15

	# buletan
	geserX = xAwan1
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*7/4
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran*0.75,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*9.5/4
	geserY = yAwan1
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran/2,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran/2
	geserY = yAwan1 + ukuran*1.5/4
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran/2
	geserY = yAwan1 - ukuran*1.5/4
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*5/4
	geserY = yAwan1 + ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 + ukuran*5/4
	geserY = yAwan1 - ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 - ukuran/2
	geserY = yAwan1 + ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya

	# buletan
	geserX = xAwan1 - ukuran/2
	geserY = yAwan1 - ukuran/8
	geserZ = zAwan1

	glTranslatef(geserX, geserY, geserZ)
	DrawAwan(ukuran,361)
	glTranslatef(-geserX, -geserY, geserZ) # balikin lagi biar ga ngefek ke bawah2nya




	# gambar awan beres
	############################################################################################################

	glTranslatef(-3.3, -2.5, 0)
	DrawPelangi()

	glTranslatef(-1, 0.2, 0)
	# gambar pohon
	glColor3f(0.82,0.41,0.11)            # Bluish shade
	glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
	glVertex3f(4.0, -1.0, 0.725)          # Top Left
	glVertex3f(3.8, -1.0, 0.725)           # Top Right
	glVertex3f(3.8, -2.4, 0.725)          # Bottom Right
	glVertex3f(4.0, -2.4, 0.725)         # Bottom Left
	glEnd()

	# gambar daun - daun
	glBegin(GL_POLYGON)                 # Start drawing a polygon
	glColor3f(0.0, 0.5, 0.0)            # green
	glVertex3f(3.85, 0.0, 0.75)           # Top
	glColor3f(0.0, 0.0, 0.0)            # Green
	glVertex3f(4.25, -1.5, 0.75)          # Bottom Right
	glColor3f(0.0, 0.0, 0.0)            # green
	glVertex3f(3.45, -1.5, 0.75)         # Bottom Left
	glEnd()                             # We are done with the polygon

	# gambar daun - daun
	glBegin(GL_POLYGON)                 # Start drawing a polygon
	glColor3f(0.0, 0.5, 0.0)            # green
	glVertex3f(3.85, 0.5, 0.85)           # Top
	glColor3f(0.0, 0.5, 0.0)            # Green
	glVertex3f(4.25, -1.0, 0.85)          # Bottom Right
	glColor3f(0.0, 0.0, 0.0)            # green
	glVertex3f(3.45, -1.0, 0.85)         # Bottom Left
	glEnd()                             # We are done with the polygon

	glTranslatef(-2, 0, 0)
	# gambar pohon
	glColor3f(0.82,0.41,0.11)            # Bluish shade
	glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
	glVertex3f(4.0, -1.0, 0.725)          # Top Left
	glVertex3f(3.8, -1.0, 0.725)           # Top Right
	glVertex3f(3.8, -2.4, 0.725)          # Bottom Right
	glVertex3f(4.0, -2.4, 0.725)         # Bottom Left
	glEnd()

	# gambar daun - daun
	glBegin(GL_POLYGON)                 # Start drawing a polygon
	glColor3f(0.0, 0.5, 0.0)            # green
	glVertex3f(3.85, 0.0, 0.75)           # Top
	glColor3f(0.0, 0.0, 0.0)            # Green
	glVertex3f(4.25, -1.5, 0.75)          # Bottom Right
	glColor3f(0.0, 0.0, 0.0)            # green
	glVertex3f(3.45, -1.5, 0.75)         # Bottom Left
	glEnd()                             # We are done with the polygon

	# gambar daun - daun
	glBegin(GL_POLYGON)                 # Start drawing a polygon
	glColor3f(0.0, 0.5, 0.0)            # green
	glVertex3f(3.85, 0.5, 0.85)           # Top
	glColor3f(0.0, 0.5, 0.0)            # Green
	glVertex3f(4.25, -1.0, 0.85)          # Bottom Right
	glColor3f(0.0, 0.0, 0.0)            # green
	glVertex3f(3.45, -1.0, 0.85)         # Bottom Left
	glEnd()                             # We are done with the polygon


	# Since we have smooth color mode on, this will be great for the Phish Heads :-).
	# Draw a triangle
	

	#  since this is double buffered, swap the buffers to display what just got drawn. 
	glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	# If escape is pressed, kill everything.
    if args[0] == ESCAPE:
	    sys.exit()

def main():
	global window
	# For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
	# Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
	glutInit(sys.argv)

	# Select type of Display mode:   
	#  Double buffer 
	#  RGBA color
	# Alpha components supported 
	# Depth buffer
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	
	# get a 640 x 480 window 
	glutInitWindowSize(900, 600)
	
	# the window starts at the upper left corner of the screen 
	glutInitWindowPosition(0, 0)
	
	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
	window = glutCreateWindow("Tugas Grafika Huahaha")

   	# Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
	# set the function pointer and invoke a function to actually register the callback, otherwise it
	# would be very much like the C version of the code.	
	glutDisplayFunc(DrawGLScene)
	
	# Uncomment this line to get full screen.
	#glutFullScreen()

	# When we are doing nothing, redraw the scene.
	glutIdleFunc(DrawGLScene)
	
	# Register the function called when our window is resized.
	glutReshapeFunc(ReSizeGLScene)
	
	# Register the function called when the keyboard is pressed.  
	glutKeyboardFunc(keyPressed)

	# Initialize our window. 
	InitGL(900, 600)

	# Start Event Processing Engine	
	glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print "Hit ESC key to quit."
main()
    	
