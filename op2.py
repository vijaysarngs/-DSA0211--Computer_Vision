import cv2
image = cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")

cv2.imshow('Original Image', image)
cv2.waitKey(0)

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)


cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)


cv2.destroyAllWindows()
