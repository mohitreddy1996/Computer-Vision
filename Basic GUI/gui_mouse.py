# actions based on the operation by mouse.
# the way of calling the mouse rollback function is the same.

import cv2
import numpy as np

def draw_circle(event,x,y,flags,param): #event is the action we do using mouse. x,y are the location where we click the mouse. flags and param are default
	if event==cv2.EVENT_LBUTTONDBLCLK: 
		cv2.circle(img,(x,y),60,(255,0,0),-1)

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image') # the window will be shown 
cv2.setMouseCallback('image',draw_circle) # the parameters are the name of the window and the function responsible for the actions

while(1):
	cv2.imshow('image',img)
	if cv2.waitKey(20) & 0xFF==ord('q'):
		break
cv2.destroyAllWindows()