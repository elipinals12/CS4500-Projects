import sys
from Other.directory_model import DirectoryModel
from Other.utils import Utils

if __name__ == "__main__":
    dm = DirectoryModel()
    while True:
        user_inputs = ""
        commands = []
        
        # Input loop, reading until valid commands are found
        while len(commands) < 1:
            try:
                # Read input, replace curly quotes, and strip whitespace
                stuff = input().strip()
                user_inputs += stuff 
                
                # Try extracting JSON commands
                commands.extend(Utils.extract_json_objects(user_inputs))
            except Exception as e:
                # Print out the error for debugging
                # print(f"Error extracting JSON: {e}")
                continue

        # Process each command
        for command in commands:
            if not command:
                continue
            
            try:
                if command == "query":
                    print(dm.get_tree())
                elif command == "quit":
                    sys.exit(0)
                elif isinstance(command, dict):
                    if "path" in command and "size" in command:
                        dm.add_to_tree(command['path'], command['size'])
                    elif "path" in command and "subs" in command:
                        dm.add_to_tree(command['path'], command)
                    else:
                        print("Invalid command format.")
                else:
                    print("Unknown command format.")
            
            # Catch any exceptions raised during processing
            except Exception as e:
                # print(f"Error processing command: {e}")
                continue