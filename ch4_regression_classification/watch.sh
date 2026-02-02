#!/usr/bin/env zsh

local script="ch4_5_regression_gradient_descent.py"

clear
python $script
while fswatch -1 $script; do
    clear
    python $script
done
