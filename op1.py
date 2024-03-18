import cv2
image = cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")
cv2.imshow('Original Image', image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.imwrite('gray_image.jpg', gray_image)
cv2.destroyAllWindows()
