#!/usr/bin/env zsh

local script="ch4_3_power_log_pseudoinverse.py"

clear
python $script
while fswatch -1 $script; do
    clear
    python $script
done
