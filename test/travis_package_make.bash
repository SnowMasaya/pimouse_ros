#!/bin/bash -xve

sudo rsync -av ./ ~/catkin_ws/src/pimouse_ros/
cd ~/catkin_ws
sudo catkin_make
