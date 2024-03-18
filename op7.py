import cv2

# Read the video
video_capture = cv2.VideoCapture("C:/Users/vijay/Videos/The Boys S02E01.mp4")

while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    cv2.imshow('Slow Motion Video', frame)
    cv2.waitKey(80)


    cv2.imshow('Fast Motion Video', frame)
    cv2.waitKey(30)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
