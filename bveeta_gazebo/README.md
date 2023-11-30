
# Simulation Package Installation Guide

## Install Simulation Package

To install the necessary ROS packages, use the following command:

```bash
sudo apt-get install ros-melodic-joy ros-melodic-teleop-twist-joy ros-melodic-teleop-twist-keyboard ros-melodic-amcl ros-melodic-map-server ros-melodic-move-base ros-melodic-urdf ros-melodic-xacro ros-melodic-rqt-image-view ros-melodic-gmapping ros-melodic-navigation ros-melodic-joint-state-publisher ros-melodic-robot-state-publisher ros-melodic-slam-gmapping ros-melodic-dwa-local-planner ros-melodic-joint-state-publisher-gui ros-melodic-cartographer-ros ros-melodic-cartographer-rviz
```

## Teleoperate Bveeta Mini

To teleoperate Bveeta Mini, execute the following commands in separate terminal windows:

```bash
$: roscore
$: roslaunch bveeta_gazebo bveeta_playground.launch
$: rosrun bveeta_control bveeta_teleop_key.py
```

## SLAM Bveeta Mini

For SLAM with Bveeta Mini, run these commands in different terminals:

```bash
$: roscore
$: roslaunch bveeta_gazebo bveeta_playground.launch
$: rosrun bveeta_control bveeta_teleop_key.py
$: roslaunch bveeta_firmware server_bringup.launch
$: roslaunch bveeta_slam bveeta_slam.launch
$: rosrun map_server map_saver -f my_map
```

## Navigation Bveeta Mini

For navigating Bveeta Mini, use the following commands:

```bash
$: roscore
$: roslaunch bveeta_gazebo bveeta_playground.launch
$: rosrun bveeta_control bveeta_teleop_key.py
$: roslaunch bveeta_firmware server_bringup.launch
$: roslaunch bveeta_navigation bveeta_navigation.launch
$: roslaunch bveeta_navigation bveeta_navigation.launch map_file:=my_map
```
