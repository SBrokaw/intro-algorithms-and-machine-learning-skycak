#!/usr/bin/env zsh

local script="ch3_7_hodgkin_huxley.py"

while fswatch -1 $script; do
    clear
    python $script
done
