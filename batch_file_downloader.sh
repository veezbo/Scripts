#!/bin/bash

#Automatic Downloader of Links in a File (only http links though)

readonly FILE="$1"
readonly DIR="$2"

while read -r line; do
	string=$line
	for word in $string; do
		if [[ $word  =~ ^http.* ]]; then
			URL=$word
			wget --spider $URL && wget -P $DIR $URL
		fi
	done	
done < "$FILE"