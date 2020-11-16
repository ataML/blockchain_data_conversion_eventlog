#!/bin/bash
num_blocks=135
for ((c=0; c<num_blocks; c++))
do
    peer channel fetch $c block$c.block -c mychannel 
done
