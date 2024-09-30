import sys
import os
import shutil
from PySide6.QtCore import QThread, Signal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QProgressBar, QLabel, QFileDialog
import subprocess
import time
import platform
from persiantools.jdatetime import JalaliDateTime

DEBUG_MODE = True




class Utils():
    def __init__(self) -> None:
        pass

    
    @staticmethod
    def extract_file_name_info(name:str) -> tuple[JalaliDateTime, str, str]:
        date, clock, train_id, camera_name = name.split('_')
        dc_str = date + '_' + clock
        dt = JalaliDateTime.strptime(dc_str,'%Y-%m-%d_%H-%M-%S-%f')
        return dt, train_id, camera_name
    

    @staticmethod
    def generate_path(main_path:str, dt:JalaliDateTime, train_id:str):
        return os.path.join(main_path,
                    train_id,
                    str(dt.year),
                    str(dt.month),
                    str(dt.day)
                    )
    


if __name__=='__main__':


    name = "2024-07-31_19-28-30-817020_11BG21_right"
    dt, name, cam = extract_file_name_info(name)
    path = generate_path('', dt, name)

