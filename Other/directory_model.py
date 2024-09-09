import json

class DirectoryModel(object):
    def __init__(self):
        # Initialize an empty dictionary to represent the directory tree
        self.directory_tree = {}

    def add_to_tree(self, path, entry):
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

    def get_tree(self):
        # Return the directory tree as a JSON string
        return json.dumps(self.directory_tree, separators=(',', ':'))