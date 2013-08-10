#!/bin/bash

full_file="$1"
file_name=$(basename $full_file)
extension="${file_name##*.}"
echo "Extension:" $extension
file_name="${file_name%.*}"
echo "File Name:" $file_name