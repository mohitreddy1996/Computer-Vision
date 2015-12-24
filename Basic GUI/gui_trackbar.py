#trackbars are set for RGB and a switch. if the switch is off the values are at 0,0,0 else 
# the values dynamically set using the trackbar

from cv2 import *
from numpy import *

def nothing(x):
	pass

img=zeros((512,512,3),uint8)
namedWindow('image')

createTrackbar('R','image',0,255,nothing)
createTrackbar('G','image',0,255,nothing)
createTrackbar('B','image',0,255,nothing)

switch='0 : OFF\n1: ON'

createTrackbar(switch,'image',0,1,nothing)

while(1):
	imshow('image',img)
	k=waitKey(1) & 0xFF

	if k==ord('q'):
		break

	b=getTrackbarPos('R','image')
	g=getTrackbarPos('G','image')
	r=getTrackbarPos('B','image')
	s=getTrackbarPos(switch,'image')
	if s==0:
		img[:]=0
	else:
		img[:]=[b,g,r]

destroyAllWindows()