#!/usr/bin/env python

#This code is for bveeta mini for white line follower
#the code detect white line and follow
#Bizbot Technology
#Programmer: Ts.Khairul

# Import necessary libraries
import cv2
import numpy as np
import time
import serial


# Set up webcam
cap = cv2.VideoCapture(0)
cap.set(3, 320) # Set width of the frame
cap.set(4, 240) # Set height of the frame

# Define white color range in HSV
lower_white = np.array([0, 0, 150])
upper_white = np.array([255, 30, 255])

ser = serial.Serial('/dev/ttyUSB1', 57600, timeout=0.050)
time.sleep(2) #must wait for 2 seconds for connections established

# Start processing frames
while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold to get white color regions
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Find contours of white regions
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Follow the largest white line contour
      # Follow the largest white line contour
    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        moments = cv2.moments(largest_contour)
        area = moments['m00']
        if area > 0:
            cx = int(moments['m10']/area)
            cy = int(moments['m01']/area)

        # Control the motors based on the white line position
        if cx < 120:
             ser.write(b"m -0 -30  \r\n")
        elif cx > 200:
             ser.write(b"m -30 -0  \r\n")
        else:
             ser.write(b"m -60 -60  \r\n")

    # Display the frame
    cv2.imshow('frame', frame)

    # Wait for key press
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
