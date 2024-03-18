import cv2
import numpy as np
img=cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,bin=cv2.threshold(grayscale,127,295,cv2.THRESH_BINARY)
kernel=np.ones((5,5),np.uint8)
dilate=cv2.dilate(bin,kernel,iterations=1)
cv2.imshow("original",img)
cv2.imshow("binary",bin)
cv2.imshow("dilate",dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()