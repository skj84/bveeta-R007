#!/usr/bin/env python

#Coding ini detect bola merah dan bveeta mini follow bola
#Bizbot Technology
#Programmer: Ts.Khairul

import cv2
import serial
import time

# Connect to the serial port to send commands to the robot
#ser = serial.Serial('/dev/ttyUSB1', 57600) # Replace with the correct port and baud rate for your robot
#time.sleep(2)

# Load the image or video
cap = cv2.VideoCapture(0)  # Use 0 for webcam or specify file path for video

# Define the lower and upper bounds of the red color in HSV color space
red_lower = (0, 120, 70)
red_upper = (10, 255, 255)

ser = serial.Serial('/dev/ttyUSB1', 57600, timeout=0.050)
time.sleep(2) #must wait for 2 seconds for connections established

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

        # Compute the center of the ball
        cx = int(x + w/2)
        cy = int(y + h/2)

        # Send commands to the robot to follow the ball
        if cx < 320:
            #ser.write(b'l')  # Turn left
            ser.write(b"m 0 -30  \r\n")
        elif cx > 320:
            #ser.write(b'r')  # Turn right
            ser.write(b"m -30 0  \r\n")
        else:
            #ser.write(b'f')  # Move forward
            ser.write(b"m -80 -80  \r\n")
    else:
        # Stop the robot if the ball is not detected
        #ser.write(b's')  # Stop moving
        ser.write(b"m 0 0  \r\n")

    # Display the resulting image
    cv2.imshow('frame', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
