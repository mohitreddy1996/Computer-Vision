
from cv2 import *

from numpy import *


cap=VideoCapture(0)
while True:
	ret,frame=cap.read()
	gray=cvtColor(frame,COLOR_BGR2GRAY)
	edges=Canny(gray,50,150)
	height,width=gray.shape[:2]
	lines=HoughLines(edges,1,pi/360,150) # binary img with lines, accuracy for p , accuracy for theta , threshold for votes
	img2=zeros((height,width,3),uint8)
	try:
		for rho,theta in lines[0]:
			a=cos(theta)
			b=sin(theta)
			x0=a*rho
			y0=b*rho
			x1=int(x0+1000*(-b))
			y1=int(y0+1000*a)
			x2=int(x0-1000*(-b))
			y2=int(y0-1000*a)
			line(img2,(x1,y1),(x2,y2),(255,255,255),1) #img src,starting point,ending point,color of the line,thickness
			imshow('img',img2)
			imshow('img2',frame)
			if waitKey(1) & 0xFF==ord('q'):
				break
	except:
		imshow('img',img2)
		imshow('img2',frame)
		if waitKey(1) & 0xFF==ord('q'):
				break
	