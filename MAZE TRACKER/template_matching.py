''' moves the template over the image and checks for a match.
if the input size (WxH) and template size (wxh)
then the output image will have size W-w+1,H-h+1
'''

from cv2 import *
from numpy import *

img=imread('cr73.jpg',0)
img2=img.copy()
template=imread('cr7face.jpg',0)
w,h=template.shape[::-1]

methods=['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR','TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']
for meth in methods:
	img=img2.copy()
	method=eval(meth)

	res=matchTemplate(img,template,method)
	min_val,max_val,min_loc,max_loc = minMaxLoc(res)

	if method in [TM_SQDIFF,TM_SQDIFF_NORMED]:
		top_left=min_loc
	else:
		top_left=max_loc

	bottom_right=(top_left[0]+w,top_left[1]+h)
	rectangle(img,top_left,bottom_right,255,2)

	imshow('img',img)
	waitKey(0)
