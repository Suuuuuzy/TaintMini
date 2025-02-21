#!/bin/bash

# Output file where the paths will be written
output_file="minitracker_benchmark.txt"

# Clear the output file if it already exists
> "$output_file"

# Walk through the directory and find all directories containing app.json
find /media/dataj/wechat-devtools-linux/prework/MiniTracker/Benchmark -type f -name "app.json" -exec dirname {} \; | while read dir; do
  # Get the absolute path of the directory and append it to the output file
  realpath "$dir" >> "$output_file"
done