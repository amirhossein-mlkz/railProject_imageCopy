import os
import subprocess

def map_network(ip, share_path, username, password):
    # Construct the full path to the network share
    share_path = f'\\\\{ip}\\{share_path}'

    # Construct the command for mapping the network share
    if username and password:
        command = f'net use {share_path} /user:{username} {password}'
    else:
        command = f'net use {share_path}'

    try:
        # Execute the command to map the network share
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if 'completed successfully' in result.stdout:
            print(result.stdout)
            return True

        if 'error 85' in result.stderr:
            print('Error: A mapping already exists for this drive')
            return False

        print(result.stdout)
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False

def list_share_directory(share_path):
    try:
        # List the files and directories in the mapped network share
        files = os.listdir(share_path)
        print("Files and directories in the network share:")
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error listing directory contents: {e}")


if __name__=='__main__':

    # Example usage
    ip = '192.168.43.63'                    # IP address of the remote system
    share_path = 'test'                      # Shared folder on the remote system
    username = "MMM"                         # Your username
    password = "PHK"                         # Your password
    network_share = f'\\\\{ip}\\{share_path}'  # Full path to the network share

    # Map the network share
    if map_network(ip, share_path, username, password):
        # List the contents of the mapped network share
        list_share_directory(network_share)
