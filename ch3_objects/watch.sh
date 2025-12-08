#!/usr/bin/env zsh

while fswatch -1 ch3_3_k_means_clustering.py; do
    clear
    python ch3_3_k_means_clustering.py
done
