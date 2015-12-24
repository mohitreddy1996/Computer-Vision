
# initially it prints rectangles with changing mouse action.
# if we click 'm' then it changes to making circles
# q for quit


import cv2
import numpy as np 

drawing =False
mode=True
ix=-1
iy=-1

def mouse_action(event,x,y,flags,param):
	global ix,iy,mode,drawing

	if event==cv2.EVENT_LBUTTONDOWN:
		drawing=True
		ix,iy=x,y
	elif event==cv2.EVENT_MOUSEMOVE:
		if drawing==True:
			if mode==True:
				cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
			else:
				cv2.circle(img,(x,y),50,(0,0,255),-1)
	elif event==cv2.EVENT_LBUTTONUP:
		drawing=False
		if mode == True:
			cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
		else:
			cv2.circle(img,(x,y),50,(0,0,255),-1)

img=np.zeros((511,511,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_action)

while(1):
	cv2.imshow('image',img)
	k=cv2.waitKey(20)&0xFF
	if k==ord('m'):
		mode = not mode
	elif k==ord('q'):
		break
cv2.destroyAllWindows()