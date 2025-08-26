import cv2
img1=cv2.imread("/home/student/Images/img61.jpg")
img2=cv2.imread("/home/student/Images/Sample_Image.jpg")
img1=cv2.resize(img1,(500,500)) 
img2=cv2.resize(img2,(500,500))
cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
final=cv2.bitwise_and(img1,img2)
cv2.imshow("combine image",final)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()