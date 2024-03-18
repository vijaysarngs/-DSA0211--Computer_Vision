import cv2
import numpy as np

original_image = cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")

x_translation = 50
y_translation = 30

translation_matrix = np.float32([[1, 0, x_translation], [0, 1, y_translation]])

translated_image = cv2.warpAffine(original_image, translation_matrix, (original_image.shape[1], original_image.shape[0]))

cv2.imshow('Original Image', original_image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
