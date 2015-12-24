# cv2.add : adds the images , pixels : if>=255 it makes the result 255
# numpy add does (x+y)%256 , cv2.add :- recommended

import cv2
import numpy as np 

# image blending : the images are added in different weights to get blending or transparency
# images should be of the same size
# imgres=(alpha*img1) + (beta*img2) + (const)

img1=cv2.imread('cr7.jpg')
img2=cv2.imread('messi.jpg')

ans=cv2.addWeighted(img1,0.8,img2,0.3,0) # image1 , alpha , image2, beta , gamma

cv2.imshow('image',ans)
cv2.waitKey(0)
cv2.destroyAllWindows()

