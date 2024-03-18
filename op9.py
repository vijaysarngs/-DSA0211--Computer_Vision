import cv2
import numpy as np

# Read the original image
original_image = cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")

# Get the height and width of the image
height, width = original_image.shape[:2]

# Define the rotation angle
angle = 30  # Specify the angle of rotation

# Perform clockwise rotation
rotation_matrix_clockwise = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
rotated_image_clockwise = cv2.warpAffine(original_image, rotation_matrix_clockwise, (width, height))

# Perform counterclockwise rotation
rotation_matrix_counterclockwise = cv2.getRotationMatrix2D((width / 2, height / 2), -angle, 1)
rotated_image_counterclockwise = cv2.warpAffine(original_image, rotation_matrix_counterclockwise, (width, height))

# Display the original, clockwise rotated, and counterclockwise rotated images
cv2.imshow('Original Image', original_image)
cv2.imshow('Clockwise Rotated Image', rotated_image_clockwise)
cv2.imshow('Counterclockwise Rotated Image', rotated_image_counterclockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()
