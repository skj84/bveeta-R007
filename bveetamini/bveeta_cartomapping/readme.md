
# Installation Guide for Ceres Solver 1.14.0

## Step 1: Cloning the Repository
Clone the Ceres Solver repository:
```bash
git clone https://ceres-solver.googlesource.com/ceres-solver
```

## Step 2: Switching to Version 1.14.0
Switch to version 1.14.0:
```bash
cd ceres-solver
git checkout tags/1.14.0 -b version-1.14.0
```

## Step 3: Installing Dependencies
Install the necessary dependencies:
```bash
# CMake
sudo apt-get install cmake
# Google Log and Google Flags
sudo apt-get install libgoogle-glog-dev libgflags-dev
# BLAS & LAPACK (ATLAS)
sudo apt-get install libatlas-base-dev
# Eigen3
sudo apt-get install libeigen3-dev
# SuiteSparse (optional)
sudo apt-get install libsuitesparse-dev
```

## Step 4: Building Ceres Solver
Build Ceres Solver:
```bash
mkdir build
cd build
cmake ..
make -j
sudo make install
```

## Step 5: Verifying the Installation
Verify the installation by running test programs or checking the version.

## Additional Notes
- This guide is for Unix-like systems with `apt-get`.
- Steps may vary slightly based on the OS version or Linux distribution.
- Ensure your system is up to date before installation.
