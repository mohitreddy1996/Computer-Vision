# cv2.VideoCapture :- to get the live streaming. cv2.VideoWriter :- to save the video as well
# we capture frame by frame and then display it.


import cv2

cap=cv2.VideoCapture(0) # camera object. the index passed into VideoCapture is to mention which camera is being used.
while True:
	ret,frame=cap.read() # ret is true if the frame is read correctly.
	#gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert the read frame into a grayscale image, display it.
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break;
cap.release() # release the captured object. <- Important.
cv2.destroyAllWindows()
