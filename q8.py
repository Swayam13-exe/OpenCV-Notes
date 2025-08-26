import cv2
import numpy as np
img = cv2.imread("C:/Users/swayam/Desktop/DIVP/Images/img41.jpg", 0)

# Log transformation
c = 255 / np.log(1 + np.max(img))
log_trans = (c * np.log(1 + img)).astype(np.uint8)

# Power-law (gamma) transformation
gamma = 0.5   # try 0.4, 0.5, 2.0 etc
power_trans = np.array(255 * (img / 255) ** gamma, dtype=np.uint8)

# Negative of image
negative = 255 - img
cv2.imshow("Log Transformation", log_trans)
cv2.imshow("Power-law Transformation", power_trans)
cv2.imshow("Negative Image", negative)
cv2.waitKey(0)
cv2.destroyAllWindows()