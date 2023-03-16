#!/usr/bin/env python

#code ini detect bola merah sahaja.
#Bizbot Technology
#Programmer: Ts.Khairul

import cv2

# Load the image or video
cap = cv2.VideoCapture(0)  # Use 0 for webcam or specify file path for video

# Define the lower and upper bounds of the red color in HSV color space
red_lower = (0, 120, 70)
red_upper = (10, 255, 255)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, red_lower, red_upper)

    # Find contours of the red color in the mask image
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a rectangle around the ball if it is detected
    if len(contours) > 0:
        # Find the largest contour (assuming it is the ball)
        largest_contour = max(contours, key=cv2.contourArea)
        (x, y, w, h) = cv2.boundingRect(largest_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting image
    cv2.imshow('frame', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
