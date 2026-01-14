#!/usr/bin/env zsh

local script="ch4_4_regression_issues.py"

clear
python $script
while fswatch -1 $script; do
    clear
    python $script
done
