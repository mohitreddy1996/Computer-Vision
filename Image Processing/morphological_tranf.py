# changes in the shape of the images
# 2 imputs required : 1) image source 2) kernel

# 1) Erosion : erodes away the foreground object -> recommended to be white.
# the kernel slides through the image , and set the pixel of at time =1 if all the pixels under the kernel are 1. otherwise it will be eroded (0)
# all the pixels near the boundary will be discarded depending upon the size of the kernel.

from cv2 import *
from numpy import *

img=imread('black-white.jpg')

kernel=ones((5,5),uint8)

# for kernel to be of shape of an ellipse : cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# for cross-shaped :- cv2.getStructuringElement(cv2.MORPH_CROSS,(x,y))

res1=erode(img,kernel,iterations=2) # increase iterations or the size of the kernel to erode thicker edges.

# 2) dilation : increases the size of the object. opposite of erosion, pixel=1 if atleast one of the pixel under the kernel is 1.
# dilation is applied after the image is eroded -> removes noises but decreases size , so dilation increases the size. or object joining.
res2=dilate(img,kernel,iterations=2)

# 3) opening : erosion followed by dilation , cv2.morphologyEx() and the parameter as MORPH_OPEN

res3=morphologyEx(img,MORPH_OPEN,kernel)

# 4) closing : dilation followed by erosion , cv2.morphologyEx() and the parameter as MORPH_CLOSE

res4=morphologyEx(img,MORPH_CLOSE,kernel)

# 5) Morphological Gradient : difference between dilation and erosion.

res5=morphologyEx(img,MORPH_GRADIENT,kernel)

# 6) top hat is the difference between imput image and the opening of the image

res6=morphologyEx(img,MORPH_TOPHAT,kernel)

# 7) BLACK hat : difference between the closing of the imput image and the input image

res7=morphologyEx(img,MORPH_BLACKHAT,kernel)

imshow('3',res3)
imshow('4',res4)
imshow('5',res5)
imshow('6',res6)
imshow('7',res7)

imshow('dilated',res2)
imshow('eroded',res1)
imshow('original',img)
waitKey(0)
destroyAllWindows()