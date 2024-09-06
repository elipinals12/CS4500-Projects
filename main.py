import sys
import json
from Other.directory_model import DirectoryModel
from Other.utils import Utils
if __name__ == "__main__":
    dm = DirectoryModel()
    while True:
            user_inputs = input().strip()
            commands = Utils.extract_json_objects(user_inputs)
            for command in commands:
                if not command:
                    continue
                try:
                    # command = json.loads(user_input.strip())
                    if command == "query":
                        print(dm.get_tree())
                    elif command == "quit":
                        sys.exit(0)
                    elif isinstance(command, dict):
                        if "path" in command and "size" in command:
                            dm.add_to_tree(command['path'], command['size'])
                        elif "path" in command and "subs" in command:
                            dm.add_to_tree(command['path'], command)
                except Exception as e:
                    print(str(e))