from datetime import datetime
import os,sys

from PySide6.QtWidgets import QDialog
from persiantools.jdatetime import JalaliDateTime
from PySide6.QtCore import QTimer

from UIFiles.updateUI import Ui_Form

from PySide6 import QtCore as sQtCore

from PySide6 import QtWidgets as sQWidget

from timeSetting import timeSetting
from uiUtils.guiBackend import GUIBackend
from Tranform.transformUtils import transormUtils
from pathConstans import pathConstants
from Tranform.transformUtils import transormUtils
from pathConstans import pathConstants
import texts
from Tranform.transformModule import transformModule
from Tranform.sharingConstans import StatusCodes
import json
from pathConstans import pathConstants
from Styles import error_style,success_style,none_style
from Tranform.filesActionWorker import CopyWorker
from PySide6.QtGui import QFont,QIcon
from PySide6.QtWidgets import QMessageBox
import threading




class updateRemote(QDialog):

    def __init__(self, ip,user_name,password,name):
        super().__init__()



        # window setup
        flags = sQtCore.Qt.WindowFlags(
            sQtCore.Qt.FramelessWindowHint
        )  # remove the windows frame of ui
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self._old_pos = None

        self.language = 'English'

        self.ui = Ui_Form()
        self.ui.setupUi(self)


        self.fields_msg = {
            'lbl_msg': self.ui.lbl_msg,

        }



        self.ip = ip
        self.username = user_name
        self.password = password
        self.name = name

        GUIBackend.button_connector(self.ui.close_btn, self.close_win)
        GUIBackend.button_connector(self.ui.btn_check_version_ig, self.start_update)
        GUIBackend.button_connector(self.ui.btn_update_ig, self.start_copy)



        self.setup()



    
    def setup(self):

        self.ui.ip.setText(str(self.ip))
        self.ui.name.setText(self.name)
    


    def mousePressEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton and not self.isMaximized():
            # accept event only on top bar
            if (
                event.position().y() <= self.ui.topFrame.height()
            ):
                self._old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton:
            self._old_pos = None



    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = sQtCore.QPoint(event.globalPosition().toPoint() - self._old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._old_pos = event.globalPosition().toPoint()




    def close_win(self):

        ret = self.show_question(texts.MESSAGES['message'][self.language],texts.MESSAGES['Close'][self.language])
        if ret:

            self.close()
            # sys.exit()









    def show_error(self, txt, disapear=None):
        if txt:
            # GUIBackend.set_wgt_visible(self.fields_msg[name], True)
            GUIBackend.set_label_text(self.ui.error_lbl, txt)
            if disapear is not None:
                timer = QTimer()
                timer.singleShot(disapear, lambda: self.show_error(None))

        else:
            txt = ''
            GUIBackend.set_label_text(self.ui.error_lbl, txt)






    def start_update(self):

        if self.ip !=None and self.username!=None and self.password!=None:



            # self.config_path = self.image_grabber_log_path
            # self.read_config_path = self.log_path

            self.trasformer = transformModule(ip=self.ip,src_path=pathConstants.OTHER_UPDATE_IMAGEGRABBER_PATH,username=self.username,password=self.password,dst_path=None)

            self.update_software = 'image_grabber'

            self.trasformer.check_connection_and_create_connection(self.check_remote_version)

            self.show_message('lbl_msg', 'Connecting ...')

            self.ui.btn_update_ig.setDisabled(True)
            self.ui.btn_update_ig.setDisabled(True)

      

    def check_remote_version(self, status_code,msg=''):


        if status_code == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            if msg !='':
                self.show_message('lbl_msg', msg)
            else:
                self.show_message('lbl_msg', 'Connection Faild. check ip and cables connections')
            # GUIBackend.set_disable_enable(self.ui.copy_button, True)
            return
        
        elif status_code == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:

            self.show_message('lbl_msg', msg)
            

            path = transormUtils.build_share_path(self.ip, pathConstants.OTHER_UPDATE_IMAGEGRABBER_MANIFEST_PATH)

            if os.path.exists(path):
                
                # try:
                    with open(path, 'r', encoding='utf-8') as f:
                        self.json_data = json.load(f)
                    
                    # print(self.json_data)


                    self.show_message('lbl_msg', 'Get Remote Version')

                    self.remote_version = self.json_data['version']

                    self.ui.lbl_remote_version_ig.setText(self.remote_version)

                    self.check_exist_version(remote_version=self.remote_version)
                # except:
                #     self.show_message('lbl_msg', 'Error Cannot Read Remote Version')

            else:
                self.show_message('lbl_msg', 'Remote Version Not Exist')


    def check_exist_version(self,remote_version=None):

        path = pathConstants.SELF_UPDATE_IMAGEGRABBER_MANIFEST_PATH

        try:
            with open(path, 'r', encoding='utf-8') as f:
                self.json_data = json.load(f)
            
            # print(self.json_data)


            self.show_message('lbl_msg', 'Get Current Version')

            self.current_exist_version = self.json_data['version']

            self.ui.lbl_exist_version_ig.setText(self.current_exist_version)


            self.compare_versions(exist_version=self.current_exist_version,remote_version=remote_version)

        except:
            self.show_message('lbl_msg', 'Error Cannot Get Current Version')
            

    def compare_versions(self,exist_version,remote_version):

        self.ui.btn_update_ig.setDisabled(False)

        if remote_version<exist_version:
            self.show_message('lbl_msg', 'You Can Update -> Click on Start Copy')
            self.ui.btn_update_ig.setDisabled(False)
            self.flag_can_update_ig = True

        else:
            self.show_message('lbl_msg', 'You Cannot Update Remote Version is Higher')
            self.ui.btn_update_ig.setDisabled(True)
            self.flag_can_update_ig = False


    
    def start_copy(self):

        
        self.src_path = pathConstants.SELF_UPDATE_IMAGEGRABBER_PATH
        self.dst_path = pathConstants.OTHER_UPDATE_IMAGEGRABBER_PATH

        self.trasformer = transformModule(self.ip, self.src_path, self.dst_path, self.username, self.password,reverse_mode=True)
        self.show_message('lbl_msg', 'Check Connection...')
        # self.set_loading_progress_bar(loading=True)
        
        GUIBackend.set_disable_enable(self.ui.btn_update_ig, False)

        self.log_search = False
        self.date_time_ranges = None

        self.start_copy_logs = False

        # self.trasformer.check_connection(self.step1_check_connection_event)
        self.trasformer.check_connection_and_create_connection(self.step1_check_connection_event)

        
    def step1_log_event(self, log:str):
        txt = f'Searching Files: {log}'
        self.show_message('lbl_msg', txt)


    def step1_check_connection_event(self, status_code,msg=''):
        if status_code == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            if msg !='':
                self.show_message('lbl_msg', msg)
            else:
                self.show_message('lbl_msg', 'Connection Faild. check ip and cables connections')
            GUIBackend.set_disable_enable(self.ui.btn_update_ig, True)
            # self.set_loading_progress_bar(False)
            return
        
        elif status_code == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
            self.show_message('lbl_msg', 'Searching Files...')

            paths = os.listdir(self.src_path)



            file_paths = []

            sizes = []
            
            for root, dirs, files in os.walk(self.src_path):
                # Add all files in the current directory
                for file in files:
                    file_paths.append(os.path.join(root, file))

                    sizes.append(get_size(os.path.join(root, file)))


            # for root, dirs, files in os.walk(paths):
            #     # Add all files in the current directory
            #     for file in files:
            #         file_paths.append(os.path.join(root, file))



                # paths[i] = transormUtils.build_share_path(self.ip,dst_path,)



                # size_in_mb = size_in_bytes / (1024 * 1024)  # Convert bytes to MB
                # print(f"Path: {path} | Size: {size_in_bytes} bytes ({size_in_mb:.2f} MB)")

            dst_path = transormUtils.build_share_path(self.ip,self.dst_path,)


            self.copy_worker = CopyWorker(dst_path=dst_path,src_path=self.src_path,files_paths=file_paths,sizes=sizes,move=False)


            # self.copy_worker.log_signal.connect(msg_callback)
            self.copy_worker.progress_signal.connect(self.step2_update_progress)
            # self.copy_worker.speed_singnal.connect(speed_func)
            self.copy_worker.finish_signal.connect(self.finish_func)
            self.copy_thread = threading.Thread( target=self.copy_worker.run, daemon=True )
            self.copy_thread.start()
            # self.copy_worker.run()
            self.show_message('lbl_msg', 'Updating')






    def finish_func(self):

        self.show_message('lbl_msg', 'Update finished')

        print('Copy finished')




    def step2_update_progress(self, completed:int, total:int):
        if total<1:
            total = 1 
        percent = int(completed/total * 100)
        self.ui.progressBar_ig.setValue(percent)


        

    def step2_files_list_ready_event(self, 
                                     status_code, 
                                     paths:list[str], 
                                     sizes:list[int], 
                                     ):
        
        if status_code == StatusCodes.findFilesStatusCodes.DIR_NOT_EXISTS:
            self.show_message('copy', f"Path dosen't exists: {self.trasformer.src_path} ", )
            GUIBackend.set_disable_enable(self.ui.copy_button, True)
            self.set_loading_progress_bar(False)
            return
        


        if len(paths) == 0:
            GUIBackend.set_disable_enable(self.ui.copy_button, True)
            self.show_message('copy', 'No Files Found to Copy')
            self.set_loading_progress_bar(False)
            return
        
        move = False
        if self.log_search:
            move = True

        self.ui.progress_bar.setMinimum(0)
        self.ui.progress_bar.setMaximum(100)
        self.ui.progress_bar.setValue(0)
        self.trasformer.start_copy(paths, 
                                   sizes, 
                                   finish_func=self.step3_copy_finish_event,
                                   speed_func=self.step2_update_speed,
                                   progress_func=self.step2_update_progress,
                                   msg_callback=self.step2_log,
                                   rename_src=True,
                                   move=move)





    def set_loading_progress_bar(self,loading=True):

        if loading:

            self.ui.progressBar.setMaximum(0)
            self.ui.progressBar.setValue(0)

        else:
            self.ui.progressBar.setMaximum(100)
            self.ui.progressBar.setValue(100)









    def show_question(self, title, message, question=True):
        # Create the custom QMessageBox
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # Set the font size to 20 for the message box
        font = QFont()
        font.setPointSize(10)
        msg_box.setFont(font)

        if question:
            # Add custom buttons for "بلی" and "خیر"
            yes_button = msg_box.addButton("Yes", QMessageBox.YesRole)
            yes_button.setFont(font)

            no_button = msg_box.addButton("No", QMessageBox.NoRole)
            no_button.setFont(font)


            # Set default button (optional)
            msg_box.setDefaultButton(no_button)

            # Execute and check which button was clicked
            msg_box.exec_()

            if msg_box.clickedButton() == yes_button:
                return True
            if msg_box.clickedButton() == no_button:
                return False
        else:
            # Add the "تایید" button for simple confirmations
            ok_button = msg_box.addButton("Confirm", QMessageBox.AcceptRole)

            # Execute and check if Ok (or تایید) was clicked
            msg_box.exec_()

            if msg_box.clickedButton() == ok_button:
                return True





    def show_message(self, name, txt, disapear=None,style=None):
        if txt:
            # GUIBackend.set_wgt_visible(self.fields_msg[name], True)
            GUIBackend.set_label_text(self.fields_msg[name], txt)
            if disapear is not None:
                timer = QTimer()
                timer.singleShot(disapear, lambda: self.show_message(name, None))
          
                if style is not None:
                    self.fields_msg[name].setStyleSheet(style)

        else:
            txt = ''
            GUIBackend.set_label_text(self.fields_msg[name], txt)
            # GUIBackend.set_wgt_visible(self.fields_msg[name], False)

            try:
                self.fields_msg[name].setStyleSheet(none_style)
            except:
                print('Error in set none style')
            









def get_size(path):
    """Returns the size of a file or directory in bytes."""
    if os.path.isfile(path):
        # For a file, return its size directly
        return os.path.getsize(path)
    elif os.path.isdir(path):
        # For a directory, calculate the total size of all files within
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                # Skip broken symlinks
                if os.path.exists(file_path):
                    total_size += os.path.getsize(file_path)
        return total_size
    else:
        return 0  # If the path doesn't exist or isn't a file/directory








if __name__ == "__main__":

    sys.path.append('UIFiles\\Assets')


    os.system('CMD /C pyside6-uic UIFiles/updateUI.ui -o UIFiles/updateUI.py')


    app = sQWidget()
    win = updateRemote()

    win.show()
    sys.exit(app.exec())