import cv2
import numpy as np
img_src=cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")
src=np.array([[67,89],[89,92],[24,213],[313,299]])
img_dst=cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")
dst=np.array([[100,134],[123,111],[34,199],[210,288]])
h,stat=cv2.findHomography(dst,src)
po=cv2.warpPerspective(img_src,h,(img_dst.shape[1],img_dst.shape[0]))
cv2.imshow("warped",po)
cv2.waitKey(0)

