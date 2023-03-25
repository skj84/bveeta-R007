#author: Ts. Khai
#Bizbot Technology
#This is simple action server for moving robot to specific goal sequence with GUI button
import Tkinter
import tkMessageBox
import actionlib
import rospy

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult
rospy.loginfo("Sequential GOAL navigation program completed!!.... Now terminated..")
rospy.init_node('send_client_goal')
client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
#--------------------------------gui from tkinter code ------------------------

top = Tkinter.Tk()
root = Tkinter.Tk()
root.geometry("200x100")

def goal1():
	tkMessageBox.showinfo("Aproach goal 1", "Let's GO!")
	#move robot to goal 1 
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'map' 
	goal.target_pose.pose.position.x = 0.359075546265
	goal.target_pose.pose.position.y = -2.03587222099
	goal.target_pose.pose.orientation.z = 1.0
	goal.target_pose.pose.orientation.w = 0.000

	rospy.loginfo("Sedang mencari GOAL 1")
	client.send_goal(goal)
	client.wait_for_result()
	rospy.loginfo("Goal 1 reached")


def goal2():
	tkMessageBox.showinfo("Aproach goal 2", "Let's GO!")
	#move robot to goal 2 
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'map' 
	goal.target_pose.pose.position.x = 1.06313192844
	goal.target_pose.pose.position.y = -0.293134450912
	goal.target_pose.pose.orientation.z = 1.0
	goal.target_pose.pose.orientation.w = 0.000

	rospy.loginfo("Sedang mencari GOAL 2")
	client.send_goal(goal)
	client.wait_for_result()
	rospy.loginfo("Goal 2 reached")

def goal3():
	tkMessageBox.showinfo("Aproach goal 3", "Let's GO!")
	#move robot to goal 3 
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'map' 
	goal.target_pose.pose.position.x = 3.84633827209
	goal.target_pose.pose.position.y = -1.25584077835
	goal.target_pose.pose.orientation.z = 1.0
	goal.target_pose.pose.orientation.w = 0.000

	rospy.loginfo("Sedang mencari GOAL 3")
	client.send_goal(goal)
	client.wait_for_result()
	rospy.loginfo("Goal 3 reached")


def goal4():
	tkMessageBox.showinfo("Aproach goal 4", "Let's GO!")
	#move robot to goal 4
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'map' 
	goal.target_pose.pose.position.x = 2.91423511505
	goal.target_pose.pose.position.y = -3.9102845192
	goal.target_pose.pose.orientation.z = 1.0
	goal.target_pose.pose.orientation.w = 0.000

	rospy.loginfo("Sedang mencari GOAL 4")
	client.send_goal(goal)
	client.wait_for_result()
	rospy.loginfo("Goal 4 reached")

def Close():
    root.destroy()

A = Tkinter.Button(top, text="Goal 1", command = goal1)
A.pack()

B = Tkinter.Button(top, text="Goal 2", command = goal2)
B.pack()

C = Tkinter.Button(top, text="Goal 3", command = goal3)
C.pack()

D = Tkinter.Button(top, text="Goal 4", command = goal4)
D.pack()

# Button for closing
exit_button = Tkinter.Button(root, text="Exit", command=Close)
exit_button.pack(pady=20)

top.mainloop()
#--------------------------------gui from tkinter code ------------------------

rospy.loginfo("Waiting for move base server")
client.wait_for_server()
