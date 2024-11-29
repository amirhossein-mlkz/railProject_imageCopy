import ctypes
import subprocess

def run_as_admin(command):
    """Run a command as an administrator."""
    try:
        # Use ctypes to request admin privileges for the subprocess
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", "powershell", f"-Command {command}", None, 1
        )
        print(f"Command executed with admin privileges: {command}")
    except Exception as e:
        print(f"Failed to run command as admin: {e}")

# Example usage
if __name__ == "__main__":
    # Command to share a folder
    folder_path = r"C:\Users\Public\TestFolder"
    share_name = "TestShare"
    command = f'net share {share_name}="{folder_path}" /GRANT:Everyone,FULL /REMARK:"Shared Folder"'
    
    run_as_admin(command)
