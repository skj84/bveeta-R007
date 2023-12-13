#Bizbot Technology
#Tutorial 11 
#Teleop Bveeta Mini with GUI Button

import rospy
from geometry_msgs.msg import Twist
import tkinter as tk

# Create a ROS publisher for sending velocity commands to the robot
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rospy.init_node('gui_control_node')

# Create a Twist message for velocity commands
twist = Twist()

# Create a Tkinter GUI window
window = tk.Tk()
window.title("Robot Control")

# Define a function for sending velocity commands to the robot
def send_velocity_command(linear_vel, angular_vel):
    twist.linear.x = linear_vel
    twist.angular.z = angular_vel
    pub.publish(twist)
    print("Sent command: linear=%s, angular=%s" % (linear_vel, angular_vel))

# Define the GUI button functions
def move_forward():
    send_velocity_command(0.5, 0)

def move_backward():
    send_velocity_command(-0.5, 0)

def turn_left():
    send_velocity_command(0, 0.5)

def turn_right():
    send_velocity_command(0, -0.5)

# Create the GUI buttons
btn_forward = tk.Button(window, text="Forward", command=move_forward)
btn_backward = tk.Button(window, text="Backward", command=move_backward)
btn_left = tk.Button(window, text="Left", command=turn_left)
btn_right = tk.Button(window, text="Right", command=turn_right)

# Add the buttons to the GUI window
btn_forward.pack()
btn_backward.pack()
btn_left.pack()
btn_right.pack()

# Define a function to handle keyboard interrupt (Ctrl+C)
def on_keyboard_interrupt(event):
    print("Keyboard interrupt, stopping program...")
    window.quit()

# Bind the keyboard interrupt function to Ctrl+C
window.bind("<Control-c>", on_keyboard_interrupt)

# Start the Tkinter main loop
try:
    window.mainloop()
except KeyboardInterrupt:
    print("Keyboard interrupt, stopping program...")
finally:
    # Stop the robot before exiting the program
    send_velocity_command(0, 0)
    rospy.sleep(1) # wait for the robot to stop
    rospy.signal_shutdown("GUI control program stopped")
