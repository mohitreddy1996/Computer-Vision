# can be done using cv2.blur(img,(x,y) <- kernal size)
from cv2 import *
from numpy import *

img=imread('cr7.jpg')

res=blur(img,(3,3)) # convolution of kernel ove rthe image and taking the average

# gaussian blurring. using cv2.Gaussianblur(). parameters : width and height <- should be positive and odd
# standard deviation in X and Y, both are almost considered the same values.
#both are effective in removing the gaussain noise.

res2=GaussianBlur(img,(3,3),0) # 0 -> standard deviation of x same for y. 

# Median Blurring : more effective for salt-pepper noises in the images.
# takes median of all the pixels under the kernel and replaces the central element with that pixel value
# in Gaussian or convolution , a new value or pixel value is assigned to the central pixel, in median blurring a pixel value is assigned.
img2=imread('salt-pepper_noises.jpg')
res3=medianBlur(img2,3)

# bilateral blurring : slower filtering process. preserves edges. gaussian function which considers differnce in itensity. so the pixels under a kernel
# with similar intensity are considered for the central pixel.

res4=bilateralFilter(img,3,10,10)

imshow('image',img)
#imshow('blurred image',res) almost same result as Gaussian blur
imshow('Gaussain blurring',res2)
imshow('original_salt-pepper noise',img2)
imshow('Median Blur',res3)
imshow('Bilateral Blur',res4) # more effective than gaussian or convolution.qq
waitKey(0)
destroyAllWindows()