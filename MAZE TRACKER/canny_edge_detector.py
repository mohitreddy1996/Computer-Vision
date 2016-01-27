'''
1. noise reduction : gaussian filter
2. Finding itensity gradient.
filter with a sobel kernel in both horizontal and vertical directions.
find edge gradient and direction.
3. Non maximum suppression : remove unwanted pixels which 
may not constitute an edge. each pixel is checked
if it is a maximum in its neighbourhood in the 
direction of gradient.

4. hystersis thresholding : maxVal and minVal are assigned
if intensity gradient is >maxVal -> edge. if the value is >minVal but <maxVal
if it is a part of sure-edge include else remove.

'''
from cv2 import *
#from matplotlib import pyplot as plt
from numpy import *

img=imread('cr7.jpg',0)
edges=Canny(img,100,200)

imshow('title',edges)

waitKey(0)

plt.show()