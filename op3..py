import cv2
img=cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,30,50)
cv2.imshow("original",img)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()