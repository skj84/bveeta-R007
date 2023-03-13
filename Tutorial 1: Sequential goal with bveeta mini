#author: Bizbot Technology
#This is simple action server for moving robot to specific goal sequence
#Toget the actual value of pose.position x,y or z please echo the topics pose

import actionlib
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult

rospy.init_node('send_client_goal')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
rospy.loginfo("Waiting for move base server")
client.wait_for_server()

#move robot to goal 1 (home)
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'map' 
goal.target_pose.pose.position.x = 0.159249559045
goal.target_pose.pose.position.y = 0.159249559045
goal.target_pose.pose.orientation.z = 1.0
goal.target_pose.pose.orientation.w = 0.000

rospy.loginfo("Sedang mencari GOAL 1")
client.send_goal(goal)
client.wait_for_result()
rospy.loginfo("Goal 1 reached")

#move robot to goal 2
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'map' 
goal.target_pose.pose.position.x = 1.2387996912
goal.target_pose.pose.position.y = -2.37061619759
goal.target_pose.pose.orientation.z = 1.0
goal.target_pose.pose.orientation.w = 0.000

rospy.loginfo("Sedang mencari GOAL 2")
client.send_goal(goal)
client.wait_for_result()
rospy.loginfo("Goal 2 reached")

#move robot to goal 3
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'map' 
goal.target_pose.pose.position.x = 0.482237994671
goal.target_pose.pose.position.y = -2.21642422676
goal.target_pose.pose.orientation.z = 1.0
goal.target_pose.pose.orientation.w = 0.000

rospy.loginfo("Sedang mencari GOAL 3")
client.send_goal(goal)
client.wait_for_result()
rospy.loginfo("Goal 3 reached")

#move robot to goal 4
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'map' 
goal.target_pose.pose.position.x = 1.44501769543
goal.target_pose.pose.position.y = 0.224104806781
goal.target_pose.pose.orientation.z = 1.0
goal.target_pose.pose.orientation.w = 0.000

rospy.loginfo("Sedang mencari GOAL 4")
client.send_goal(goal)
client.wait_for_result()
rospy.loginfo("Goal 4 reached")

rospy.loginfo("Sequential GOAL navigation program completed!!.... Now terminated..")
