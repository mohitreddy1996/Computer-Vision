# imread : read an image.
# imshow : to display an image
import cv2
import numpy

img=cv2.imread('cr7.jpg',0) # the parameter field : 1:-color image,transparency is neglected. 0 :- grayscale. -1 :- loads as it is.
#cv2.imwrite('cr72.jpg',img)
#cv2.namedWindow('image',cv2.WINDOW_NORMAL) #can load the image in the window later.cv2.WINDOW_NORMAL : we can resize the image
cv2.imshow('image',img) # The name of the image window.
cv2.imwrite('cr7gray.jpg',img)
cv2.waitKey(0) # 0 is passed , waits indefinitely untill a key is pressed
cv2.destroyAllWindows

''' to kill the windows on user specified inputs give : k=cv2.waitkey(0)
k should be compared with ASCII value of the specified key '''