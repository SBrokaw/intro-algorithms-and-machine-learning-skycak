#!/usr/bin/env zsh

local script="ch3_6_SIR_model.py"

while fswatch -1 $script; do
    clear
    python $script
done
