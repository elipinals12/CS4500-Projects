import json
import math

class DirectoryModel(object):
    def __init__(self):
        # Initialize an empty dictionary to represent the directory tree
        self.directory_tree = {}

    def add_to_tree(self, path, entry):
<<<<<<< HEAD
        parts = path.strip('/').split('/')
        current = self.directory_tree
        
        # Traverse the tree to the second-to-last directory
        for part in parts[:-1]:
            if part not in current or not isinstance(current[part], dict):
                return  # Return without modifying the tree if any part of the path doesn't exist
            current = current[part]  # Move into the directory

        # Add sub-directory or file at the correct level (the last directory in the path)
        if isinstance(entry, dict) and "subs" in entry:
            ordered_subs = sorted(entry["subs"])  # Sort sub-directories
            last_directory = parts[-1]
            current = current if last_directory == "" else current[last_directory]
            legal = 0 != math.prod([sub not in current.keys() for sub in ordered_subs])
            if legal:
                for sub in ordered_subs:
                    if sub.isalpha():  # Validate sub-directory names
                        current[sub] = {}
        elif isinstance(entry, int):  # Handle files with size
            current[parts[-1]] = entry  # Add the file with size in the correct directory
=======
        # Split the path into parts and remove leading/trailing slashes
        parts = path.strip('/').split('/')
        current = self.directory_tree
        
        # Traverse to the target directory
        for part in parts[:-1]:
            if part not in current or not isinstance(current[part], dict):
                return  # Ignore invalid paths
            current = current[part]
        
        # Add sub-directory or file to the directory tree
        if isinstance(entry, dict):  # If entry is a sub-directory structure
            for sub in entry['subs']:
                if sub.isalpha():  # Ensure sub-directory names are alphabetic
                    current[sub] = {}
        elif isinstance(entry, int):  # If entry is a file with size
            current[parts[-1]] = entry
>>>>>>> 37374b269942a68fcefc04e5f502b58bfd933fc7

    def get_tree(self):
        # Return the directory tree as a JSON string
        return json.dumps(self.directory_tree, separators=(',', ':'))