import cv2
import numpy as np
img=cv2.imread('/home/student/Images-20250722T070237Z-1-001/Images/img45.jpg')
cv2.imshow("original_image",img) 

#resize image
size=img.shape
print(size)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()
resize_img=cv2.resize(img,(size[1]//2,size[0]//2))
cv2.imshow("window",resize_img)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()

#crop image
x,y,w,h=10,8,170,130
cropped=img[y:y+h,x:x+w]
cv2.imshow("cropped image",cropped)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()

# Split the RGB channels 	
b,g,r = cv2.split(img)
cv2.imshow("Model Blue Image", b)
cv2.imshow("Model Green Image", g)
cv2.imshow("Model Red Image", r)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()

#Convert to HSV 
hsvimg=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)	
cv2.imshow("HSV", hsvimg)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()

# Convert to binary image	
bw_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,bw = cv2.threshold(bw_img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", bw)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()