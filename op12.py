import cv2
import numpy as np
cv=cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")
he,wi,ch=cv.shape
pts = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2=np.float32([[100,50],[300,0],[0,300],[300,300]])
m=cv2.getPerspectiveTransform(pts,pts2)
p=cv2.warpPerspective(cv,m,(wi,he))
cv2.imshow("transformed",p)
cv2.waitKey(0)
