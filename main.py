import sys
from Other.directory_model import DirectoryModel
from Other.utils import Utils

if __name__ == "__main__":
    # Initialize the DirectoryModel instance
    dm = DirectoryModel()
    
    # Infinite loop to continuously read user input
    while True:
        user_inputs = ""
        commands = []
        
        # Input loop, reading until valid commands are found
        while len(commands) < 1:
            try:
                # Read input from the user, replace curly quotes, and strip whitespace
                stuff = input().strip()
                user_inputs += stuff 
                
                # Try extracting JSON commands from the user input
                commands.extend(Utils.extract_json_objects(user_inputs))
            except Exception as e:
                # Print out the error for debugging (commented out)
                # print(f"Error extracting JSON: {e}")
                continue

        # Process each command extracted from the user input
        for command in commands:
            if not command:
                continue
            
            try:
                # Handle the "query" command to print the directory tree
                if command == "query":
                    print(dm.get_tree())
                # Handle the "quit" command to exit the program
                elif command == "quit":
                    sys.exit(0)
                # Handle dictionary commands to add to the directory tree
                elif isinstance(command, dict):
                    # Add to the tree if the command contains "path" and "size"
                    if "path" in command and "size" in command:
                        dm.add_to_tree(command['path'], command['size'])
                    # Add to the tree if the command contains "path" and "subs"
                    elif "path" in command and "subs" in command:
                        dm.add_to_tree(command['path'], command)
                    else:
                        print("Invalid command format.")
                else:
                    print("Unknown command format.")
            
            # Catch any exceptions raised during command processing
            except Exception as e:
                # Print out the error for debugging (commented out)
                # print(f"Error processing command: {e}")
                continue