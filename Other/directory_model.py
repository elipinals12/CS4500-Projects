import json

class DirectoryModel(object):
    def __init__(self):
        self.directory_tree = {}

    def add_to_tree(self,path,entry):
        parts = path.strip('/').split('/')
        current = self.directory_tree
        for part in parts[:-1]:  # Traverse to the target directory
            if part not in current or not isinstance(current[part], dict):
                return  # Ignore invalid paths
            current = current[part]
        # Add sub-directory or file
        if isinstance(entry, dict):  # If entry is a sub-directory structure
            for sub in entry['subs']:
                if sub.isalpha():
                    current[sub] = {}
        elif isinstance(entry, int):  # If entry is a file with size
            current[parts[-1]] = entry

    def get_tree(self):
        return json.dumps(self.directory_tree, separators=(',', ':'))