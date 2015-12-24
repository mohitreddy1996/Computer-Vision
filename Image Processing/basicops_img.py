# basic operations on image
#access pixel values and modify them.
# access image property , region of image (ROI)
# splitting and merging images

from cv2 import *
from numpy import *
from matplotlib import pyplot as plt 

img=imread('cr7.jpg')
img1=imread('cr7gray.jpg')
px=img[100,100] # x and y coordinates are given as inputs.
# for BGR it return b,g,r values. for grayscale : it returns itensity.
print px
# to access blue pixel : 
px1=img1[100,100] # returns itensity
print px1
# to access the BGR values : img.item(x,y, (0,1,2) : for BGR values)
# and to set the pixel values : img.itemset((x,y,(0/1/2)),value)
imshow('image',img)
waitKey(0)
destroyAllWindows()
#image properties
print img.shape # returns the shape
print img.size # returns the size
print img.dtype # data type

# ROI : region of image , used for eye detection , facial recog. we select the face only and search for eyes. -increases accuracy and performance
# numpy array to get the index of the object ( rectangluar frame) and place that object somewhere in the image
ball=img[150:177 , 110:140] # [ y1 : y2, x1:x2] <- format
img[150:177,180:210]=ball
namedWindow('image',WINDOW_NORMAL)
imshow('image',img)
waitKey(0)
destroyAllWindows()

# splitting and merging of images, b,g,r = cv2.split(img) , divides the image into b,g,r pixels 
# merging after each plane(b,g,r) : img=merge(b,g,r)
# or use numpy arrays to work on bgr

# displaying multiple images using pyplot( subplots)
# and ADDING BORDERS
# parameters : (img, top margin, bottom margin, left margin, right margin , border_type,value <- only if border type is BORDER_CONSTANT)

GREEN=[0,255,0]
img2=imread('cr7.jpg')

replicate = copyMakeBorder(img2,10,10,10,10,BORDER_REPLICATE)
constant = copyMakeBorder(img2,10,10,10,10,BORDER_CONSTANT,value=GREEN)
reflect = copyMakeBorder(img2,10,10,10,10,BORDER_REFLECT)
reflect101 = copyMakeBorder(img2,10,10,10,10,BORDER_REFLECT_101)
wrap = copyMakeBorder(img2,10,10,10,10,BORDER_WRAP)

plt.subplot(321),plt.imshow(img2,'mohit'),plt.title('original')
plt.subplot(322),plt.imshow(replicate,'mohit'),plt.title('replicate')
plt.subplot(323),plt.imshow(reflect,'mohit'),plt.title('reflect')
plt.subplot(324),plt.imshow(reflect101,'mohit'),plt.title('reflect101')
plt.subplot(325),plt.imshow(constant,'mohit'),plt.title('constant')
plt.subplot(326),plt.imshow(wrap,'mohit'),plt.title('wrap')

plt.show()