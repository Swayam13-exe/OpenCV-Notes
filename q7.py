import cv2
import numpy as np
img = cv2.imread("C:/Users/swayam/Desktop/DIVP/Images/img41.jpg", 0)
min_val, max_val = np.min(img), np.max(img)
stretched = ((img - min_val) / (max_val - min_val) * 255).astype(np.uint8)
cv2.imshow("Original img41", img)
cv2.imshow("Contrast Stretched img41", stretched)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()