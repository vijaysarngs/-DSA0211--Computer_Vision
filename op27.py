import cv2
import numpy as np
image = cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")
img2 = cv2.imread("C:/Users/vijay/OneDrive/Pictures/catawbiense/WhatsApp Image 2024-01-25 at 11.05.20_0f518504.jpg")
print(image.shape)
cv2.imshow("original", image)
imageCopy = image.copy()
cv2.circle(imageCopy, (100, 100), 30, (255, 0, 0), -1)
cv2.imshow('image', image)
cv2.imshow('image copy', imageCopy)
cropped_image = image[80:280, 150:330]
cv2.imshow("cropped", cropped_image)
cv2.imwrite("Cropped Image.jpg", cropped_image)
dst = cv2.addWeighted(image, 0.5, img2, 0.7, 0)
img_arr = np.hstack((image, img2))
cv2.imshow('Input Images',img_arr)
cv2.imshow('Blended Image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
