# cv2.line() , cv2.circle() , cv2.rectangle() , cv2.ellipse() , cv2.putText()

# parameter for the functions : img : image where the shapes will be drawn
# 2) color : ( B, G, R) : the values of BGR
# 3) thickness : by default 1 , if -1 is passed it fills the shapes
# 4) lineType : default 8-connected

# polylines(img,array containing the coordinates,True-closed polygon/False - open polygon,Color)
#the array passed has to be in shape as ROWS*1*2
# -1 the array shape is not changed.
# (0,0) : top left corner

# putText(img, TEXT , LOCATION TO START FROM, FONT , SCALE , COLOR , Thickness, cv2.LINE_AA <- for better looks)

import cv2
import numpy

img=numpy.zeros((512,512,3),numpy.uint8) # creates a black image #creates a 3-D image with uint8 : unsigned int (0,255)

cv2.line(img,(0,0),(511,511),(255,0,0),5) # img, start-coordinate , ending coordinate , color , thickness
cv2.rectangle(img,(380,0),(510,128),(0,255,0),3) # img , top left corner's coordinate, bottom right corner's coordinate , color, thickness
cv2.circle(img,(360,200),60,(0,0,255),-1) # img,centre,radius,color,thickness
#in ellipse centre, (major,minor axis length),(centre),stateAngle,endAngle,lengths,color
pts=numpy.array([[200,100],[150,123],[311,320],[250,510]],numpy.int32) # we form an array with coordinates feeded
pts=pts.reshape((-1,1,2)) # we make the array into the shape rows*1*2
cv2.polylines(img,[pts],True,(0,255,255)) # polylines is used to make multiple lines and list of coordinates are passed , True = closed polygon ,False= open polygon
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'MOHIT',(20,500),font,1,(255,255,255),2)
cv2.imshow('Line',img)
cv2.waitKey(0)
destroyAllWindows()