import socket
import ipaddress
import subprocess

def get_local_ip_and_subnet():
    """Get the local IP address and subnet mask."""
    try:
        # Get the local IP address of the primary network interface
        local_ip = socket.gethostbyname(socket.gethostname())
        
        # Use 'ipconfig' or 'ifconfig' to get the subnet mask
        if subprocess.run(["ipconfig"], capture_output=True).returncode == 0:
            # Windows
            output = subprocess.check_output("ipconfig", text=True)
        else:
            # Linux/macOS
            output = subprocess.check_output("ifconfig", text=True)
        
        # Parse the output for the subnet mask corresponding to the local IP
        for line in output.splitlines():
            if local_ip in line:
                # Get the next line for subnet mask
                idx = output.splitlines().index(line) + 1
                while idx < len(output.splitlines()):
                    if "Subnet Mask" in output.splitlines()[idx]:
                        # Extract the subnet mask
                        subnet_mask = output.splitlines()[idx].split(":")[-1].strip()
                        return local_ip, subnet_mask
                    idx +=1 
    except Exception as e:
        print("Couldn’t process local")

        
def is_ip_in_same_subnet(local_ip, subnet_mask, remote_ip):
    """Check if the remote IP is in the same subnet as the local IP."""
    local_network = ipaddress.ip_network(f"{local_ip}/{subnet_mask}", strict=False)
    remote_address = ipaddress.ip_address(remote_ip)
    return remote_address in local_network






def check_ip(remote_ip):


    try:
        # Get local IP and subnet
        local_ip, subnet_mask = get_local_ip_and_subnet()
        print(f"Local IP: {local_ip}")
        print(f"Subnet Mask: {subnet_mask}")
        # Check if remote IP is in the same subnet

        if remote_ip == local_ip:
            msg = f"Two IP Are Same,Change System IP"
            print(msg)
            return False,msg


        elif is_ip_in_same_subnet(local_ip, subnet_mask, remote_ip):
            print(f"The remote IP {remote_ip} is in the same subnet as your local IP {local_ip}.")

            return True,""


        else:
            print(f"The remote IP {remote_ip} is NOT in the same subnet as your local IP {local_ip}.")

            return False , "Remote IP is Not in Netwrk Range"

    except RuntimeError as e:
        print(f"Error: {e}")
        return False , str(e)
    except ValueError as e:
        print(f"Invalid IP or subnet mask: {e}")

        return False , "Invalid IP or Subnetmask"












if __name__ == "__main__":


        # Input remote IP
        # remote_ip = input("Enter the remote IP to check: ").strip()

        remote_ip = '192.168.151.51'

        ret , msg = check_ip(remote_ip=remote_ip)

        print(ret , msg)