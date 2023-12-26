
# Installation Guide

## Required Dependencies:

Install the necessary ROS Noetic packages using the following command:

```
sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy ros-noetic-teleop-twist-keyboard ros-noetic-amcl ros-noetic-map-server ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro ros-noetic-rqt-image-view ros-noetic-gmapping ros-noetic-navigation ros-noetic-joint-state-publisher ros-noetic-robot-state-publisher ros-noetic-slam-gmapping ros-noetic-dwa-local-planner ros-noetic-joint-state-publisher-gui ros-noetic-camera-info-manager ros-noetic-tf2-sensor-msgs ros-noetic-mbf-costmap-core ros-noetic-move-base-flex ros-noetic-costmap-converter
```

## Cloning the Repository:

Clone the repository in your Host PC:

```
cd catkin_ws/src
git clone -b noetic https://github.com/skj84/bveeta-R007
```

## Installing YDLidar:

Follow these steps to install YDLidar:

```
git clone https://github.com/YDLIDAR/YDLidar-SDK.git
cd YDLidar-SDK/
mkdir build
cd build
cmake ..
make
sudo make install
```

## Building with Catkin:

Build the package using catkin_make:

```
cd ~/catkin_ws
catkin_make
```

## Setting Execute Permissions:

Allow execute permission for the necessary scripts:

```
roscd ros_arduino_python/nodes
sudo chmod +x arduino_node.py
```
