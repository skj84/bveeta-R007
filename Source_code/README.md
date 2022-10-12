Step 1:
Clone this repository in your Host PC

Step2:
cd catkin_ws/src
git clone https://github.com/skj84/bveeta-R007

Step3:
install all dependencies below from your terminal:

sudo apt-get install ros-melodic-joy ros-melodic-teleop-twist-joy   ros-melodic-teleop-twist-keyboard ros-melodic-laser-proc   ros-melodic-rgbd-launch ros-melodic-depthimage-to-laserscan   ros-melodic-rosserial-arduino ros-melodic-rosserial-python   ros-melodic-rosserial-server ros-melodic-rosserial-client   ros-melodic-rosserial-msgs ros-melodic-amcl ros-melodic-map-server   ros-melodic-move-base ros-melodic-urdf ros-melodic-xacro   ros-melodic-compressed-image-transport ros-melodic-rqt*   ros-melodic-gmapping ros-melodic-navigation ros-melodic-interactive-markers ros-melodic-hector-mapping ros-melodic-map-server ros-melodic-slam-gmapping

Step 4: Run roscore
ssh into bveeta mini
roscore
 
Step 5: Bringup bveeta
ssh into bveeta mini
roslaunch bveeta_bringup bveeta_bringup.launch

Step 6:
In your Host PC, terminal test your robot with Gmapping slam
roslaunch gmapping bveeta_gmapping.launch

if map appear then everything in your setup is done correctly. Otherwise, please refer to the hardcopy handout given
with the bveeta mini kit.
