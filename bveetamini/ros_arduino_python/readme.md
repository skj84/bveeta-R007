
# ROS Installation Guide

This guide provides instructions for installing the Robot Operating System (ROS) on Ubuntu.

## Prerequisites

- Ubuntu (recommended versions: 20.04, 18.04, or 22.04)
- Internet connection
- Administrator (sudo) access

## Step 1: Configure Ubuntu Repositories

Ensure your Ubuntu repositories are configured to allow "restricted," "universe," and "multiverse." You can do this from the Software & Updates app in Ubuntu.

## Step 2: Setup Your Sources List

Set up your computer to accept software from ROS.org. Open a terminal and enter:

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

## Step 3: Set Up Your Keys

```bash
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

## Step 4: Installation

First, make sure your Debian package index is up to date:

```bash
sudo apt update
```

Then, install the full ROS package:

```bash
sudo apt install ros-noetic-full-desktop
```

## Step 5: Environment Setup

Add ROS environment variables to your bash session:

```bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## Step 6: Dependencies for Building Packages

Install dependencies for building ROS packages:

```bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

Initialize rosdep:

```bash
sudo rosdep init
rosdep update
```

## Conclusion

You have now successfully installed ROS on your Ubuntu system. To start using ROS, you can begin by learning how to create and manage your ROS workspaces and packages.

For more detailed instructions and troubleshooting, visit the [official ROS installation page](http://wiki.ros.org/noetic/Installation/Ubuntu).
