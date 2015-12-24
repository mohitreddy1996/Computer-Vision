# to read from a video file present in the disk.
#waitKey parameter can be changed to play the video in slow motion.

import cv2

cap=cv2.VideoCapture('video1.avi')

while(cap.isOpened()):
	ret,frame=cap.read()
	cv2.imshow('Pokemon',frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()