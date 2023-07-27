#!/bin/bash

# Change this to your directory
dir="."

# Counter
counter=1

# For each PNG file in the directory
for file in "$dir"/*.png
do
  # Rename the file
  mv -- "$file" "$dir"/image"$counter".png

  # Increment the counter
  ((counter++))
done

