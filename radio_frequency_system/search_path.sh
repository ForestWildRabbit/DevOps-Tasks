#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 filename search_string"
  exit 1
fi

filename="$1"
key="$2"

# Check if the file exists
if [ ! -f "$filename" ]; then
  echo "Error: File '$filename' not found."
  exit 1
fi

value=$(grep "^$key:" "$filename" | awk -F: '{print $2}' | sed 's/^[ \t]*//')

if [ -z "$value" ]; then
  echo "Key '$key' not found in file."
else
  echo "$value"
fi