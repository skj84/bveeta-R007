#!/usr/bin/env python
#This code prompted by Bveeta Mini
#Generated code by chatgpt ai 

import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class FaceDetectionNode:
    def __init__(self):
        rospy.init_node('face_detection_control_node', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/usb_cam/image_raw', Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.target_x = Float32()
        self.target_x_pub = rospy.Publisher('/face_detection/target_x', Float32, queue_size=1)
        self.target_x_threshold = 0.05

    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            if len(faces) > 0:
                x, y, w, h = faces[0]
                target_x = x + w / 2
                self.target_x.data = target_x
                self.target_x_pub.publish(self.target_x)
                
                error = target_x - cv_image.shape[1] / 2
                angular_vel = -0.01 * error  # Adjust this scaling factor as needed
                linear_vel = 0.1  # Adjust this velocity as needed
                
                twist = Twist()
                twist.linear.x = linear_vel
                twist.angular.z = angular_vel
                self.cmd_vel_pub.publish(twist)
            else:
                self.target_x.data = -1.0
                self.target_x_pub.publish(self.target_x)
                
                twist = Twist()
                self.cmd_vel_pub.publish(twist)
            
        except Exception as e:
            print(e)

if __name__ == '__main__':
    try:
        face_detection_node = FaceDetectionNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
