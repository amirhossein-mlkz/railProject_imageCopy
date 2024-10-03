import sys
sys.path.append('C:\\Users\\amirh\Desktop\\railProject_SoftwareCopy')

import subprocess
import time
import os
import threading
import shutil

from persiantools.jdatetime import JalaliDateTime, timedelta
from PySide6.QtCore import Signal, QObject

from Tranform.Network import pingWorker, shareMapping
from Tranform.transformUtils import transormUtils
from Tranform.sharingConstans import DIRECTORY_TREE, STRUCT_PARTS
from Tranform.filesScanners import filesFinderWorker
from Tranform.filesActionWorker import CopyWorker



class transformModule:
    def __init__(self, ip:str, src_path:str, dst_path:str) -> None:
        self.ip = ip
        self.src_path = transormUtils.build_share_path(ip, src_path)
        self.dst_path = dst_path

        self.msg_callback = None

        self.ping_thread = None
        self.ping_worker = None

        self.searcher_thread = None
        self.searcher_worker = None

        self.move_flag = False
        
    
    
    
    

    def start_transition(self, msg_callback, trains=None, dates_range=None, move=False):
        self.move_flag = move
        self.msg_callback = msg_callback
        self.trains = trains
        self.dates_range = dates_range
        self.check_connection()


    def check_connection(self,):
        self.ping_worker = pingWorker(self.ip)
        self.ping_worker.result_signal.connect(self.connection_result_event)
        self.ping_thread = threading.Thread(target=self.ping_worker.run)
        self.ping_thread.start()

    def connection_result_event(self, status):
        if status:
            self.sreach_files()
        else:
            print('connection Failed')

    def sreach_files(self,):
        if not os.path.exists(self.src_path):
            print(f'transformModule.start_transition: {self.src_path} not exist')
            return
        
        self.searcher_worker = filesFinderWorker(self.src_path,
                                                 trains=self.trains,
                                                 date_ranges=self.dates_range,
                                                 struct=DIRECTORY_TREE)
        self.searcher_worker.log_signal.connect(self.msg_callback)
        self.searcher_worker.finish_signal.connect(self.files_list_ready)
        self.searcher_thread = threading.Thread( target=self.searcher_worker.run, daemon=True )
        self.searcher_thread.start()
        
    def files_list_ready(self, paths:list[str], sizes:list[int], avaiabilities:dict[str,dict[str, list]]):
        # a = transormUtils.dateTimeRanges( avaiabilities['11BG21']['right'], 600 )
        self.copy_worker = CopyWorker(self.src_path,
                                      dst_path=self.dst_path,
                                      files_paths=paths,
                                      sizes=sizes,
                                      move=self.move_flag
                                      )
        
        self.copy_worker.log_signal.connect(self.msg_callback)
        self.copy_worker.speed_singnal.connect(self.msg_callback)
        self.copy_worker.finish_signal.connect(self.copy_finish)
        self.copy_thread = threading.Thread( target=self.copy_worker.run, daemon=True )
        self.copy_thread.start()
        

    def copy_finish(self, ):

        print('copy done')









if __name__=='__main__':
    from PySide6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)


    nmap = shareMapping('','','')
    drives = nmap.get_mapped_drives()
    res = nmap.check_drived_is_mapped('192.168.1.60')
    if res is None and False:
        nmap.map_network('192.168.1.60','image_share',username='rail',password= '1', )
    
    
    def msg_callback1(txt):
        print(txt)

    obj = transformModule('192.168.1.60', 'image_share', 'c:\\image_share')
    obj.start_transition(msg_callback1,
                        #  trains=['11BGD1'],
                        #  dates_range=( JalaliDateTime(1402,3,13, 11,40), JalaliDateTime(1402,4, 11,8,30))
                            # dates_range=( JalaliDateTime(1402,1,1), JalaliDateTime(1403,12,13))
                         )
    app.exec()
    