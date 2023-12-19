# Installation Guide for Cartographer on ROS Noetic

  

## Dependencies

First, install the necessary ROS Noetic dependencies:

```bash

sudo  apt-get  install  ros-noetic-map-server  ros-noetic-move-base  ros-noetic-navigation  ros-noetic-dwa-local-planner  ros-noetic-ira-laser-tools  ros-noetic-teleop-twist-keyboard

```

  

## Building & Installation

For building Cartographer ROS, use wstool, rosdep, and Ninja for faster builds.

  

### On Ubuntu Focal with ROS Noetic

Install the required tools:

```bash

sudo  apt-get  update

sudo  apt-get  install  -y  python3-wstool  python3-rosdep  ninja-build  stow

```

  

### Create a New Cartographer ROS Workspace

Create a new workspace 'carto_ws' inside your existing 'catkin_ws':

```bash

mkdir  -p  ~/catkin_ws/carto_ws

cd  ~/catkin_ws/carto_ws

wstool  init  src

wstool  merge  -t  src  https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall

wstool  update  -t  src

```

  

### Clone Additional Repositories

Clone necessary repositories:

```bash

cd  ~/catkin_ws/carto_ws/src

git  clone  -b  melodic-devel  https://github.com/ros-perception/perception_pcl.git

git  clone  https://github.com/ros-perception/pcl_msgs

git  clone  -b  noetic-devel  https://github.com/jsk-ros-pkg/geometry2_python3.git

```

  

### Install Dependencies with rosdep

From the 'carto_ws' directory:

```bash

cd  ~/catkin_ws/carto_ws

rosdep  install  --from-paths  src  --ignore-src  --rosdistro=${ROS_DISTRO}  -y

src/cartographer/scripts/install_abseil.sh

```

  

# Installation Guide for Ceres Solver 1.14.0

  

## Step 1: Cloning the Repository

Clone the Ceres Solver repository:

```bash

git  clone  https://ceres-solver.googlesource.com/ceres-solver

```

  

## Step 2: Switching to Version 1.14.0

Switch to version 1.14.0:

```bash

cd  ceres-solver

git  checkout  tags/1.14.0  -b  version-1.14.0

```

  

## Step 3: Installing Dependencies

Install the necessary dependencies:

```bash

# CMake

sudo  apt-get  install  cmake

# Google Log and Google Flags

sudo  apt-get  install  libgoogle-glog-dev  libgflags-dev

# BLAS & LAPACK (ATLAS)

sudo  apt-get  install  libatlas-base-dev

# Eigen3

sudo  apt-get  install  libeigen3-dev

# SuiteSparse (optional)

sudo  apt-get  install  libsuitesparse-dev

```

  

## Step 4: Building Ceres Solver

Build Ceres Solver:

```bash

mkdir  build

cd  build

cmake  ..

make  -j

sudo  make  install

```

  

## Step 5: Verifying the Installation

Verify the installation by running test programs or checking the version.

  

## Additional Notes

- This guide is for Unix-like systems with `apt-get`.

- Steps may vary slightly based on the OS version or Linux distribution.

- Ensure your system is up to date before installation.


### Build with catkin_make_isolated

After installing Ceres Solver:

```bash

cd  ~/catkin_ws/carto_ws

catkin_make_isolated  --install  --use-ninja  -j4  -l4

```

  

### Source the Workspaces

Overlay the workspaces as per the ROS workspace overlaying guidelines:

  

1. First, source the carto_ws:

```bash

source ~/catkin_ws/carto_ws/devel/setup.bash

```

  

2. Delete the 'devel' and 'build' folders from 'catkin_ws', rebuild, and source the main 'catkin_ws':

```bash

cd ~/catkin_ws

rm -rf devel build

catkin_make

source devel/setup.bash

```
