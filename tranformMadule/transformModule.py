import subprocess
import platform
import time
import os
import threading

from persiantools.jdatetime import JalaliDateTime, timedelta
from PySide6.QtCore import Signal, QObject


class FILE_STRUCT:
    TRAIN = 'train'
    CAMERA = 'camera'
    YEAR = 'year'
    MONTH = 'month'
    DAY = 'day'
    HOUR = 'hour'
    MINUTE = 'minute'
    FILE = 'file'

DIRECTORY_TREE = [FILE_STRUCT.TRAIN, 
                  FILE_STRUCT.CAMERA, 
                  FILE_STRUCT.YEAR,
                  FILE_STRUCT.MONTH,
                  FILE_STRUCT.DAY,
                  FILE_STRUCT.HOUR,
                  FILE_STRUCT.MINUTE,
                  FILE_STRUCT.FILE
                ]

DIRECTORY_TREE = [FILE_STRUCT.TRAIN, 
                  FILE_STRUCT.CAMERA, 
                  FILE_STRUCT.FILE
                ]


class transformModule:
    def __init__(self, ip:str, src_path:str, dst_path:str) -> None:
        self.ip = ip
        self.src_path = src_path
        self.dst_path = dst_path
        self.ping_thread = None
        self.ping_worker = None

        self.searcher_thread = None
        self.searcher_worker = None
        
    
    def check_connection(self, respone_callback):
        self.ping_worker = pingWorker(self.ip)
        self.ping_worker.result_signal.connect(respone_callback)
        self.ping_thread = threading.Thread(target=self.ping_worker.run)
        self.ping_thread.start()

    def start_transition(self, msg_callback, trains=None, dates_range=None):
        if not os.path.exists(self.src_path):
            return
        
        self.searcher_worker = filesFinderWorker(self.src_path,
                                                 trains=trains,
                                                 date_ranges=dates_range,
                                                 struct=DIRECTORY_TREE)
        self.searcher_worker.log_signal.connect(msg_callback)
        self.searcher_worker.finish_singal.connect(self.files_list_ready)
        self.searcher_thread = threading.Thread( target=self.searcher_worker.run, daemon=True )
        self.searcher_thread.start()
        
    def files_list_ready(self, paths:list[str], sizes:list[int]):
        print('finish')

class transormUtils:

    @staticmethod
    def extract_file_name_info(name:str) -> tuple[JalaliDateTime, str, str]:
        date, clock, train_id, camera_name = name.split('_')
        dc_str = date + '_' + clock
        dt = JalaliDateTime.strptime(dc_str,'%Y-%m-%d_%H-%M-%S-%f')
        return dt, train_id, camera_name

    @staticmethod
    def last_day_of_month(year, month):
        if month == 12:
            next_month = JalaliDateTime(year+1, 1, 1)
        else:
            next_month = JalaliDateTime(year, month+1, 1)
        last_day_of_month:JalaliDateTime = next_month - timedelta(days=1)
        return last_day_of_month.day


class filesFinderWorker(QObject):
    finish_singal = Signal(dict)
    log_signal = Signal(str)

    def __init__(self,
                 main_path:str, 
                 struct:list[str],
                 trains:list[str] = None, 
                 date_ranges:tuple[JalaliDateTime] = None,
                 gap_step_sec=600) -> None:
        super().__init__()    
        self.trains = trains
        self.date_ranges = date_ranges
        self.temp_date_ranges = date_ranges[0], date_ranges[1]
        self.main_path = main_path
        self.struct = struct





class filesFilterWorker(QObject):
    finish_singal = Signal(list, list)
    log_signal = Signal(str)
    def __init__(self, 
                 main_path:str, 
                 struct:list[str],
                 trains:list[str] = None, 
                 date_ranges:tuple[JalaliDateTime] = None,) -> None:
        super().__init__()    
        self.trains = trains
        self.date_ranges = date_ranges
        self.temp_date_ranges = date_ranges[0], date_ranges[1]
        self.main_path = main_path
        self.struct = struct

        #choose filter trains by folder name or by directory name
        # self.check_train_by_filename = True
        # if FILE_STRUCT.TRAIN in self.struct:
        #     self.check_train_by_filename = False


    def __init_flags(self,):
        self.is_train_checked = False
        self.is_year_checked = False
        self.is_month_checked = False
        self.is_day_checked = False
        self.is_hour_checked = False
        self.is_minute_checked = False
  

    def run(self, ):
        self.__init_flags()
        self.res_paths = []
        self.res_sizes = []
        self.total_size = 0
        self.searcher(self.main_path, pos_index=0)
        self.finish_singal.emit( self.res_paths, self.res_sizes)

    def __sort_number_folder(self, names:list[str]):
        def key_func(x:str):
            if x.isdigit():
                return int(x)
            else:
                return 10*6
        
        names.sort(key=key_func)
        return names

    def searcher(self, path, pos_index, date=None):
        #pos_index show we are in which level of directory
        if pos_index >= len(self.struct):
            return
        

        step_name = self.struct[pos_index]
        subs = os.listdir(path)
        if step_name in [FILE_STRUCT.YEAR,FILE_STRUCT.MONTH,FILE_STRUCT.DAY,FILE_STRUCT.HOUR,FILE_STRUCT.MINUTE]:
            subs = self.__sort_number_folder(subs)

        for sub in subs:
            sub_path = os.path.join(path, sub)
            #check if we arent in last level of tree
            if pos_index != (len(self.struct) -1):
                if not os.path.isdir(sub_path):
                    continue
            else:
                if not os.path.isfile(sub_path):
                    continue
            #-----------------------------------
            flag, date = self.check_filters(sub, step_name, date)
            if flag:
                if pos_index == (len(self.struct) -1):
                    size = os.path.getsize(sub_path)
                    self.res_paths.append(sub_path)
                    self.res_sizes.append(size)
                    self.total_size += size
                    self.log_signal.emit(f'Size f{int(self.total_size)}')
                else:
                    self.searcher(sub_path, pos_index+1, date)
                    
                
            
    

    def check_filters(self, sub:str, step_name:str, date:JalaliDateTime):
        if step_name == FILE_STRUCT.TRAIN:
            self.is_train_checked = True
            if self.trains is None:
                return True, date
            if sub in self.trains:
                return True, date
            return False, date
        #------------------------------check year------------------------- 
        elif step_name == FILE_STRUCT.YEAR:
            self.is_year_checked = True
            if self.date_ranges is None:
                return True, date
            if not sub.isdigit():
                return False, date
            year = int(sub)
            if self.date_ranges[0].year <= year <= self.date_ranges[1].year:
                date = JalaliDateTime(year,month=1,day=1)
                start_date = JalaliDateTime(self.date_ranges[0].year,month=1,day=1, hour=0,minute=0)
                last_day =  transormUtils.last_day_of_month(self.date_ranges[1].year, 12)
                end_date = JalaliDateTime(self.date_ranges[1].year,month=12,day=last_day, hour=23, minute=59)
                self.temp_date_ranges = (start_date, end_date)
                return True, date
            else:
                return False, date
        #------------------------------check month-------------------------
        elif step_name == FILE_STRUCT.MONTH:
            #we coudnt check month if year dose not check befor
            if not( self.is_year_checked):
                return True, date
            
            self.is_month_checked = True
            if self.date_ranges is None:
                return True, date
            if not sub.isdigit():
                return False, date
            
            month = int(sub)
            date = date.replace(month=month)
            last_day =  transormUtils.last_day_of_month(self.date_ranges[1].year, self.date_ranges[1].month)
            start_date = self.temp_date_ranges[0].replace( month=self.date_ranges[0].month, day=1, hour=0, minute=0)
            end_date = self.temp_date_ranges[1].replace( month=self.date_ranges[1].month, day=last_day, hour=23, minute=59)
            self.temp_date_ranges = start_date, end_date
            if self.temp_date_ranges[0] <= date <= self.temp_date_ranges[1]:                
                return True, date
            else:
                return False, date
        
        #------------------------------check day-------------------------
        elif step_name == FILE_STRUCT.DAY:
            #we coudnt check day if year and month dose not check befor
            if not( self.is_year_checked and
                    self.is_month_checked):
                return True, date
            
            self.is_day_checked = True
            if self.date_ranges is None:

                return True, date
            if not sub.isdigit():
                return False, date
            
            day = int(sub)
            date = date.replace(day=day)
            start_date = self.temp_date_ranges[0].replace( day=self.date_ranges[0].day, hour=0, minute=0)
            end_date = self.temp_date_ranges[1].replace( day=self.date_ranges[1].day, hour=23, minute=59)
            self.temp_date_ranges = (start_date, end_date)
            if self.temp_date_ranges[0] <= date <= self.temp_date_ranges[1]:
                
                return True, date
            else:
                return False, date
            
        #------------------------------check hour-------------------------
        elif step_name == FILE_STRUCT.HOUR:
            #we couldnt check day if year and month dose not check befor
            if not( self.is_year_checked and
                    self.is_month_checked and
                    self.is_day_checked):
                return True, date
            
            self.is_hour_checked = True
            if self.date_ranges is None:
                return True, date
            if not sub.isdigit():
                return False, date
            
            hour = int(sub)
            date = date.replace(hour=hour)
            start_date = self.temp_date_ranges[0].replace( hour=self.date_ranges[0].hour, minute=0)
            end_date = self.temp_date_ranges[1].replace( hour=self.date_ranges[1].hour, minute=59)
            self.temp_date_ranges = (start_date, end_date)
            if self.temp_date_ranges[0] <= date <= self.temp_date_ranges[1]:
                return True, date
            else:
                return False, date
            
        #------------------------------check minute-------------------------
        elif step_name == FILE_STRUCT.MINUTE:
            #we couldnt check day if year and month dose not check befor
            if not( self.is_year_checked and
                    self.is_month_checked and
                    self.is_day_checked and
                    self.is_hour_checked):
                return True, date
            
            self.is_minute_checked = True
            if self.date_ranges is None:
                return True, date
            if not sub.isdigit():
                return False, date
            
            minute = int(sub)
            date = date.replace(minute=minute)
            start_date = self.temp_date_ranges[0].replace( minute=self.date_ranges[0].minute)
            end_date = self.temp_date_ranges[1].replace( minute=self.date_ranges[1].minute)
            self.temp_date_ranges = (start_date, end_date)
            if self.temp_date_ranges[0] <= date <= self.temp_date_ranges[1]:
                
                return True, date
            else:
                return False, date
        #------------------------------check FILE-------------------------
        
        elif step_name == FILE_STRUCT.FILE:
            if self.date_ranges is None and self.trains is None:
                return True, date
            
            date, train_id, camera = transormUtils.extract_file_name_info(sub)
            
            if self.trains is not None:
                if not self.is_train_checked:
                    if train_id not in self.trains:
                        return False, date
                
            if self.date_ranges is not None:
                if not (self.is_year_checked and
                        self.is_month_checked and
                        self.is_day_checked and
                        self.is_hour_checked and
                        self.is_minute_checked):
                    if not( self.date_ranges[0] <= date <= self.date_ranges[1] ):
                        return False, date
            
            return True, date
        
        else:
            return True, date



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
                if line.lower().startswith("ok") or line.lower().startswith("unavailable"):
                    parts = line.split()
                    if len(parts) >= 3:
                        drive_letter = parts[1]
                        network_path = parts[2]
                        available = False
                        if parts[0].lower() == 'ok':
                            available = True

                        all_drives.append({
                            "drive_letter": drive_letter,
                            "network_path": network_path,
                            "status": available
                        })


        except subprocess.CalledProcessError as e:
            print("خطا در اجرای دستور 'net use':", e)
        
        finally:
            return all_drives
    
    def check_drived_is_mapped(self, ip:str):
        drives = self.get_mapped_drives()
        for drive in drives:
            if ip in drive['network_path']:
                return True
        return False
    
    def map_network(self, ip, share_path, username, password, drive_letter='Z:'):
        share_path = f'\\\\{ip}\\{share_path}'

        if username and password:
            command = f'net use {drive_letter} {share_path} /user:{username} {password}'
        else:
            command = f'net use {drive_letter} {share_path}'

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return True
            else:
                return False
        
        except Exception as e:
            print(f"error: {e}")
            return False
        

class CopyWorker(QObject):
    progress_signal = Signal(int)
    speed_singnl = Signal(int)
    log_signal = Signal(str)
    finish_signal = Signal()
    error_signal = Signal(str)

    def __init__(self, src_path, dst_path, conn_details,paths:list[str], sizes:list[int],copy_mode = 'copy'):
        super().__init__()
        self.src_path = src_path
        self.dst_path = dst_path
        self.conn_details = conn_details

        # Variables
        self.network_path = conn_details['share']
        self.drive_letter = "Z:"
        self.username = conn_details['username']
        self.password = conn_details['password']
        self.folder_to_copy = src_path
        self.destination_folder = dst_path
        self.image_condition = image_condition
        self.copy_mode = copy_mode

    def run(self):

        self.log_signal.emit("Checking if drive is mapped...")
        if not self.is_drive_mapped():
            self.log_signal.emit("Mapping network drive...")
            self.map_network_drive()

        if os.path.exists(self.drive_letter) or DEBUG_MODE:
            self.log.emit("Creating destination folder if it does not exist...")
            if not os.path.exists(self.destination_folder):
                os.makedirs(self.destination_folder)

            destination_path = os.path.join(self.destination_folder, os.path.basename(self.folder_to_copy))
            # if os.path.exists(destination_path):
            #     self.log.emit("Removing existing destination folder...")
            #     shutil.rmtree(destination_path)

            total_size = self.get_folder_size(self.folder_to_copy)
            copied_size = 0

            self.log.emit("Starting copy...")

            self.start_time = time.time()
            print('1')
            for root, dirs, files in os.walk(self.folder_to_copy):
                dest_dir = destination_path
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                for file in files:

                    doing_copy = True
                    date_time,train_id, camera_name=Utils.extract_file_name_info(file)
                    if self.image_condition is not None:
                        if not(self.image_condition['start']<=date_time<=self.image_condition['end']):
                            doing_copy=False


                    

                    src_file = os.path.join(root, file)



                    copied_size += os.path.getsize(src_file)


                    if doing_copy:

                        new_path = Utils.generate_path(dest_dir,date_time,train_id)
                        if not os.path.exists(new_path):
                            os.makedirs(new_path)
                        dest_file = os.path.join(new_path, file)

                        if self.copy_mode=='copy':
                            shutil.copy2(src_file, dest_file)

                        else:
                            shutil.move(src_file, dest_file)



                    progress = int(copied_size / total_size * 100)
                    self.progress.emit(progress)
                    self.log.emit("Starting copy...   {}".format(str(file)))

                        


            self.completed.emit()
            self.end_time = time.time()
            print(self.end_time-self.start_time)
            self.log.emit("Copy completed! Elpassed Time :{}".format(self.end_time-self.start_time))
        else:
            raise Exception('Failed to map the network drive. Check your network path, username, and password.')

        # except Exception as e:
        #     print(str(e))
        #     self.error.emit(str(e))

        # finally:
        #     self.disconnect_network_drive()

    def get_folder_size(self, folder):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

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




class pingWorker(QObject):
    result_signal = Signal(bool)

    def __init__(self, ip) -> None:
        super().__init__()
        self.ip = ip
    
    def run(self,):
        res = self.__get_ping(self.ip)
        self.result_signal.emit(res)

    def __get_ping(self, ip):
        if platform.system().lower() == "windows":
            param = "-n"
        else:
            param = "-c"
        
        try:
            # اجرای دستور پینگ
            output = subprocess.run(["ping", param, "1", ip], capture_output=True, text=True)
            
            # بررسی returncode
            if 'ttl' in output.stdout.lower():
                return True
            else:
                return False

        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        


if __name__:
    from PySide6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)


    nmap = shareMapping('','','')
    drives = nmap.get_mapped_drives()
    res = nmap.check_drived_is_mapped('192.168.1.60')
    
    
    def msg_callback(txt):
        pass
        return
        print(txt)

    obj = transformModule('', 'test_data2', 'dst')
    obj.start_transition(msg_callback,
                         trains=['11BGD1'],
                         dates_range=( JalaliDateTime(1402,3,13, 11,40), JalaliDateTime(1402,4, 11,8,30))
                            # dates_range=( JalaliDateTime(1402,1,1), JalaliDateTime(1403,12,13))
                         )
    app.exec()
    