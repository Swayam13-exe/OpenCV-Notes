import cv2
import numpy as np
back = cv2.imread("C:/Users/swayam/Desktop/DIVP/Images/img6.jpg")
fore = cv2.imread("C:/Users/swayam/Desktop/DIVP/Images/img43.jpg")
mask = cv2.imread("C:/Users/swayam/Desktop/DIVP/Images/p2.png")  
back = cv2.resize(back, (500,500)) 
fore = cv2.resize(fore, (500,500))
mask = cv2.resize(mask, (500,500))
bg=cv2.bitwise_and(fore,mask)
final=cv2.add(bg,back)
cv2.imshow("setup",final)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()