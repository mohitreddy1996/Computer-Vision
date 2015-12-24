# translations , rotation , affine transformation 

# 1. scaling : resizing the image. cv2.resize()
# the size can be specified manually or scaling factor can be specified.
#interpolation methods are used. 1) cv2.INTER_AREA -> shrinking 2) cv2.INTER_CUBIC 3) cv2.INTER_LINEAR -> zooming (default)

import cv2
import numpy as np 

img=cv2.imread('cr7.jpg')

res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC) #scaling factor


# translation . we create a translation matrix : M={{1,0,delta_x},{0,1,delta_y}}
# make the M matrix into a float32 array and pass it into cv2.warpAffine()

rows,cols=img.shape[:2]

M=np.float32([[1,0,100],[0,1,50]]) # shifts by 100 in x and 50 in y 
dst=cv2.warpAffine(img,M,(cols,rows)) # width = number of columns and height = number of rows

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
