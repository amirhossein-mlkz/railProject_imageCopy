import paramiko
from datetime import datetime

# Configuration
remote_host = "192.168.43.63"  # Replace with the remote machine's IP address
remote_user = "MMM"        # Username for the remote machine
remote_pass = "PHK"        # Password for the remote machine

# Get the local time
local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(remote_host, username=remote_user, password=remote_pass)

# Get the current remote time
stdin, stdout, stderr = ssh.exec_command("date '+%Y-%m-%d %H:%M:%S'")
remote_time = stdout.read().decode().strip()

# Compare and update the time if necessary
if remote_time != local_time:
    print(f"Remote time is not synchronized. Updating time on {remote_host}...")
    
    # Command to set the new time on the remote machine
    command = f"sudo date -s '{local_time}'"
    ssh.exec_command(command)
    print(f"Time on {remote_host} updated to {local_time}.")
else:
    print("Remote time is already synchronized.")

# Close the SSH connection
ssh.close()
