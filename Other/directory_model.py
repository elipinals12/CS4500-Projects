import json
import math

class DirectoryModel(object):
    def __init__(self):
        self.directory_tree = {}

    def add_to_tree(self, path, entry):
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

    def get_tree(self):
        return json.dumps(self.directory_tree, separators=(',', ':'))