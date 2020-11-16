#!/bin/bash
num_blocks=135
for ((c=0; c<num_blocks; c++))
do 
    configtxlator proto_decode --input block$c.block --type common.Block --output /Users/amazloomian/Desktop/guided\ research/data/$c.json
done
