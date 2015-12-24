# otsu's binarization is applicable only for bimodal images : ( two histogram peaks)
# the threshold value selected for such an image is the value in the middle of the two peaks <-otsu's binarization does.
# for such thresholds pass an extra flag = cv2.THRESH_OTSU and the threshold as 0. <- finds the threshold value and is returned

from cv2 import *
from numpy import *

img=imread('noisy_image.png',0)

#img=cvtColor(img,COLOR_BGR2GRAY)
#global thresholding
ret1,th1=threshold(img,127,255,THRESH_BINARY)
#otsu thresholding
ret2,th2=threshold(img,0,255,THRESH_BINARY+THRESH_OTSU)
# gaussian blurness + otsu threshold.
blur=GaussianBlur(img,(5,5),0)
ret3,th3=threshold(blur,0,255,THRESH_BINARY+THRESH_OTSU)
# plot histograms using matplotlib. Otsu binarization with gaussian blurness gives better results.

imshow('image1',th1)
imshow('image2',th2)
imshow('image3',th3)

waitKey(0)
destroyAllWindows()