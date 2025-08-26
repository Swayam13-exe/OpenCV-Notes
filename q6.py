import cv2
import numpy as np

#rectangle
img1=cv2.imread('/home/student/Images/img19.jpg')
img1=cv2.resize(img1,(500,500))
cv2.imshow("bug",img1)
start_point = (80,70)
end_point = (420, 450)
color = (255, 255, 255)
thickness = 5
bg = cv2.rectangle(img1, start_point, end_point, color, thickness)
cv2.imshow("ladybug",bg)

#2 rotation
img2=cv2.imread('/home/student/Images/img20.jpg')
cv2.imshow("background",img2)
height, width = img2.shape[:2]
center = (width // 2, height // 2)
angle = 90 # degrees
scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(img2, rotation_matrix, (width, height))
cv2.imshow("rotated image",rotated_image)

#1 translation
tx, ty = 100, 50
translation_matrix = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])
translated_image = cv2.warpAffine(rotated_image, translation_matrix, (width, height))
cv2.imwrite('rotated_then_translated.jpg', translated_image)
cv2.imshow('Rotated and Translated', translated_image)

#sampling and quImage sampling and Quantization
import cv2
import numpy as np
image = cv2.imread("C:/Users/swayam/Desktop/DIVP/Images/img20.jpg")

# Sampling (downscale)
small_sample = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
cv2.imshow("Sampled Image", small_sample)
cv2.waitKey(0)

# Quantization (reduce gray/color levels)
levels = 4  # try 2, 4, 8 for different results
quantized_img = np.floor(small_sample / (256 / levels)) * (256 / levels)
quantized_img = quantized_img.astype(np.uint8)
cv2.imshow("Quantized Image", quantized_img)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()