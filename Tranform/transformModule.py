import sys

from Tranform.Network import pingAndCreateWorker
sys.path.append('C:\\Users\\amirh\Desktop\\railProject_SoftwareCopy')

import time
import threading

# from persiantools.jdatetime import JalaliDateTime, timedelta
# from PySide6.QtCore import Signal, QObject

try:
    from Tranform.Network import pingWorker, shareMapping
    from Tranform.transformUtils import transormUtils
    from Tranform.sharingConstans import DIRECTORY_TREE, STRUCT_PARTS
    from Tranform.filesScanners import filesFinderWorker
    from Tranform.filesActionWorker import CopyWorker

except:

    # from Network import pingWorker, shareMapping
    from transformUtils import transormUtils
    # from sharingConstans import DIRECTORY_TREE, STRUCT_PARTS
    # from filesScanners import filesFinderWorker
    # from filesActionWorker import CopyWorker




import subprocess


class transformModule:
    def __init__(self, 
                 ip:str, 
                 src_path:str, 
                 dst_path:str,
                 username:str,
                 password:str
                 ) -> None:
        self.ip = ip
        if self.ip is not None:

            

            self.src_path = transormUtils.build_share_path(ip, src_path)

            self.dst_path = dst_path
            self.username = username
            self.password = password


        else:
            self.src_path = src_path

            self.dst_path = None
            self.username = None
            self.password = None



        self.msg_callback = None

        self.ping_thread = None
        self.ping_worker = None

        self.searcher_thread = None
        self.searcher_worker = None

        self.move_flag = False
        
    
    
    
    

    # def start_transition(self, msg_callback, trains=None, dates_range=None, move=False):
    #     self.move_flag = move
    #     self.msg_callback = msg_callback
    #     self.trains = trains
    #     self.dates_range = dates_range
    #     self.check_connection()










    def check_connection(self, event_func, ):
        # self.ping_worker = pingWorker(self.ip, self.username, self.password)
        self.ping_worker = pingWorker(self.ip)
        self.ping_worker.result_signal.connect(event_func)
        self.ping_thread = threading.Thread(target=self.ping_worker.run, daemon=True)
        self.ping_thread.start()

    

    def check_connection_and_create_connection(self,event_func):



        self.ping_worker = pingAndCreateWorker(self.ip,self.src_path,self.username,self.password)
        self.ping_worker.result_signal.connect(event_func)
        self.ping_thread = threading.Thread(target=self.ping_worker.run, daemon=True)
        self.ping_thread.start()








        


    def find_files(self, trains, dates_tange, finish_event_func, log_event_func=None,log_search=False):
        
        
        self.searcher_worker = filesFinderWorker(self.src_path,
                                                 trains=trains,
                                                 date_ranges=dates_tange,
                                                 struct=DIRECTORY_TREE,
                                                 log_search=log_search)
        if log_event_func is not None:
            self.searcher_worker.log_signal.connect(log_event_func)

        self.searcher_worker.finish_signal.connect(finish_event_func)
        self.searcher_thread = threading.Thread( target=self.searcher_worker.run, daemon=True )
        self.searcher_thread.start()
        
    def start_copy(self, paths:list[str], sizes:list[int], finish_func, speed_func, progress_func, msg_callback, move=False):
        # a = transormUtils.dateTimeRanges( avaiabilities['11BG21']['right'], 600 )
        self.copy_worker = CopyWorker(self.src_path,
                                      dst_path=self.dst_path,
                                      files_paths=paths,
                                      sizes=sizes,
                                      move=move
                                      )
        
        self.copy_worker.log_signal.connect(msg_callback)
        self.copy_worker.progress_signal.connect(progress_func)
        self.copy_worker.speed_singnal.connect(speed_func)
        self.copy_worker.finish_signal.connect(finish_func)
        self.copy_thread = threading.Thread( target=self.copy_worker.run, daemon=True )
        self.copy_thread.start()
        

    def copy_finish(self, ):

        print('copy done')




    def read_log(self):

        print(self.src_path)





if __name__=='__main__':
    from PySide6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)


    # nmap = shareMapping('','','')
    # drives = nmap.get_mapped_drives()
    # res = nmap.check_drived_is_mapped('192.168.1.60')
    # if res is None and False:
    #     nmap.map_network('192.168.1.60','image_share',username='rail',password= '1', )
    
    
    # def msg_callback1(txt):
    #     print(txt)

    ip = '192.168.43.63'                    # IP address of the remote system
    share_path = 'test'                      # Shared folder on the remote system
    username = "MMM"                         # Your username
    password = "PHK"   


    obj = transformModule(ip=ip,src_path='test',dst_path='asd',username=username,password=password)
    ret = obj.create_connection()
    print(ret)
    app.exec()
    