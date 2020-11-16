#!/bin/bash
for ((c=0; c<132; c++))
do
    peer channel fetch $c block$c.block -c mychannel 
done
