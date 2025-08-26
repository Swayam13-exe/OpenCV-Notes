import cv2
dog1=cv2.imread('/home/student/Images/img18.jpg')
cv2.imshow("background",dog1)	
center=(440, 150)
radius=120
color=(0, 255, 0)
thickness=2
dog2=cv2.circle(dog1, center, radius, color, thickness)
cv2.imshow("dog",dog2)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()
