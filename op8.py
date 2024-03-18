import cv2

original_image = cv2.imread("C:/Users/vijay/OneDrive/Pictures/campanulatum/WhatsApp Image 2024-01-24 at 10.24.43_e3180346.jpg")

bigger_image = cv2.resize(original_image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

smaller_image = cv2.resize(original_image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Original Image', original_image)
cv2.imshow('Bigger Image', bigger_image)
cv2.imshow('Smaller Image', smaller_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
