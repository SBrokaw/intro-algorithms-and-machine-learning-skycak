#!/usr/bin/env zsh

while fswatch -1 ch3_2_rref.py; do
    clear
    python3 ch3_2_rref.py
done
