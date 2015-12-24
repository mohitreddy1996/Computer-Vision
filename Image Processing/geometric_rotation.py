# opencv allows rotation with scaling at any centre by any degrees.
# the matrix M : [[alpha,beta,(1-alpha)*centre_x - beta*centre_y],[-beta,alpha,beta*centre_x + (1-alpha)*centre_y]]
# alpha = scale*cos(theta) and beta=scale*sin(theta)

import cv2
import numpy as np 

img=cv2.imread('cr7.jpg')

rows,cols=img.shape[:2]

M=cv2.getRotationMatrix2D((cols/2,rows/2),90,1) # cv2.getRotationMatrix2D((x,y),degree of rotation, scaling factor )

res=cv2.warpAffine(img,M,(cols,rows))

# affine transformation : all parallel lines in the original image will still be parallel in the output image.
# to form affine Matrix we need 3 points from input and corresponding points from the output.
# getAffineTransform will give 2x3 matrix passed as argument to cv2.warpAffine(img,M,(cols,rows))


cv2.imshow('image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()