#!/usr/bin/env zsh

local script="ch4_1_linear_polynomial_pseudoinverse.py"

while fswatch -1 $script; do
    clear
    python $script
done
