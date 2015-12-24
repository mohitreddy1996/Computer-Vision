# to save the video being recorded using VideoWriter 

# to get the codec : VideoWriter_fourcc(*'XVID') or ('X','V','I','D')
# the VideoWriter object and we write each frame into it.
# VideoWriter(filename,codec_variable,frames per second,(w,h) <- dimensions)

import cv2

cap=cv2.VideoCapture(0)

#codec
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out=cv2.VideoWriter('Output.avi',fourcc,20.0,(640,480))

while cap.isOpened() :
	ret,frame=cap.read()
	if ret==True:
		#frame=cv2.flip(frame,0) # flip the frame read
		out.write(frame)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF==ord('q'):
			break
	else :
		break
cap.release()
out.release()
cv2.destroyAllWindows()