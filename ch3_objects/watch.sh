#!/usr/bin/env zsh

while fswatch -1 ch3_4_tictactoe.py; do
    clear
    python ch3_4_tictactoe.py
done
