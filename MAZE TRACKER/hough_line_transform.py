''' we take a point on a line. we get the line equation putting theta=0,1,..180. get the value of p.
increment for every (p,theta) pair value.
put a threshold value for the votes. if the value is greater than threshold
line exists. '''

from cv2 import *
from numpy import *

img=imread('sudoko.png')
gray=cvtColor(img,COLOR_BGR2GRAY)
edges=Canny(gray,50,150,apertureSize=3)

lines=HoughLines(edges,1,pi/180,200) # binary img with lines, accuracy for p , accuracy for theta , threshold for votes
#imshow('edges',edges)
#waitKey(0)
#print lines
for rho,theta in lines[0]:
	a=cos(theta)
	b=sin(theta)
	x0=a*rho
	y0=b*rho
	x1=int(x0+1000*(-b))
	y1=int(y0+1000*a)
	x2=int(x0-1000*(-b))
	y2=int(y0-1000*a)

	line(img,(x1,y1),(x2,y2),(0,0,255),2) #img src,starting point,ending point,color of the line,thickness

imshow('img',img)
waitKey(0)


'''probabilistic Hough Transform
takes only a random subset of the points to detect lines.
arguments : 1. minLineLength : minimum length of the line. Line segments less than this are rejected.
2. maxLineGap : maximum allowed gap between line segments to treat them as a single line.
'''
minLineLength=100
maxLineGap=10
lines=HoughLinesP(edges,1,pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
	line(img,(x1,y1),(x2,y2),(0,255,0),2)

imshow('img2',img)
waitKey(0)