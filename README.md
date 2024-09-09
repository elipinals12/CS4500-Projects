# Project Overview

This project manages and processes JSON files representing directory structures. It includes scripts for handling JSON data, querying paths, and updating sizes.

## Files

- **`main.py`**: Runs the process. Handles input/output with JSON files and coordinates tasks between the other scripts.
- **`directory_model.py`**: Manages JSON directory structure. Helps navigate and query paths within the JSON.
- **`utils.py`**: Provides helper functions for JSON parsing and manipulation.
- **`xjson.bash`**: A Bash script for running JSON operations from the command line.

## How to Run

### Python
1. Use `main.py`:
   python main.py

### Bash
1. Use `xjson.bash`:
   bash xjson.bash < <input_file>

## Relationships

- `main.py` coordinates between the directory model (`directory_model.py`) and utilities (`utils.py`).
- `xjson.bash` offers an alternative way to run the same operations via the shell.