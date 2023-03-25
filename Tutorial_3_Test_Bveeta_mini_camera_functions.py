#Tutorial 3:Test bveeta mini camera with Open CV
#functions involved
#variable involved
#Author: Bizbot Technology

import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Webcam is not available. Please check the connections or reset the webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
