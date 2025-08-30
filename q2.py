import cv2
img1=cv2.imread('/home/student/Images/img39.jpg')
cv2.imshow("background",img1)
#cropped
x,y,w,h=10,8,170,130
cropped=img1[y:y+h,x:x+w]
cv2.imshow("cropped image",cropped)
#negative transform
neg=cv2.bitwise_not(img1)
cv2.imshow("negative_transform",neg)
#conver to binary
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
_,bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", bw)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()
