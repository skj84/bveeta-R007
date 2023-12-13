
# Simulation Package Installation Guide

## Install Bveeta Mini Package

To install the necessary ROS packages, use the following command:

```bash
sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy ros-noetic-teleop-twist-keyboard ros-noetic-amcl ros-noetic-map-server ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro ros-noetic-rqt-image-view ros-noetic-gmapping ros-noetic-navigation ros-noetic-joint-state-publisher ros-noetic-robot-state-publisher ros-noetic-slam-gmapping ros-noetic-dwa-local-planner ros-noetic-joint-state-publisher-gui
```

## Teleoperate Bveeta Mini

To teleoperate Bveeta Mini, execute the following commands in separate terminal windows:

```bash
$: roscore
$: roslaunch ros_arduino_python arduino.launch
$: rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

## SLAM Bveeta Mini

For SLAM with Bveeta Mini, run these commands in different terminals:

```bash
$: roscore
$: roslaunch ros_arduino_python arduino.launch
$: rosrun teleop_twist_keyboard teleop_twist_keyboard.py
$: roslaunch bveeta_firmware server_bringup.launch
$: roslaunch bveeta_cartomapping bveeta_cartomapping.launch
$: rosrun map_server map_saver -f my_map
```

## Navigation Bveeta Mini

For navigating Bveeta Mini, use the following commands:

```bash
$: roscore
$: roslaunch ros_arduino_python arduino.launch
$: rosrun teleop_twist_keyboard teleop_twist_keyboard.py
$: roslaunch bveeta_firmware server_bringup.launch
$: roslaunch bveeta_cartonavigation bveeta_cartonavigation.launch map_file:=my_map
```

## Simulation SLAM Bveeta Mini

For SLAM with Bveeta Mini, run these commands in different terminals:

```bash
$: roscore
$: roslaunch bveeta_gazebo bveeta_playground.launch
$: rosrun bveeta_control bveeta_teleop_key.py
$: roslaunch bveeta_firmware server_bringup.launch
$: roslaunch bveeta_cartomapping bveeta_cartomapping.launch
$: rosrun map_server map_saver -f my_map
```

## Simulation Navigation Bveeta Mini

For navigating Bveeta Mini, use the following commands:

```bash
$: roscore
$: roslaunch bveeta_gazebo bveeta_playground.launch
$: rosrun bveeta_control bveeta_teleop_key.py
$: roslaunch bveeta_firmware server_bringup.launch
$: roslaunch bveeta_navigation bveeta_navigation.launch
$: roslaunch bveeta_cartonavigation bveeta_cartonavigation.launch map_file:=my_map
```
