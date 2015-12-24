# Smoothing images 1) blur images using low pass filters 2) 2-D convolution
# low pass filters :- for remove noises, blurring images 
# high pass filters :- for edge detection

#2D convolution : custom filtering. cv2.filter2D to convolve a kernel with an image. 
# averaging filter kernel , we can create a matrix : n*n with all entries as 1. and K=[n*n 1]*(1/n*n)
# we keep the kernel on top of a pixel , add all n*n pixels under the kernel , take avergae and replace the central pixel\
from cv2 import *
from numpy import *

img=imread('cr7.jpg')

kernel=ones((5,5),float32)/(25)
dst=filter2D(img,-1,kernel)

imshow('image',img)
imshow('blurred image',dst)
waitKey(0)
destroyAllWindows()