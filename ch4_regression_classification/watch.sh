#!/usr/bin/env zsh

local script="ch4_3_power_log_pseudoinverse.py"

while fswatch -1 $script; do
    clear
    python $script
done
