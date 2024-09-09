#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi

# Run the Python script
python3 main.py

# Check if the Python script ran successfully
if [ $? -eq 0 ]; then
    echo "Python script ran successfully."
else
    echo "Python script failed to run."
    exit 1
fi
