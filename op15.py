import cv2
import numpy as np
img1 = cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")
img2 = cv2.imread("C:/Users/vijay/OneDrive/Pictures/catawbiense/WhatsApp Image 2024-01-25 at 11.05.20_0f518504.jpg")
pts1 = np.array([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.array([[100, 100], [300, 100], [100, 300], [300, 300]])

H, _ = cv2.findHomography(pts1, pts2)

dst = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()