#!/usr/bin/env zsh

local script="ch4_6_k_nearest_neighbors.py"

clear
python $script
while fswatch -1 $script; do
    clear
    python $script
done
