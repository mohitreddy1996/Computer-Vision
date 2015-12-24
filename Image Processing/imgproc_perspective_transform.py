# we need a 3x3 matrix for the operation. straight lines will remain straight lines
# we need 4 points , 3 of them shouldnt be collinear. 
# the tranformation matrix can be found by cv2.getPerspectiveTransform . apply the matrix into cv2.warpPerspective

import cv2
import numpy as np 

img=cv2.imread('cr7.jpg') 
rows,cols=img.shape[:2]
pts1=np.float32([[50,6] , [218,6] , [50,169] , [218,169]]) # get the four coordinates of the points
pts2=np.float32([[0,20],[165,0],[20,185],[185,165]]) # set the locations where the image should be ploted

M=cv2.getPerspectiveTransform(pts1,pts2)
res=cv2.warpPerspective(img,M,(200,200)) # src, tranform matrix , the size
cv2.imshow('image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()