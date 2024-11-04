import subprocess
from datetime import datetime
import time
import json

from persiantools import jdatetime

class timeSetting:

    @staticmethod
    def get_time_from_remote_system(ip_address) -> tuple[datetime, datetime]:
        result = subprocess.run(["net", "time", f"\\\\{ip_address}"], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error:", result.stderr)
            return None, None
        
        # Extract time from stdout
        # Assuming the output format is: "Current time at \\[ip_address] is [time]"
        for line in result.stdout.splitlines():
            if "is" in line :
                # Example line: "Current time at \\192.168.1.60 is 11/4/2024 12:34 PM"
                try:
                    remote_time_str = line.split("is")[-1].strip()
                    # Convert to datetime object
                    remote_time = datetime.strptime(remote_time_str, "%m/%d/%Y %I:%M:%S %p")
                    # Get current local time
                    local_time = datetime.now()
                    return remote_time, local_time
                except ValueError:
                    print("Could not parse the date format.")
                    return None, None

    @staticmethod
    def sync_time(remote_ip: str, time: datetime):
        """تنظیم زمان سیستم متصل"""
        # فرمت زمان به شکل ISO 8601
        local_time_str = time.strftime('%Y-%m-%dT%H:%M:%S')  # استفاده از T بین تاریخ و زمان
        command = f'w32tm /set /computer:{remote_ip} /set:{local_time_str} /force'

        try:
            # اجرای دستور و ضبط خروجی
            result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
            return True, None  # موفقیت
        except subprocess.CalledProcessError as e:
            # در صورت خطا، جزئیات خطا را بازگشت می‌دهیم
            return False, f"Error {e.returncode}: {e.stderr if e.stderr else 'No output'}"
        
    @staticmethod
    def get_timezone():
        # Display timezone name and offset
        timezone_name = time.tzname[0] if time.localtime().tm_isdst == 0 else time.tzname[1]
        return timezone_name
    
    @staticmethod
    def save_time_setting( path, local_time:datetime, remote_time:datetime, ):
        local_timezone:str = timeSetting.get_timezone()
        local_time_str = local_time.strftime('%Y-%m-%d_%H-%M-%S')
        remote_time_str = remote_time.strftime('%Y-%m-%d_%H-%M-%S')
        setting = {}
        setting['src'] = remote_time_str
        setting['dst'] = local_time_str
        setting['timezone']=  local_timezone
        try:
            with open(path, 'w', encoding='utf-8') as json_file:
                json.dump(setting, json_file, ensure_ascii=False, indent=4)
                return True
        except:
            return False
        return False

