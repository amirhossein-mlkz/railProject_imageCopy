import platform
import subprocess
import os

from PySide6.QtCore import Signal, QObject
import win32net #pip install pywin32
import win32netcon
import win32security

from Tranform.sharingConstans import StatusCodes



class Sharing:

    @staticmethod
    def create_and_share_folder(folder_path, share_name, description="", permissions=None):
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Define the share info
        share_info = {
            'netname': share_name,
            'type': win32netcon.STYPE_DISKTREE,
            'remark': description,
            'permissions': 0,
            'max_uses': -1,
            'current_uses': 0,
            'path': folder_path,
            'passwd': ''
        }
        
        # Add the share
        win32net.NetShareAdd(None, 2, share_info)
        
        # Set folder permissions
        if permissions:
            Sharing.set_folder_permissions(folder_path, permissions)

    @staticmethod
    def remove_share(share_name):
        try:
            # Remove the share
            win32net.NetShareDel(None, share_name)
            print(f"Share '{share_name}' removed successfully.")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def set_folder_permissions(folder_path, permissions):
        
        
        # Get the security descriptor for the folder
        sd = win32security.GetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION)
        dacl = sd.GetSecurityDescriptorDacl()
        
        # Add the specified permissions
        for user, access in permissions.items():
            user, domain, type = win32security.LookupAccountName("", user)
            dacl.AddAccessAllowedAce(win32security.ACL_REVISION, access, user)
        
        # Set the new DACL
        sd.SetSecurityDescriptorDacl(1, dacl, 0)
        win32security.SetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION, sd)

#--------------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------------

class pingWorker(QObject):
    result_signal = Signal(int)

    def __init__(self, ip) -> None:
        super().__init__()
        self.ip = ip
    
    def run(self,):
        res,msg = self.__get_ping(self.ip)
        if not res:
            self.result_signal.emit(StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT,msg)
            return
        else:

            self.result_signal.emit(StatusCodes.pingAndConnectionStatusCodes.SUCCESS,msg)

    def __get_ping(self, ip):
        if platform.system().lower() == "windows":
            param = "-n"
        else:
            param = "-c"
        
        try:
            # اجرای دستور پینگ
            output = subprocess.run(["ping", param, "1", ip], capture_output=True, text=True, timeout=4)
            
            # بررسی returncode
            if 'ttl' in output.stdout.lower():
                return True, ''
            else:
                return False,''

        except Exception as e:
            print(f"An error occurred: {e}")
            return False,''
        


#--------------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------------


class pingAndCreateWorker(QObject):
    result_signal = Signal(int,str)

    def __init__(self, ip:str,src_path:str,username:str,password:str) -> None:
        super().__init__()
        self.ip = ip
        self.src_path=src_path
        self.username=username
        self.password=password
    
    def run(self,):
        res,msg = self.__get_ping(self.ip)
        if not res:
            self.result_signal.emit(StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT,msg)
            return
        else:
            ret,msg = self.create_connection()
            if ret:
                self.result_signal.emit(StatusCodes.pingAndConnectionStatusCodes.SUCCESS,msg)
            else:
                self.result_signal.emit(StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT,msg)

    def __get_ping(self, ip):
        if platform.system().lower() == "windows":
            param = "-n"
        else:
            param = "-c"
        
        try:
            # اجرای دستور پینگ
            output = subprocess.run(["ping", param, "1", ip], capture_output=True, text=True, timeout=4)
            
            # بررسی returncode
            if 'ttl' in output.stdout.lower():
                msg = 'Ping Succussfully'
                return True,msg
            else:
                msg = 'Ping Error'
                return False,msg

        except Exception as e:
            print(f"An error occurred: {e}")
            return False,e
        




    def create_connection(self):


        # Construct the command for mapping the network share
        if self.username and self.password:
            #command = f'net use {self.src_path} /user:{self.username} {self.password}'
            command = ["net", "use", self.src_path, f"/user:{self.username}", self.password]
        else:
            #command = f'net use {self.src_path}'
            command = ["net", "use", self.src_path]

        try:
            # Execute the command to map the network share
            result = subprocess.run(command, capture_output=True, text=True, timeout=4)
            if 'completed successfully' in result.stdout:
                msg = 'connection completed successfully'
                return True,msg

            elif 'error 85' in result.stderr:
                msg = 'Error: A mapping already exists for this drive'
                print(msg)
                return False,msg
            elif 'error 53' in result.stderr:
                msg = 'Error: The network path was not found'
                print(msg)
                return False,msg
   
            return False, 'Error : Failed Create Connection, Username Or Password Maybe Wrong'

        except Exception as e:
            print(f"Error: {e}")
            return False, f'Error : Failed Create Connection, Username Or Password Maybe Wrong {e}'



class shareMapping(QObject):

    def __init__(self, username, password, drive_letter, ) -> None:
        super().__init__()

    def map_network_drive(self):
        command = f'net use {self.drive_letter} {self.network_path} /user:{self.username} {self.password}'
        os.system(command)

    def disconnect_network_drive(self):
        os.system(f'net use {self.drive_letter} /delete')

    def  is_drive_mapped(self):
        try:
            output = subprocess.check_output(f'net use {self.drive_letter}', shell=True, stderr=subprocess.STDOUT).decode()
            return self.network_path in output
        except subprocess.CalledProcessError:
            return False
        
    
    def get_mapped_drives(self,):
        try:
            output = subprocess.check_output('net use', shell=True).decode() 
            
            lines = output.splitlines()
            all_drives = []

            for line in lines:
                if (   line.lower().startswith("ok") 
                    or line.lower().startswith("unavailable") 
                    or line.lower().startswith("disconnected")
                    ):
                    parts = line.split()
                    if len(parts) >= 3:
                        drive_letter = parts[1]
                        network_path = parts[2]
                        available = False
                        connect = False
                        if parts[0].lower() == 'ok':
                            available = True
                            connect = True
                        elif parts[0].lower() == 'unavailable':
                            available = False
                            connect = False

                        elif parts[0].lower() == 'disconnected':
                            available = True
                            connect = False

                        all_drives.append({
                            "drive_letter": drive_letter,
                            "network_path": network_path,
                            "available": available,
                            'connect': connect,
                        })


        except subprocess.CalledProcessError as e:
            print("خطا در اجرای دستور 'net use':", e)
        
        finally:
            return all_drives
    
    def check_drived_is_mapped(self, ip:str):
        drives = self.get_mapped_drives()
        for drive in drives:
            if ip in drive['network_path']:
                return drive
        return None
    
    def map_network(self, ip, share_path, username, password, drive_letter='Z:'):
        share_path = f'\\\\{ip}\\{share_path}'

        if username and password:
            command = f'net use {drive_letter} {share_path} /user:{username} {password}'
        else:
            command = f'net use {drive_letter} {share_path}'

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if 'completed successfully' in result.stdout:
                return True
            
            if 'error 85' in result.stderr:
                print('Error: map exist drive')
                return False
            return False
        
        except Exception as e:
            print(f"error: {e}")
            return False