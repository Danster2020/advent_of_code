#!/bin/bash

echo -n "Year?: "
read -r year

echo -n "Day?: "
read -r day

target_dir="./$year/day$day"

# create dirs
mkdir -p "$target_dir"

# create files
touch $target_dir/task1.py
touch $target_dir/task2.py
touch $target_dir/puzzle.txt
touch $target_dir/puzzle_ex.txt