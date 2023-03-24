#Bizbot Technology
#For bveeta mini
#!/usr/bin/env python
import rospy
from ros_arduino_msgs.srv import ServoWrite

# Wait for the service to become available
rospy.wait_for_service('arduino/servo_write')

# Create a proxy to the service
servo_write = rospy.ServiceProxy('/arduino/servo_write', ServoWrite)

# Call the service
try:
    response = servo_write(1, 1.5) #if your servo is connect to pin 4
    print('Done !!')
except rospy.ServiceException as e:
    print('Service call failed:', e)
