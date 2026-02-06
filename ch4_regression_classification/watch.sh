#!/usr/bin/env zsh

local script="ch4_8_naive_bayes.py"

clear
python $script
while fswatch -1 $script; do
    clear
    python $script
done
