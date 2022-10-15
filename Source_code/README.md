Steps below is for Original Bveeta Mini with Raspberry Pi 4 8G user (debian buster + ROS melodic)

Step 1:
install all dependencies below from your terminal:

sudo apt-get install ros-melodic-joy ros-melodic-teleop-twist-joy   ros-melodic-teleop-twist-keyboard ros-melodic-laser-proc   ros-melodic-rgbd-launch ros-melodic-depthimage-to-laserscan   ros-melodic-rosserial-arduino ros-melodic-rosserial-python   ros-melodic-rosserial-server ros-melodic-rosserial-client   ros-melodic-rosserial-msgs ros-melodic-amcl ros-melodic-map-server   ros-melodic-move-base ros-melodic-urdf ros-melodic-xacro   ros-melodic-compressed-image-transport ros-melodic-rqt*   ros-melodic-gmapping ros-melodic-navigation ros-melodic-interactive-markers ros-melodic-hector-mapping ros-melodic-map-server ros-melodic-slam-gmapping ros-melodic-teb-local-planner

Step 2:
Clone this repository in your Host PC

Step 3:
cd catkin_ws/src

Step 4:
git clone https://github.com/skj84/bveeta-R007

Step 5:
cd ..

Step 6:
catkin_make

Step 7: Run roscore
ssh into bveeta mini
roscore
 
Step 8: Bringup bveeta (for raspberry pi user ONLY)
ssh into bveeta mini
roslaunch bveeta_bringup bveeta_bringup.launch

Step 9:
In your Host PC, terminal test your robot with Gmapping slam
roslaunch gmapping bveeta_gmapping.launch

Step 10:
Please sudo chmod +x for nodes that are not runnning 

Step 11: 
sudo chmod 777 /dev/ttyUSB0
sudo chmod 777 /dev/ttyUSB1
if SDD cannot connect, unplug lidar and SDD together and plug in lidar first then followed by SDD 

if map appear then everything in your setup is done correctly. Otherwise, please refer to the hardcopy handout given
with the bveeta mini kit.

<a href="https://ibb.co/82vzBmt"><img src="https://i.ibb.co/1Kysn0j/Screenshot-from-2022-06-30-05-41-23.png" alt="Screenshot-from-2022-06-30-05-41-23" border="0"></a><br /><a target='_blank' href='https://500pxdownload.com/'></a><br />
