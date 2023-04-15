#!/usr/bin/env python
#Bizbot Technology
#For bveeta mini

import rospy
from ros_arduino_msgs.srv import ServoWrite

# Wait for the service to become available
rospy.wait_for_service('arduino/servo_write')

# Create a proxy to the service
servo_write = rospy.ServiceProxy('/arduino/servo_write', ServoWrite)

# Get the servo pin number from the user
while True:
    try:
        pin = int(input('Enter the servo number (0 if servo connect to pin 7, and 1 if servo connect to pin 4): '))
        break
    except ValueError:
        print('Invalid input, please enter an integer.')

# Get the desired position from the user
while True:
    try:
        pos = int(input('Enter the desired position in radian (0-3.142): '))
        if pos < 0 or pos > 180:
            raise ValueError('Position must be between 0 and 180.')
        break
    except ValueError as e:
        print(e)

# Call the service
try:
    response = servo_write(pin, pos)
    print('Done !!')
except rospy.ServiceException as e:
    print('Service call failed:', e)
