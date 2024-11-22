import sys,os,platform,time,threading
import subprocess
import shutil
import re,json

from PySide6.QtWidgets import QGraphicsBlurEffect
from PySide6.QtWidgets import QAbstractSpinBox
from PySide6 import QtCore as sQtCore
from PySide6.QtWidgets import QMainWindow as sQMainWindow
from PySide6.QtWidgets import QApplication as sQApplication
from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont,QIcon
from PySide6.QtWidgets import QMessageBox
import sqlite3
from persiantools.jdatetime import JalaliDateTime

from Tranform.transformUtils import transormUtils
from database import DataBase
from Calendar import  JalaliCalendarDialog
from guiBackend import GUIBackend
from login import LoginPage
from UIFiles.main_UI import Ui_main
from uiUtils.GUIComponents import single_timer_runner
from Tranform.transformModule import transformModule, archiveManager
from Tranform.sharingConstans import StatusCodes
from Tranform.Network import pingAndCreateWorker, pingWorker
from uiUtils.mapDictionary import mapDictionary
from timeSetting import timeSetting
from timeSettingDialog import timeSettingDialog
import texts
from UpdateRemote import updateRemote

from Styles import error_style,success_style,none_style,click_side_btns,normal_side_btns
from ShowConfig import ShowConfig
from Constants import BASE_CONFIG,CAMERA_NAMES,CONFIG_PATH, EXISTVIDEOS_PATH, IMAGE_GRABBER_CONFIG_PATH,PARMS,EXISTVIDEOS_PATH,MAIN_PATH,IMAGE_PATH,LOG_PATH,DST_PATH, UTILS_PATH

from UpdateExistVideos import WidgetUpdateExistVideos

DEBUG = True


# ui class
class mainUI(sQMainWindow):

    def __init__(self):
        super().__init__()



        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.language = 'English'
        self.login_ui = LoginPage(self)
        self.login_ui.login_button_connector(self.check_password)
        self.login_ui.close_button_connector(self.close_login)

        self.is_login = False

        # window setup
        flags = sQtCore.Qt.WindowFlags(
            sQtCore.Qt.FramelessWindowHint
        )  # remove the windows frame of ui
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self._old_pos = None
        self.set_login_status(False) 
        self.ui.stackedWidget.setCurrentWidget(self.ui.copy)
        self.db = DataBase('data.db')
        self.button_connector()

        self.load_pathes()


        self.fields_msg = {
            'copy': self.ui.copy_log_lbl,
            'timeline':self.ui.time_line_msg,
            'setting_msg' : self.ui.label_message_change_password,
            'profile' :  self.ui.label_profile_message,
            'profile_edit' :  self.ui.label_profile_edit_message,
            'load_config': self.ui.load_config_msg,
            'send_config': self.ui.send_config_msg,
        }

        self.mapDict = mapDictionary({
            'codec': {
                'none':'Best Quality',
                'mpeg':'Best Compression'
            }
        })

        GUIBackend.set_combobox_items(self.ui.new_profile_compression, self.mapDict.get_values('codec'))
        GUIBackend.set_combobox_items(self.ui.edit_profile_compression, self.mapDict.get_values('codec'))

        self.side_btns = [ self.ui.side_setting_btn , self.ui.side_train_config_btn,self.ui.side_profile_btn,self.ui.side_copy_btn]

        self.names = []


     

        self.calenders = {
            'start':JalaliCalendarDialog( self.ui.start_date),
            'end'  :JalaliCalendarDialog(self.ui.end_date)
        }

        self.calenders_btn = {
            'start': self.ui.start_calendar_btn,
            'end': self.ui.end_calendar_btn

        }
        for name , btn in self.calenders_btn.items():
            GUIBackend.button_connector_argument_pass(btn, self.open_calender, args=(name,))

      
        self.init_clock_spinbox()
        self.all_style_repoblish()
        self.startup()

        self.load_train_configs()
        self.edit_mode(mode=False)
        self.profile_edit_mode(mode=False)


        self.create_init_folders()

        self.load_train_profiles()


        self.clear_ui_profile()

        self.log_search = False

        self.flag_copy_log = True  ############ Temp

        self.ui.progressBar.setMaximum(100)  # Indefinite progress
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setValue(0)



    def create_init_folders(self):
        if not os.path.exists(CONFIG_PATH):
            os.mkdir(CONFIG_PATH)

    def startup(self,):
        for name in self.fields_msg.keys():
            self.show_message(name, None)

    def init_clock_spinbox(self,):
        self.ui.start_time_hour.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.start_time_minute.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.end_time_hour.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.end_time_minute.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.end_time_hour.setValue(23)
        self.ui.end_time_minute.setValue(59)

    def all_style_repoblish(self,):        
        for atr_name in dir(self.ui):
            atr = getattr(self.ui, atr_name)
            try:
                atr.style().unpolish(atr)
                atr.style().polish(atr)
            except:
                pass

    def open_calender(self, name:str):
        
        self.calenders[name].show()

    def button_connector(self):

        self.ui.close_btn.clicked.connect(self.close_win)
        self.ui.check_time_btn.clicked.connect(self.check_time_sync)
        self.ui.minimize_btn.clicked.connect(self.minimize_win)

        self.ui.copy_button.clicked.connect(self.ui_copy)
        # self.ui.copy_button.clicked.connect(self.copy_logs)

        self.ui.side_copy_btn.clicked.connect(self.set_stack_widget)
        self.ui.side_profile_btn.clicked.connect(self.set_stack_widget)
        self.ui.side_train_config_btn.clicked.connect(self.set_stack_widget)
        self.ui.side_setting_btn.clicked.connect(self.set_stack_widget)
        
        self.ui.login_btn.clicked.connect(self.show_login)

        self.ui.btn_save_train.clicked.connect(self.save_train_config)
        self.ui.btn_check_connection.clicked.connect(self.check_connection_train_cofig)
        self.ui.btn_edit_config.clicked.connect(self.edit_config_train)
        self.ui.btn_delete_config.clicked.connect(self.delete_config_train)
        self.ui.btn_save_config_edit.clicked.connect(self.save_config_edit)
        self.ui.btn_cancel_config_edit.clicked.connect(self.cancel_config_edit)
        self.ui.btn_refresh_name_config_edit.clicked.connect(self.load_train_configs)

        self.ui.combo_copy_train_name.currentIndexChanged.connect(self.ui_update_copy_parms)


        self.ui.btn_change_password.clicked.connect(self.change_password)
        self.ui.btn_save_password.clicked.connect(self.save_password)


        self.ui.group_camera_1.toggled.connect(self.on_group_box_toggled)
        self.ui.group_camera_2.toggled.connect(self.on_group_box_toggled)
        self.ui.group_camera_3.toggled.connect(self.on_group_box_toggled)
        self.ui.group_camera_4.toggled.connect(self.on_group_box_toggled)

        self.ui.btn_save_profile.clicked.connect(self.save_camera_config)

        
        self.ui.btn_edit_profile.clicked.connect(self.edit_profile)
        self.ui.btn_delete_profile.clicked.connect(self.delete_profile)
        self.ui.btn_save_edit_profile.clicked.connect(self.save_edit_profile)
        self.ui.btn_cancel_edit_profile.clicked.connect(self.cancel_edit_profile)
        self.ui.btn_send_profile.clicked.connect(self.send_profile)
        self.ui.btn_load_profile.clicked.connect(self.load_profile)
        self.ui.combo_load_train_name.currentIndexChanged.connect(self.set_load_ip)

        self.ui.btn_refresh_profile_name.clicked.connect(self.refresh_edit_profile)

        self.ui.btn_local_update.clicked.connect(self.update_exist_videos)



        self.ui.btn_update_train.clicked.connect(self.check_train_update)

        

    def show_login(self):
        if self.is_login:
            self.set_login_status(False)
        else:
            self.applyBlurEffect()
            self.login_ui.show()

    def close_login(self):
        
        self.login_ui.close()

    def check_password(self):

        password = self.login_ui.get_hash_pass()
        if password == '':
            self.login_ui.write_error('Please Enter Password')
            return
        

        
        passwords_db = self.db.fetch_table_as_dict(table_name='password')
        for pass_db in passwords_db:    
            if str(password) == str(pass_db['password']):
                self.set_login_status(True)
                self.login_ui.close()
                
            
            else:
                self.login_ui.write_error("Password is not correct")



    def set_login_status(self, status):
        self.is_login = status
        self.ui.timeline_groupbox.setVisible(status) 
        GUIBackend.set_checkbox_value(self.ui.only_copy_new_checkbox, True)

        if status == True:
            self.ui.login_btn.setText('Logout')
            self.ui.login_btn.setIcon(QIcon(":/asstets/icons/logout_icon.png"))

        else:
            self.ui.login_btn.setText('Login')
            self.ui.login_btn.setIcon(QIcon(":/asstets/icons/login_icon.png"))


        


    def covert_date(self,jdatetime):
        date = jdatetime.strftime('%Y/%m/%d')
        return date
    
    def set_stack_widget(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "side_copy_btn":
            self.ui.stackedWidget.setCurrentWidget(self.ui.copy)
        if btnName == "side_profile_btn":
            self.ui.stackedWidget.setCurrentWidget(self.ui.camera_config)
        if btnName == "side_train_config_btn":
            self.ui.stackedWidget.setCurrentWidget(self.ui.train_config)
        if btnName == "side_setting_btn":
            self.ui.stackedWidget.setCurrentWidget(self.ui.settings)
        

        self.clear_side_btns(click_btn=btn)




    def clear_side_btns(self,click_btn=None):


        for btn in self.side_btns:            
            btn.setStyleSheet(normal_side_btns)

        click_btn.setStyleSheet(click_side_btns)



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
            sys.exit()

    def minimize_win(self):
        self.showMinimized()


    
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
            

        


    def load_pathes(self):
        res = self.db.fetch_table_as_dict(table_name='pathes')

        data = self.load_json(json_name=BASE_CONFIG)

        if data:
            self.main_path = MAIN_PATH
            self.image_path = os.path.join(self.main_path,IMAGE_PATH)
            self.log_path = os.path.join(self.main_path,UTILS_PATH,LOG_PATH)
            self.image_grabber_log_path = os.path.join(self.main_path,UTILS_PATH,IMAGE_GRABBER_CONFIG_PATH)


            self.dst_main_path  = os.path.join(DST_PATH,MAIN_PATH)
            # if DEBUG:
            #     pass
            #     self.dst_main_path  = os.path.join('C:\\test_share',MAIN_PATH)      ############# TEMP
            self.dst_image_path = os.path.join(self.dst_main_path,IMAGE_PATH) 
            self.dst_utils_path = os.path.join(self.dst_main_path,UTILS_PATH)
            self.archive_path = os.path.join(self.dst_utils_path,EXISTVIDEOS_PATH)
            self.dst_log_path = os.path.join(self.dst_utils_path,LOG_PATH)


            pathes = [self.dst_main_path,self.dst_image_path,self.dst_utils_path]

            for path in pathes:
                if not os.path.exists(path):
                    print(path)
                    os.makedirs(path)




    def ui_copy(self):
        self.start_copy()

    
    def ui_update_copy_parms(self):

        name = self.ui.combo_copy_train_name.currentText()

        ret = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=name)

        if len(ret)!=1:
            print('Error in get data')
            return
        
        ret = ret[0]


        self.ui.ip_input.setText(ret['ip'])
        self.ui.username_input.setText(ret['username'])


    def start_copy(self,image_condition=None):

        self.set_error_btn(error_count = 0)
        
        name = self.ui.combo_copy_train_name.currentText()

        ret = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=name)

        if len(ret)!=1:
            print('Error in get data')
            return
        
        ret = ret[0]


        self.copy_ip = ret['ip']
        self.copy_username = ret['username']
        self.copy_password = ret['password']
        src_path = self.image_path
        dst_path = self.dst_image_path
        self.date_time_ranges = None
        self.status_of_file = 'new'

        if self.ui.timeline_groupbox.isChecked() and self.is_login:
            start_date_time = self.calenders['start'].date
            end_date_time = self.calenders['end'].date

            start_h = self.ui.start_time_hour.value()
            start_min = self.ui.start_time_minute.value()

            end_h = self.ui.end_time_hour.value()
            end_min = self.ui.end_time_minute.value()

            start_date_time = start_date_time.replace(hour=start_h, minute=start_min, second=0, microsecond=0)
            end_date_time = end_date_time.replace(hour=end_h, minute=end_min, second=0, microsecond=0)

            if start_date_time > end_date_time:
                self.show_message('timeline', "start date time can't be bigger than end", 4000)
                return

            self.date_time_ranges = (start_date_time, end_date_time)

            #------------------------------------------------------------
            if GUIBackend.get_checkbox_value(self.ui.only_copy_new_checkbox):
                self.status_of_file = 'new'
            else:
                self.status_of_file = None


            

        self.trasformer = transformModule(self.copy_ip, src_path, dst_path, self.copy_username, self.copy_password)
        self.show_message('copy', 'Check Connection...')
        self.set_loading_progress_bar(loading=True)
        
        GUIBackend.set_disable_enable(self.ui.copy_button, False)

        self.log_search = False
        self.start_copy_logs = False

        # self.trasformer.check_connection(self.step1_check_connection_event)
        self.trasformer.check_connection_and_create_connection(self.step1_check_connection_event)


    def step1_check_connection_event(self, status_code,msg=''):
        if status_code == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            if msg !='':
                self.show_message('copy', msg)
            else:
                self.show_message('copy', 'Connection Faild. check ip and cables connections')
            GUIBackend.set_disable_enable(self.ui.copy_button, True)
            self.set_loading_progress_bar(False)
            return
        
        elif status_code == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
            self.show_message('copy', 'Searching Files...')
            self.trasformer.find_files( trains= None,
                                        dates_tange=self.date_time_ranges,
                                        finish_event_func=self.step2_files_list_ready_event,
                                        log_event_func=self.step1_log_event,
                                        log_search=self.log_search,
                                        status=self.status_of_file)

    def step1_log_event(self, log:str):
        txt = f'Searching Files: {log}'
        self.show_message('copy', txt)

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

            if self.flag_copy_log and not self.start_copy_logs:
                self.copy_logs()
            else:
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

    def step2_update_progress(self, completed:int, total:int):
        if total<1:
            total = 1 
        percent = int(completed/total * 100)
        self.ui.progress_bar.setValue(percent)
        #Convert to MB
        self.ui.completed_copy_lbl.setText(str(completed))
        self.ui.total_copy_lbl.setText(str(total))

    def step2_update_speed(self, speed):
        speed = speed / (1024)**2
        speed = round(speed,1)
        txt = f'Speed: {speed} MB'
        self.ui.copy_speed_lbl.setText(txt)

    def step2_log(self, txt):
        self.show_message('copy', txt)


    def step3_copy_finish_event(self, status_code):
        if status_code == StatusCodes.copyStatusCodes.DISCONNECT:
            GUIBackend.set_disable_enable(self.ui.copy_button, True)
            self.show_message('copy', "Dissconnected!")
            self.set_loading_progress_bar(False)
            return
        # a = transormUtils.dateTimeRanges( avaiabilities['11BG21']['right'], 600 )
        GUIBackend.set_disable_enable(self.ui.copy_button, True)
        self.show_message('copy', "Copy Videos Finish Success")

        self.set_loading_progress_bar(loading=False)



        if self.log_search and self.start_copy_logs:
            new_logs = self.trasformer.searcher_worker.res_paths
            self.show_logs(new_logs)
            self.update_exist_videos()

        if self.flag_copy_log and not self.start_copy_logs:
            self.copy_logs()

    def show_logs(self,new_logs):
        
        self.errors = 0
        for log in new_logs:
            split = log.split('\\')
            file = split[-1]
            folder = split[-2]

            log_path = os.path.join(self.dst_log_path,folder,file)

            errors = self.read_log(log_path=log_path)
            self.errors+=errors




        self.set_error_btn(error_count = self.errors)



    def set_error_btn(self,error_count):
        if error_count>0:
            self.ui.btn_found_errors.setText('{} Error Found , Click To Send When Connect Internet !'.format(error_count))
        else:
            self.ui.btn_found_errors.setText('')


    def read_log(self,log_path):
        print(log_path)
        # Open and read the log file
        with open(log_path, 'r', encoding='utf-8') as file:
            log_content = file.readlines()

        # Initialize the error count
        error_count = 0

        # Loop through and process each line
        for line in log_content:
            if "ERROR" in line:
                error_count += 1
                # print(line.strip())  # Print each error line

        return error_count








    def update_exist_videos(self):

        self.show_message('copy', "Local Updateing You Can Remove Trian Connection")
        self.show_message('setting_msg', "Local Updateing You Can Remove Trian Connection")
        self.set_loading_progress_bar(loading=True)

        self.archive_manager = archiveManager(self.dst_utils_path)
        self.archive_manager.update_archive(self.dst_image_path, self.save_exist_videos)

        



    def save_exist_videos(self,status_code,):
        print(status_code)
        if status_code == StatusCodes.findFilesStatusCodes.DIR_NOT_EXISTS:
            self.show_message('copy', "archive directory not exist")
            return
        
        if status_code == StatusCodes.findFilesStatusCodes.SUCCESS:
            self.show_message('copy', "archive updated")

        self.set_loading_progress_bar(False)
            

        return
        print('asd')
        avaiabilities

        if avaiabilities != {}:
            for train_name in avaiabilities.keys():
                train = avaiabilities[train_name]
                for camera in train.keys():
                    try:
                        date_times = train[camera]
                        times = transormUtils.dateTimeRanges(date_times=date_times,step_lenght_sec=600,max_gap_sec=10)
                        train[camera] = times
                    except:
                        print('Error in Convert timtimes to ranges')
                        self.show_message('copy', "Error in Local Updating")
                        self.show_message('setting_msg', "Error in Local Updating")
        else:
            self.show_message('copy', "Nothing to Update")
            self.show_message('setting_msg', "Nothing to Update")
            return


        json_exist_videos = self.dst_exist_videos_path


        if os.path.exists(json_exist_videos):
            os.remove(json_exist_videos)

        # # Your code to write the JSON
        try:
            with open(json_exist_videos, 'w', encoding='utf-8') as f:
                json.dump(avaiabilities, f, ensure_ascii=False, indent=4, default=self.custom_json_handler)
            self.show_message('copy', "Finish Local Updateing")
            self.show_message('setting_msg', "Finish Local Updateing")
            self.set_loading_progress_bar(loading=False)



        except:

            self.show_message('copy', "Error in Write New File")
            self.show_message('setting_msg', "Error in Write New File")
            self.set_loading_progress_bar(loading=False)


    # Custom JSON encoder function
    def custom_json_handler(self,obj):
        if isinstance(obj, JalaliDateTime):
            return obj.strftime('%Y-%m-%d %H:%M')  # Convert to string format
        raise TypeError(f"Type {type(obj)} is not serializable")



    def set_loading_progress_bar(self,loading=True):

        if loading:

            self.ui.progressBar.setMaximum(0)
            self.ui.progressBar.setValue(0)

        else:
            self.ui.progressBar.setMaximum(100)
            self.ui.progressBar.setValue(100)

    def copy_logs(self):


        self.start_copy_logs = True

        self.show_message('copy', "Start Copy Logs ...")

        name = self.ui.combo_copy_train_name.currentText()

        ret = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=name)

        if len(ret)!=1:
            print('Error in get data')
            return
        
        ret = ret[0]


        self.copy_ip = ret['ip']
        self.copy_username = ret['username']
        self.copy_password = ret['password']
        src_path = self.log_path
        dst_path = self.dst_log_path
        self.date_time_ranges = None
        self.status_of_file = 'new'


        self.trasformer = transformModule(self.copy_ip, src_path, dst_path, self.copy_username, self.copy_password)

        self.log_search=True
        # self.trasformer.check_connection(self.step1_check_connection_event)
        self.trasformer.check_connection_and_create_connection(self.step1_check_connection_event)


        # check_connection_and_create_connection



    def applyBlurEffect(self):
        current_effect = self.graphicsEffect()
        if current_effect:
            self.setGraphicsEffect(None)
        else:
            blur_effect = QGraphicsBlurEffect()
            blur_effect.setBlurRadius(10)
            self.setGraphicsEffect(blur_effect)




    def save_train_config(self):


        name = self.ui.line_train_profile_name.text()

        ip = self.ui.line_train_profile_ip.text()
        username = self.ui.line_train_profile_username.text()
        password = self.ui.line_train_profile_password.text()
    
        if name =='' or ip=='' or username=='' or password=='':
            print('name error')
            return
        

        if not self.is_valid_ip(ip):
            print('IP Error')
            return
        
        ret = self.show_question(texts.MESSAGES['message'][self.language],texts.MESSAGES['CheckSave'][self.language])

        if ret:



            ret = self.db.add_value('TrainConfig',name=name,ip=ip,username=username,password=password)

            if ret:
                print('Add Complete')

                ip = self.ui.line_train_profile_ip.setText('')
                username = self.ui.line_train_profile_username.setText('')
                password = self.ui.line_train_profile_password.setText('')
                self.load_train_configs()




    def check_connection_train_cofig(self):
        print('check_connection_train_cofig')
        return

    def cancel_config_edit(self,):
        self.edit_mode(mode=False)


    def save_config_edit(self):


        name = self.ui.combo_train_name_config.currentText()
        ip = self.ui.line_train_profile_ip_edit.text()
        username = self.ui.line_train_profile_username_edit.text()
        password = self.ui.line_train_profile_password_edit.text()

       
        if  ip=='' or username=='' or password=='':
            print('name error')
            return
        

        ret = self.show_question(texts.MESSAGES['message'][self.language],texts.MESSAGES['CheckSave'][self.language])

        if ret:

            flag = False
            ip_ret = self.db.update_row_by_input(table_name='TrainConfig',column_name='ip',new_value=ip,condition_field='name',condition_value=name)
            if ip_ret:
                username_ret = self.db.update_row_by_input(table_name='TrainConfig',column_name='username',new_value=username,condition_field='name',condition_value=name)
                if username_ret:
                    password_ret = self.db.update_row_by_input(table_name='TrainConfig',column_name='password',new_value=password,condition_field='name',condition_value=name)
                    if password_ret:
                        flag =  True
            if flag:
                print('Update Sucssfully')                
                self.edit_mode(mode=False)

        self.load_train_configs()
        self.ui_update_copy_parms()
    
        
    

    def load_train_configs(self):

        ret = self.db.fetch_table_as_dict(table_name='TrainConfig')
        if len(ret)>=1:
        
            self.names = []
            for row in ret:
                self.names.append(row['name'])

        GUIBackend.set_combobox_items(self.ui.combo_train_name_config,self.names)
        GUIBackend.set_combobox_items(self.ui.combo_copy_train_name,self.names)
        GUIBackend.set_combobox_items(self.ui.combo_send_train_name,self.names)
        GUIBackend.set_combobox_items(self.ui.combo_load_train_name,self.names)

        


    def load_train_profiles(self):

        configs = os.listdir(CONFIG_PATH)
        try:
            configs.remove(BASE_CONFIG)
        except:
            print('Base Config Not Exist')
            return
        new_configs = []
        for config in configs:
            # new_configs.append(config.split('.')[1])
            config = config.replace(".json", "")
            new_configs.append(config)

        GUIBackend.set_combobox_items(self.ui.combo_train_name_profile,new_configs)
        GUIBackend.set_combobox_items(self.ui.combo_send_profile_name,new_configs)




    def delete_config_train(self):
        name = self.ui.combo_train_name_config.currentText()

        ret = self.show_question(texts.MESSAGES['message'][self.language],texts.MESSAGES['Delete'][self.language])

        if ret:

            self.db.remove_row_by_col_name(table_name='TrainConfig',col_name='name',name_value=name)
            print('Item Removed')

        self.load_train_configs()
    

    def edit_config_train(self):


        name = self.ui.combo_train_name_config.currentText()

        ret = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=name)

        if len(ret)!=1:
            print('Error in get data')
            return
        
        ret = ret[0]

        self.edit_mode(mode=True)


        self.ui.line_train_profile_ip_edit.setText(ret['ip'])
        self.ui.line_train_profile_username_edit.setText(ret['username'])
        self.ui.line_train_profile_password_edit.setText(ret['password'])
        return



    def edit_mode(self,mode):
        if not mode:
            ip = self.ui.line_train_profile_ip_edit.setText('')
            username = self.ui.line_train_profile_username_edit.setText('')
            password = self.ui.line_train_profile_password_edit.setText('')

        self.ui.btn_delete_config.setDisabled(mode)
        self.ui.btn_edit_config.setDisabled(mode)
        self.ui.combo_train_name_config.setDisabled(mode)
        self.ui.btn_refresh_name_config_edit.setDisabled(mode)
        self.ui.frame_train_edit.setDisabled(not(mode))
        self.ui.btn_save_config_edit.setDisabled(not(mode))
        self.ui.btn_cancel_config_edit.setDisabled(not(mode))



        




    def change_password(self):

        self.set_frame_change_password(mode=True)

        return
    


    def set_frame_change_password(self,mode=True):
        height = 180
        if self.ui.frame_change_password.height()>0:
            height = 0

        if not(mode):
            height = 0
            
        self.ui.frame_change_password.setMaximumHeight(height)
        self.ui.frame_change_password.setMinimumHeight(height)

        self.ui.line_current_password.setText('')
        self.ui.line_new_password.setText('')
        self.ui.line_confirm_password.setText('')


    def save_password(self):

        current_password =  self.ui.line_current_password.text()

        hass_pass =  self.login_ui.convert_pass2hash(password=current_password)
                
        passwords_db = self.db.fetch_table_as_dict(table_name='password')
        reset_pass = False
        for iter,pass_db in enumerate(passwords_db):    
            if str(hass_pass) == str(pass_db['password']):
                reset_pass = True
                self.pass_id = iter
                break
        
        if not(reset_pass):
            
            print('Current password is wrong')

            self.show_message(name='setting_msg',txt='Current Password Wrong',disapear=2000,style=error_style)



            return


        if reset_pass:

            new_password = self.ui.line_new_password.text()
            confirm_password = self.ui.line_confirm_password.text()

            if new_password != confirm_password or new_password=='' :
                reset_pass = False
        

        if not(reset_pass):
            
            print('Password not match')

            self.show_message(name='setting_msg',txt='Password Not Match',disapear=2000,style=error_style)

            return



        if reset_pass:

            new_hass_pass = self.login_ui.convert_pass2hash(password=new_password)

            ret = self.db.update_row_by_input(table_name='password',column_name='password',new_value=new_hass_pass,condition_field='id',condition_value=0)

            if ret:

                self.show_message(name='setting_msg',txt='Password Update Successfully',disapear=2000,style=success_style)

                self.set_frame_change_password(mode=False)

            
            else:
                reset_pass = False
        



    def on_group_box_toggled(self, checked):
        # Get the sender of the signal (the group box that was toggled)
        group_box_name = self.sender()
        group_box = group_box_name
        group_box_name = group_box_name.objectName()
        group_box_name = group_box_name.split('_')[-1]
        group_box_name = int(group_box_name)
        if group_box_name>1:

            ret , msg = self.check_camera_config(group_box_name)

            if not ret:

                print(msg)
                group_box.setChecked(False)
                self.show_message('profile',txt=msg,style=error_style,disapear=2000)


    def clear_ui_profile(self, edit=False):


        for iter in range(len(CAMERA_NAMES)):

            for parm in PARMS:
                if edit:
                    input = eval('self.ui.line_{}_camera_{}_edit'.format(parm,iter+1))
                else:
                    input = eval('self.ui.line_{}_camera_{}'.format(parm,iter+1))

                input.setText('')
            
            self.ui.group_camera_1.setChecked(False)
            if edit :
                group = eval('self.ui.group_camera_{}_edit'.format(iter+1))
            
            else:
                group = eval('self.ui.group_camera_{}'.format(iter+1))

                GUIBackend.set_input(self.ui.line_train_name, '')
            group.setChecked(False)


    def check_camera_config(self,index,edit= False):
        
        message = True
        flag = True
        one_item = False
        for iter in range(1,index):
            if edit:
                goup_box = eval('self.ui.group_camera_{}_edit'.format(iter))
            else:
                goup_box = eval('self.ui.group_camera_{}'.format(iter))
            if goup_box.isChecked():
                one_item = True
                for parm in PARMS:

                    if edit:
                        input = eval('self.ui.line_{}_camera_{}_edit.text()'.format(parm,iter))

                    else:
                        input = eval('self.ui.line_{}_camera_{}.text()'.format(parm,iter))

                    if parm == 'ip':

                        ret = self.is_valid_ip(input)

                        if not ret:
                            message = 'IP Camera {} is not correct'.format(iter)
                            flag = False
                            break

                    if input =='':
                        flag = False
                        message = 'Field {} Camera {} is Empty'.format(parm,iter)

                        break




                
            if not flag :
                break

        if not one_item:
            message = 'At Least Select One Item'
            flag = False
            return flag,message


        return flag,message

    def is_valid_ip(self,ip):
        # Regular expression pattern to match a valid IPv4 address
        pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
        return pattern.match(ip) is not None






    def save_camera_config(self):
        train_name = self.get_train_name_config()
        codec_ui = GUIBackend.get_combobox_selected(self.ui.new_profile_compression)
        codec = self.mapDict.value2key('codec', codec_ui)

        ret,msg = self.check_train_name(train_name=train_name)
        if not ret:
            self.show_message('profile',txt=msg,style=error_style,disapear=2000)
            return False

        ret , msg = self.check_camera_config(index=5)
        # ret = True ############# temp
        if not ret:
            print(msg)
            self.show_message('profile',txt=msg,style=error_style,disapear=2000)
        
        else:
            config = self.load_json(json_name=BASE_CONFIG)
            if config:
                print(config['cameras'])
            
            else:
                return
            

            ret = self.show_question(texts.MESSAGES['message'][self.language],texts.MESSAGES['Save'][self.language])

            if not ret:
                return


            camera_configs = self.create_camera_configs()

            config = self.update_base_json(config,camera_configs,train_name, codec)

            self.save_json(save_name=train_name,json_data=config)

            self.clear_ui_profile()

            self.refresh_edit_profile()



    def update_base_json(self,json_data,camera_configs=None,train_name=None, codec=None):

        if camera_configs:
            json_data['cameras'] = camera_configs
        if train_name:
            json_data ['train_id'] = train_name
        if codec:
            json_data['video_codec'] = codec
        return json_data
    

    def check_train_name(self,train_name):

        exist_json = os.listdir(CONFIG_PATH)
        train_name = train_name+'.json'
        if train_name =='.json':
            return False,'Train Name Is Empty'
        elif train_name in exist_json:
            return False,'Duplicate Name , Change Train Name'


        return True,''

    def create_camera_configs(self,edit_mode = False):

        configs = []

        for iter in range(len(CAMERA_NAMES)):

            config = {}
            
            if edit_mode:
                state = GUIBackend.is_groupbox_checked(eval(f'self.ui.group_camera_{iter+1}_edit'))
                if not state:
                    continue
                name = eval('self.ui.line_{}_camera_{}_edit.text()'.format(PARMS[0],iter+1))
                ip = eval('self.ui.line_{}_camera_{}_edit.text()'.format(PARMS[1],iter+1))
                port = eval('self.ui.line_{}_camera_{}_edit.text()'.format(PARMS[2],iter+1))
                username = eval('self.ui.line_{}_camera_{}_edit.text()'.format(PARMS[3],iter+1))
                password = eval('self.ui.line_{}_camera_{}_edit.text()'.format(PARMS[4],iter+1))

            else:
                state = GUIBackend.is_groupbox_checked(eval(f'self.ui.group_camera_{iter+1}'))
                if not state:
                    continue
                name =     eval('self.ui.line_{}_camera_{}.text()'.format(PARMS[0],iter+1))
                ip =       eval('self.ui.line_{}_camera_{}.text()'.format(PARMS[1],iter+1))
                port =     eval('self.ui.line_{}_camera_{}.text()'.format(PARMS[2],iter+1))
                username = eval('self.ui.line_{}_camera_{}.text()'.format(PARMS[3],iter+1))
                password = eval('self.ui.line_{}_camera_{}.text()'.format(PARMS[4],iter+1))

            config = {
                'name' : name,
                'ip' : ip,
                'port': port, 
                'username' :username,
                'password' :password
            }

            configs.append(config)

        return configs


    def get_train_name_config(self):

        train_name = self.ui.line_train_name.text()
        return train_name


    def load_json(self,json_name):

            try:
                if '.' in json_name:
                    if json_name.split('.')[-1] != 'json':
                        json_name = json_name + '.json'
                else:
                    json_name = json_name + '.json'
                path = os.path.join(CONFIG_PATH,json_name)
                with open(path, 'r', encoding='utf-8') as f:
                    self.json_data = json.load(f)
                return self.json_data

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load Base Configuration: {e}")
                return False


    def save_json(self,save_name,json_data, show_msg = True):

        try:
            if '.' in save_name:
                if save_name.split('.')[-1] != 'json':
                    save_name = save_name + '.json'
            else:
                save_name = save_name + '.json'

            save_path = os.path.join(CONFIG_PATH,save_name)
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)

            if show_msg:
                QMessageBox.information(self, "Success", "Configuration saved successfully!")
            
            return True

        except Exception as e:
            print(e)
            if show_msg:
                QMessageBox.critical(self, "Error", f"Failed to save Configuration: {e}")
            return False




    def edit_profile(self):
        profile = self.ui.combo_train_name_profile.currentText()

        json_data = self.load_json(json_name=profile)

        train_id = json_data['train_id']
        camera_configs = json_data['cameras']
        codec = json_data['video_codec']
        codec_ui = self.mapDict.key2value('codec', codec)
        GUIBackend.set_combobox_current_item(self.ui.edit_profile_compression, codec_ui)
        GUIBackend.set_input( self.ui.edit_profile_name, train_id)


        for iter,config in enumerate(camera_configs):
            one_item = False
            
            for parm in PARMS:

                if config[parm] !='':
                    one_item=True
                input = eval('self.ui.line_{}_camera_{}_edit'.format(parm,iter+1))
                input.setText(config[parm])

            if one_item:
                group = eval('self.ui.group_camera_{}_edit'.format(iter+1))
                group.setChecked(True)

        self.profile_edit_mode(mode=True)


    def profile_edit_mode(self,mode=True):
        # return
        height = 0 
        if mode:
            height = 490

        self.ui.frame_profile_edit.setMaximumHeight(height)
        self.ui.btn_edit_profile.setDisabled(mode)
        self.ui.btn_delete_profile.setDisabled(mode)
        self.ui.combo_train_name_profile.setDisabled(mode)

        self.ui.btn_save_edit_profile.setDisabled(not(mode))

    
    def delete_profile(self):

        profile = self.ui.combo_train_name_profile.currentText()


        ret = self.show_question(texts.MESSAGES['message'][self.language],texts.MESSAGES['Delete'][self.language])

        if ret:
            profile = profile+'.json'
            path = os.path.join(CONFIG_PATH,profile)
            os.remove(path)
            self.load_train_profiles()




    def refresh_edit_profile(self):
        self.load_train_profiles()


    def cancel_edit_profile(self,):
        self.profile_edit_mode(mode=False)

    def save_edit_profile(self):

        profile = self.ui.combo_train_name_profile.currentText()
        new_train_id = GUIBackend.get_input(self.ui.edit_profile_name)
        json_path = os.path.join(CONFIG_PATH, profile + '.json')

        if profile == '':
            self.show_message('profile',txt='profile cant be empty',style=error_style,disapear=2000)
            return
        
        if profile.lower() != new_train_id.lower():
            ret,msg = self.check_train_name(train_name=new_train_id)
            if not ret:
                self.show_message('profile',txt=msg, style=error_style,disapear=2000)
                return False
        


        if not os.path.exists(json_path):
            self.show_message('profile',txt='Profile Config Not Exist, maybe deleted during edit',style=error_style,disapear=2000)
            return

        json_data = self.load_json(json_name=profile)
        camera_configs = self.create_camera_configs(edit_mode=True)
        ret , msg = self.check_camera_config(index=5,edit=True)

        if ret:
            codec_ui = GUIBackend.get_combobox_selected(self.ui.edit_profile_compression)
            codec = self.mapDict.value2key('codec', codec_ui)

            json_data = self.update_base_json(json_data,camera_configs, train_name=new_train_id, codec=codec)

            if os.path.exists(json_path):
                try:
                    os.remove(json_path)
                except:
                    self.show_message('profile',txt='failed replace',style=error_style,disapear=2000)
                    return
                    
            self.save_json(save_name=new_train_id,json_data=json_data)
            self.profile_edit_mode(mode=False)
            self.refresh_edit_profile()

        else:
            self.show_message('profile_edit',txt=msg,style=error_style,disapear=2000)







    def send_profile(self):
        self.show_message('send_config', '')  
        profile_name = self.ui.combo_send_profile_name.currentText()

        if profile_name =='':
            self.show_message('send_config', 'no Profile Exist')
            return

        train_name = self.ui.combo_send_train_name.currentText()
        if train_name =='':
            self.show_message('send_config', 'No Train Exist')
            return

        ret = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=train_name)
        if len(ret) == 0:
            self.show_message('send_config', 'Train Info not Found, it may deleted')
        train_info = ret[0]

        self.train_info_to_send_config = train_info
        self.config_name_to_send = profile_name

        path = transormUtils.build_share_path(train_info['ip'], self.main_path)
        pingworker = pingAndCreateWorker(train_info['ip'], path, train_info['username'], train_info['password'])
        pingworker.result_signal.connect(self.send_config_step1)
        threading.Thread(target=pingworker.run).start()
        self.ui.btn_send_profile.setDisabled(True)


        # profile_name = profile_name+'.json'
        # file_path = os.path.join(CONFIG_PATH,profile_name)
        # print(file_path,'   ',train_parms)

    def send_config_step1(self, status_code, msg:str):
        if status_code == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            if msg !='':
                self.show_message('send_config', msg)
                self.ui.btn_send_profile.setEnabled(True)

            else:
                self.show_message('send_config', 'Connection Faild. check ip and cables connections')
                self.ui.btn_send_profile.setEnabled(True)

            return
        
        elif status_code == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:

            self.show_message('send_config', msg)
    

            config_path = transormUtils.build_share_path(self.train_info_to_send_config['ip'],
                                                         self.image_grabber_log_path)
            dir_config, _ = os.path.split(config_path)
            if not os.path.exists(dir_config):
                self.show_message('send_config', 'Utils Directory Not Exist')
                self.ui.btn_send_profile.setEnabled(True)
                return
            


            src_config_path = os.path.join(CONFIG_PATH, self.config_name_to_send + '.json')

            #-----------------update last modify------------------------
            json_data = self.load_json(self.config_name_to_send)
            if json_data is None:
                self.show_message('send_config', f'Couldnt Load Config')
                self.ui.btn_send_profile.setEnabled(True)
                return
            ret = self.save_json(self.config_name_to_send, json_data, show_msg=False)
            if ret == False:
                self.show_message('send_config', f'An Error Occur')
                self.ui.btn_send_profile.setEnabled(True)
                return
            #-----------------------------------------------------------
            
            
            if not os.path.exists(src_config_path):
                self.show_message('send_config', 'Selected Config file not found')
                self.ui.btn_send_profile.setEnabled(True)
                return
            
            try:
                shutil.copy2(src_config_path, config_path)
                self.show_message('send_config', 'write config success')
            except Exception as e:
                self.show_message('send_config', f'An Error Occur: {e}')
            finally:
                self.ui.btn_send_profile.setEnabled(True)



                

    def load_profile(self):

        train_name = self.ui.combo_load_train_name.currentText()
        if train_name =='':
            print('No train Exist')
            return


        train_parms = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=train_name)



        if len(train_parms)>0:

            parms = train_parms[0]
            self.remote_ip = parms['ip']
            username = parms['username']
            password = parms['password']



            # self.config_path = self.image_grabber_log_path
            self.read_config_path = self.log_path

            self.trasformer = transformModule(ip=self.remote_ip,src_path=self.read_config_path,username=username,password=password,dst_path=None)

            self.trasformer.check_connection_and_create_connection(self.step1_load_profile)

            self.show_message('load_config', 'Connecting ...')


            self.ui.btn_load_profile.setDisabled(True)
            self.ui.combo_load_train_name.setDisabled(True)

    def step1_load_profile(self, status_code,msg=''):

        self.ui.btn_load_profile.setDisabled(False)
        self.ui.combo_load_train_name.setDisabled(False)

        if status_code == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            if msg !='':
                self.show_message('load_config', msg)
            else:
                self.show_message('load_config', 'Connection Faild. check ip and cables connections')
            # GUIBackend.set_disable_enable(self.ui.copy_button, True)
            return
        
        elif status_code == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:

            self.show_message('load_config', msg)
            

            json_path = transormUtils.build_share_path(self.remote_ip,self.image_grabber_log_path)
            if os.path.exists(json_path):
                

                with open(json_path, 'r', encoding='utf-8') as f:
                    self.json_data = json.load(f)

                self.ui_show_config = ShowConfig(self.json_data)
                self.ui_show_config.show()
                # self.trasformer.read_log()
                self.show_message('load_config', 'Window Show')
            else:
                self.show_message('load_config', 'Config Not Exist')




    def show_load_parms(self):

        return
    
    def set_load_ip(self):

        self.show_message('load_config', '')


        train_name = self.ui.combo_load_train_name.currentText()
        train_parms = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=train_name)

        if len(train_parms)==1: 
            train_parms = train_parms[0]
            self.ui.line_ip_load.setText(train_parms['ip'])



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


    def check_time_sync(self,):
        name = self.ui.combo_copy_train_name.currentText()
        db_results = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=name)

        if len(db_results)!=1:
            print('Error in get data')
            return
        
        db_res = db_results[0]
        self.ip = db_res['ip']
        src_path = 'rail_share'
        src_path = transormUtils.build_share_path(self.ip, src_path)

        self.ping_worker = pingAndCreateWorker(self.ip, src_path,db_res['username'],db_res['password'])
        self.ping_worker.result_signal.connect(self.time_sysnc_connection_event)
        self.ping_thread = threading.Thread(target=self.ping_worker.run, daemon=True)
        self.ping_thread.start()
        GUIBackend.set_disable_enable(self.ui.check_time_btn, False)
        self.show_message('copy', '')


    def time_sysnc_connection_event(self, status_code,msg=''):
        if status_code == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            if msg !='':
                self.show_message('copy', msg)
            else:
                self.show_message('copy', 'Connection Faild. check ip and cables connections')
            GUIBackend.set_disable_enable(self.ui.check_time_btn, True)
            self.set_loading_progress_bar(False)
            return
        
        elif status_code == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
            
            GUIBackend.set_disable_enable(self.ui.check_time_btn, False)
            tsd = timeSettingDialog( self.ip )
            tsd.exec_()

            GUIBackend.set_disable_enable(self.ui.check_time_btn, True)


            

    def check_train_update(self):



        name = self.ui.combo_copy_train_name.currentText()
        db_results = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=name)

        if len(db_results)!=1:
            self.show_message('copy', 'Error in Get Data')
            return
        
        db_res = db_results[0]
        self.db_res = db_res
        self.ip = db_res['ip']
        src_path = 'rail_share'
        src_path = transormUtils.build_share_path(self.ip, src_path)

        self.ping_worker = pingAndCreateWorker(self.ip, src_path,db_res['username'],db_res['password'])
        self.ping_worker.result_signal.connect(self.remote_update_event)
        self.ping_thread = threading.Thread(target=self.ping_worker.run, daemon=True)
        self.ping_thread.start()
        GUIBackend.set_disable_enable(self.ui.btn_update_train, False)
        self.show_message('copy', 'Check Connection')





    def remote_update_event(self, status_code,msg=''):
        if status_code == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            if msg !='':
                self.show_message('copy', msg)
            else:
                self.show_message('copy', 'Connection Faild. check ip and cables connections')
            GUIBackend.set_disable_enable(self.ui.btn_update_train, True)
            self.set_loading_progress_bar(False)
            return
        
        elif status_code == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
            
            GUIBackend.set_disable_enable(self.ui.btn_update_train, False)
            tsd = updateRemote( self.ip , user_name=self.db_res['username'],password=self.db_res['password'],name=self.db_res['name'] )
            tsd.exec_()

            GUIBackend.set_disable_enable(self.ui.btn_update_train, True)






# if __name__ == "__main__":


#     os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'calendar.ui'), os.path.join('UIFiles', 'calendar.py')))


#     app = sQApplication()
#     win = UI_main_window_org()

#     win.show()
#     sys.exit(app.exec())