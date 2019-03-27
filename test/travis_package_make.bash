#!/bin/bash -xve

rsync -av ./ ~/catkin_ws/src/pimouse_ros/
export PYTHONPATH="${PYTHONPATH}:~/catkin_ws/src/pimouse_ros"
cd ~/catkin_ws
catkin_make
