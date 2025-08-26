import cv2
img = cv2.imread("C:/Users/swayam/Desktop/DIVP/Images/img30.jpg", 0)
equalized = cv2.equalizeHist(img)
cv2.imshow("Original img30", img)
cv2.imshow("Equalized img30", equalized)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()