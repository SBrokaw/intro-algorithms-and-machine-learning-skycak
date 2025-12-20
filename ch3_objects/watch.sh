#!/usr/bin/env zsh

while fswatch -1 ch3_5_euler_estimation.py; do
    clear
    python ch3_5_euler_estimation.py
done
