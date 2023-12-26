
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


# Running Cartographer in Various Configurations

## 1. Run Cartographer

To run Cartographer for mapping, execute the following commands:

```bash
# Launch the robot bringup
roslaunch bveeta_bringup bveeta_bringup.launch

# Launch the firmware server
roslaunch bveeta_firmware server_bringup.launch

# Launch the Cartographer for mapping with RViz
roslaunch bveeta_cartomapping bveeta_cartomapping_rviz.launch

# Run the teleop twist keyboard for manual control
rosrun teleop_twist_keyboard teleop_twist_keyboard.py

# Save the map
rosrun map_server map_saver -f my_map
```

## 2. Run Cartographer with Move-Base

For running Cartographer with move-base functionality:

```bash
roslaunch bveeta_bringup bveeta_bringup.launch
roslaunch bveeta_firmware server_bringup.launch
roslaunch bveeta_cartonavigation bveeta_cartonavigation.launch
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
rosrun map_server map_server my_map.yaml
```

## 3. Run Cartographer with Gazebo Simulation

To simulate Cartographer with Gazebo:

```bash
roslaunch bveeta_gazebo maze.launch
roslaunch bveeta_firmware server_bringup.launch
roslaunch bveeta_cartonavigation bveeta_cartonavigation.launch
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
rosrun map_server map_server my_map.yaml
```

## 4. Run Cartographer with Move-Base and Gazebo Simulation

For a Gazebo simulation combined with move-base:

```bash
roslaunch bveeta_gazebo maze.launch
roslaunch bveeta_firmware server_bringup.launch
roslaunch bveeta_cartonavigation bveeta_cartonavigation.launch
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
rosrun map_server map_server my_map.yaml
```

