#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32, Bool
import RPi.GPIO as GPIO
import time
from math import pi

leftEn = 13         #   Purple
rightEn = 12        #   Red

leftBackward = 5    #   Blue
leftForward = 6     #   Green
rightForward = 16   #   Yellow
rightBackward = 20  #   Orange

motor_rpm = 60              #   max rpm of motor on full voltage 
wheel_diameter = 0.065      #   in meters
wheel_separation = 0.17     #   in meters
max_pwm_val = 100           #   100 for Raspberry Pi , 255 for Arduino
min_pwm_val = 0            #   Minimum PWM value that is needed for the robot to move

wheel_radius = wheel_diameter/2
circumference_of_wheel = 2 * pi * wheel_radius
max_speed = (circumference_of_wheel*motor_rpm)/60   #   m/sec

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(leftEn, GPIO.OUT)
GPIO.setup(rightEn, GPIO.OUT)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)
GPIO.setup(rightBackward, GPIO.OUT)

pwmL = GPIO.PWM(leftEn, 100)
pwmL.start(0)
pwmR = GPIO.PWM(rightEn, 100)
pwmR.start(0)

def stop():
    global lpwm_pub
    global rpwm_pub
    global ldir_pub
    global rdir_pub
    
    #print('stopping')
    pwmL.ChangeDutyCycle(0)
    GPIO.output(leftForward, GPIO.HIGH)
    GPIO.output(leftBackward, GPIO.HIGH)
    pwmR.ChangeDutyCycle(0)
    GPIO.output(rightForward, GPIO.HIGH)
    GPIO.output(rightBackward, GPIO.HIGH)
    
    lpwm_pub.publish(0)
    rpwm_pub.publish(0)
    ldir_pub.publish(1)
    rdir_pub.publish(1)
    
def wheel_vel_executer(left_speed, right_speed):
    global max_pwm_val
    global min_pwm_val
    
    global lpwm_pub
    global rpwm_pub
    global ldir_pub
    global rdir_pub
    
    lspeedPWM = max(min(((abs(left_speed)/max_speed)*max_pwm_val),max_pwm_val),min_pwm_val)
    rspeedPWM = max(min(((abs(right_speed)/max_speed)*max_pwm_val),max_pwm_val),min_pwm_val)
    pwmL.ChangeDutyCycle(lspeedPWM)
    pwmR.ChangeDutyCycle(rspeedPWM)
    
    lpwm_pub.publish(int(lspeedPWM))
    rpwm_pub.publish(int(rspeedPWM))
    
    if left_speed >= 0 :
        GPIO.output(leftForward, GPIO.HIGH)
        GPIO.output(leftBackward, GPIO.LOW)
        ldir_pub.publish(1)
    else :
        GPIO.output(leftForward, GPIO.LOW)
        GPIO.output(leftBackward, GPIO.HIGH)
        ldir_pub.publish(0)
        
    if right_speed >= 0 :
        GPIO.output(rightForward, GPIO.HIGH)
        GPIO.output(rightBackward, GPIO.LOW)
        rdir_pub.publish(1)
    else :
        GPIO.output(rightForward, GPIO.LOW)
        GPIO.output(rightBackward, GPIO.HIGH)
        rdir_pub.publish(0)
    
def callback(data):

    # refer this for understanding the formula 
    # http://www.cs.columbia.edu/~allen/F17/NOTES/icckinematics.pdf
    
    global wheel_radius
    global wheel_separation
    
    linear_vel = data.linear.x                  # Linear Velocity of Robot
    angular_vel = data.angular.z                # Angular Velocity of Robot
    #print(str(linear)+"\t"+str(angular))
    
    VrplusVl  = 2 * linear_vel
    VrminusVl = angular_vel * wheel_separation
    
    right_vel = ( VrplusVl + VrminusVl ) / 2      # right wheel velocity along the ground
    left_vel  = VrplusVl - right_vel              # left wheel velocity along the ground
    
    #print (str(left_vel)+"\t"+str(right_vel))
    
    if (left_vel == 0.0 and right_vel == 0.0):
        stop()
    else:
        wheel_vel_executer(left_vel, right_vel)
        
def listener():
    
    global lpwm_pub
    global rpwm_pub
    global ldir_pub
    global rdir_pub
    
    rospy.init_node('cmdvel_listener', anonymous=False)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    lpwm_pub = rospy.Publisher('lpwm', Int32, queue_size = 10)
    rpwm_pub = rospy.Publisher('rpwm', Int32, queue_size = 10)
    ldir_pub = rospy.Publisher('ldir', Bool, queue_size = 10)
    rdir_pub = rospy.Publisher('rdir', Bool, queue_size = 10)
    rospy.spin()

if __name__== '__main__':
    print('Tortoisebot Differential Drive Initialized with following Params-')
    print('Motor Max RPM:\t'+str(motor_rpm)+' RPM')
    print('Wheel Diameter:\t'+str(wheel_diameter)+' m')
    print('Wheel Separation:\t'+str(wheel_separation)+' m')
    print('Robot Max Speed:\t'+str(max_speed)+' m/sec')
    listener()
