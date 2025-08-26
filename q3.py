import cv2
img1=cv2.imread('/home/student/Images/img34.jpg')
img1=cv2.resize(img1,(500,500))
cv2.imshow("original",img1)

#rgb
b,g,r=cv2.split(img1)
cv2.imshow("Model Blue Image", b)
cv2.imshow("Model Green Image", g)
cv2.imshow("Model Red Image", r)	

#negative transform	
neg=cv2.bitwise_not(img1)
cv2.imshow("negative transform",neg)

#circle
center=(420, 440)
radius=60
color=(0, 0, 0)
thickness=4
center1=(70, 50)
radius1=60	
color1=(0, 0, 0)
thickness1=4
img2=cv2.circle(img1, center, radius, color, thickness)
img2=cv2.circle(img1, center1, radius1, color1, thickness1)
cv2.imshow("dog",img2)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()