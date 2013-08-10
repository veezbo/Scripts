#!/bin/bash

#Grab the Full File Name
full_file="$1"


file_name=$(basename $full_file)
extension="${file_name##*.}"

#Output extension
echo "Extension:" $extension


file_name="${file_name%.*}"

#Output filename (without extension)
echo "File Name:" $file_name