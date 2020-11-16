#!/bin/bash
for ((c=0; c<132; c++))
do 
    configtxlator proto_decode --input block$c.block --type common.Block --output /Users/amazloomian/Desktop/guided\ research/data/$c.json
done
