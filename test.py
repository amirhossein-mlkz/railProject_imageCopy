import json
import os

# Specify the network path to the JSON file
json_path = r'\\192.168.43.99\rail_share\utils\config.json'

def read_json_from_network(path):
    try:
        # Check if the file exists
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                # Load JSON data
                data = json.load(f)
                return data
        else:
            print(f"File not found: {path}")
            return None
    except FileNotFoundError:
        print(f"File not found: {path}")
    except PermissionError:
        print(f"Permission denied: {path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return None

# Call the function and print the result
data = read_json_from_network(json_path)
if data is not None:
    print(data)
