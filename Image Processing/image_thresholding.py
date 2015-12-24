# thresholding : if the value of the pixel is greater than threshold value it is assigned to a specific value
# cv2.threshold -> inputs : grayscale image : checks the itensity , threshold value , max value , flag : cv2.THRESH_BINARY etc.

# adaptive threshold : the algorithm calculates threshold for smaller region of images.
# 1) cv2.threshold , 2) cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of the neighbourhood ADAPTIVE_THRESH_MEAN_C
# 3) cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted mean of the neighbouring area.
# parameter : block size , C <- value to be subtracted from the mean/weighted mean
from cv2 import *
from numpy import *

img=imread('sudoko.jpg')
imshow('image',img)
#img=medianBlur(img,5)
img=cvtColor(img,COLOR_BGR2GRAY)
ret,frame1=threshold(img,127,255,THRESH_BINARY)
frame2=adaptiveThreshold(img,255,ADAPTIVE_THRESH_MEAN_C,THRESH_BINARY,11,2)
frame3=adaptiveThreshold(img,255,ADAPTIVE_THRESH_GAUSSIAN_C,THRESH_BINARY,11,2)

imshow('frame1',frame1)
imshow('frame2',frame2)
imshow('frame3',frame3)

waitKey(0)
destroyAllWindows()