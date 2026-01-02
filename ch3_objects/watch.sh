#!/usr/bin/env zsh

local script="ch3_8_hash_tables.py"

while fswatch -1 $script; do
    clear
    python $script
done
