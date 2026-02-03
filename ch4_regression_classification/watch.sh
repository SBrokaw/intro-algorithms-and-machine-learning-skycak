#!/usr/bin/env zsh

local script="ch4_6_multiple_regression_interaction.py"

clear
python $script
while fswatch -1 $script; do
    clear
    python $script
done
