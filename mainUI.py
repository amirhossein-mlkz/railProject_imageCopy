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
from PySide6.QtWidgets import QVBoxLayout, QWidget, QComboBox, QGridLayout, QLabel, QDialog,QDialogButtonBox,QPushButton,QFrame , QStatusBar

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
from Tranform.Network import Sharing

from pathConstans import pathConstants
from FirewallRules import enable_file_sharing, ensure_network_discovery_enabled

from timeSetting import timeSetting
from utils.Storage import StorageWidget , get_current_drive_storage
from utils import Storage
import dorsa_logger
from pathConstans import pathConstants
from Tranform.storageManager import storageManager,Space

from IPChecker import check_ip

DEBUG = False
SHOW_LASTLOG = True


# ui class
class mainUI(sQMainWindow):

    def __init__(self):
        super().__init__()



        self.ui = Ui_main()
        self.ui.setupUi(self)

        self.create_init_folders()




        self.logger = dorsa_logger.logger(
                                        main_folderpath=pathConstants.SELF_LOGS_SHARE_FOLDER,
                                        date_type=dorsa_logger.date_types.AD_DATE,
                                        date_format=dorsa_logger.date_formats.YYMMDD,
                                        time_format=dorsa_logger.time_formats.HHMMSS,
                                        file_level=dorsa_logger.log_levels.DEBUG,
                                        console_level=dorsa_logger.log_levels.DEBUG,
                                        console_print=True,
                                        current_username="NotLogin",
                                        line_seperator='-')






        self.language = 'English'
        self.login_ui = LoginPage(self)
        self.login_ui.login_button_connector(self.check_password)
        self.login_ui.close_button_connector(self.close_login)

        self.is_login = False






        # Create a QStatusBar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Set the maximum height for the status bar (e.g., 30 pixels)
        self.status_bar.setMaximumHeight(10)


                # Set the background color and text color using a stylesheet
        self.status_bar.setStyleSheet("""
            QStatusBar {
                background-color: rgb(220, 221, 180);  /* Background color */
            }
        """)




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
        self.storage_obj = storageManager(path=pathConstants.SELF_IMAGES_DIR,
                                          logs_path=None)
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
            'ip_msg' : self.ui.lbl_ip_error,
        }

        self.mapDict = mapDictionary({
            'codec': {
                'none':'Best Quality',
                'mpeg':'Best Compression'
            }
        })

        GUIBackend.set_combobox_items(self.ui.new_profile_compression, self.mapDict.get_values('codec'))
        GUIBackend.set_combobox_items(self.ui.edit_profile_compression, self.mapDict.get_values('codec'))
        GUIBackend.set_combobox_items(self.ui.new_profile_motion, ['Enable','Disable'])
        GUIBackend.set_combobox_items(self.ui.edit_profile_motion, ['Enable','Disable'])

        self.side_btns = [ self.ui.side_setting_btn , self.ui.side_train_config_btn,self.ui.side_profile_btn,self.ui.side_copy_btn]
        # self.side_btns = [ ]

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



        self.load_train_profiles()


        self.clear_ui_profile()

        self.log_search = False

        self.flag_copy_log = True  ############ Temp

        self.ui.progressBar.setMaximum(100)  # Indefinite progress
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setValue(0)


        self.create_share_folder()
        self.set_firewall_rules()




        self.show_storage()

    
        self.load_storage_values()




        ############################ LOG  #####################################

        log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                    text=f"MainUI Completed", 
                                    code="Minit000")
        self.logger.create_new_log(message=log_msg)

        #######################################################################


        #self.ui.btn_update_train.setVisible(False)
        #self.ui.btn_update_train.setVisible(False)




    def show_storage(self):

        self.storage_object = StorageWidget(path=pathConstants.SELF_IMAGES_DIR)
        self.storage_object.set_delete_func_event(self.manual_delete)
        GUIBackend.add_widget(self.ui.storage_widget,self.storage_object)


    def set_firewall_rules(self):

        ret = enable_file_sharing()

        msg = ensure_network_discovery_enabled()



        ############################ LOG  #####################################

        log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                    text=f"Firewall Rules Updated : {ret} , Enusre discovery : {msg}", 
                                    code="Minit000")
        self.logger.create_new_log(message=log_msg)

        #######################################################################




    
    def create_share_folder(self):
        try:
            ret_remove =  Sharing.remove_share(pathConstants.SELF_SHARE_NAME)
            ret_share = Sharing.create_and_share_folder(pathConstants.SELF_SHARE_PATH,
                                            pathConstants.SELF_SHARE_NAME)
            


            ############################ LOG  #####################################

            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                        text=f"Remove Share Folder : {ret_remove} , Create Share Folder : {ret_share} ", 
                                        code="Mc000")
            self.logger.create_new_log(message=log_msg)

            #######################################################################



        except:
            pass


    def create_init_folders(self):
        if not os.path.exists(CONFIG_PATH):
            os.mkdir(CONFIG_PATH)

        if not os.path.exists(pathConstants.SELF_LOGS_SHARE_FOLDER):
            os.makedirs(pathConstants.SELF_LOGS_SHARE_FOLDER)

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

        self.ui.btn_edit_config.clicked.connect(self.edit_config_train)
        self.ui.btn_delete_config.clicked.connect(self.delete_config_train)
        self.ui.btn_save_config_edit.clicked.connect(self.save_config_edit)
        self.ui.btn_cancel_config_edit.clicked.connect(self.cancel_config_edit)
        self.ui.btn_refresh_name_config_edit.clicked.connect(self.load_train_configs)

        self.ui.combo_copy_train_name.currentIndexChanged.connect(self.ui_update_copy_parms)


        self.ui.btn_change_password.clicked.connect(self.change_password)
        self.ui.btn_storage_manager.clicked.connect(self.show_ui_storage)
        self.ui.btn_save_password.clicked.connect(self.save_password)
        self.ui.btn_save_storage.clicked.connect(self.save_storage_config)
        


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

        


        ############################### LOG  ##################################

        log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                    text=f"Buttons Connected", 
                                    code="Mc000")
        self.logger.create_new_log(message=log_msg)

        #######################################################################







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


        ############################### LOG  ##################################

        log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                    text=f"Close Windows Show", 
                                    code="Mc000")
        self.logger.create_new_log(message=log_msg)

        #######################################################################



        if ret:
            ############################### LOG  ##################################
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                        text=f"Software Closed", 
                                        code="Mc000")
            self.logger.create_new_log(message=log_msg)
            #######################################################################

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

        try:
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

            else:

                ############################### LOG  ##################################
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Load Pathes Error", 
                                            code="ml000")
                self.logger.create_new_log(message=log_msg)
                #######################################################################

        except Exception as e:

            ############################### LOG  ##################################
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                        text=f"Except Error in Load pathes : {e}", 
                                        code="ml001")
            self.logger.create_new_log(message=log_msg)
            #######################################################################


    def ui_copy(self):

        self.start_copy()




    
    def ui_update_copy_parms(self):

        name = self.ui.combo_copy_train_name.currentText()

        ret = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=name)

        if len(ret)!=1:
            print('Error in get data')

            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Get train info from DB error {ret}", 
                                            code="Mu001")
                self.logger.create_new_log(message=log_msg)
            except:
                print('Create log function get db ui_update_copy_parms error')
                pass
            #######################################################################
            
            return
        


        ret = ret[0]
        self.ui.ip_input.setText(ret['ip'])
        self.ui.username_input.setText(ret['username'])


        ############################### LOG  ##################################
        try:
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                        text=f"Update Copy Params in UI {ret['ip']} {ret['username']}", 
                                        code="Mu000")
            self.logger.create_new_log(message=log_msg)
        except:
            print('Create log function ui_update_copy_parms error')
            pass
        #######################################################################





        flag , msg = check_ip(ret['ip'])

        if flag:
            self.ui.lbl_ip_error.setStyleSheet(""" 
                                               
                                                border: 2px solid #004a00; /* Blue border */
                                                border-radius: 10px;
                                               
                                                background-color: #008000;  /* Background color */ """)

        else:
            self.ui.lbl_ip_error.setStyleSheet(""" 
                                               
                                                border: 2px solid #8a8a00; /* Blue border */
                                                border-radius: 10px;                             
                                                background-color: #FFFF00;  /* Background color */ """)

        self.show_message('ip_msg',msg)



        ############################### LOG  ##################################
        try:
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                        text=f"Check IP : {flag},{msg}", 
                                        code="Mu001")
            self.logger.create_new_log(message=log_msg)
        except:
            print('Create log function check_ip error')
            pass
        #######################################################################






    def start_copy(self,image_condition=None):


        ############################### LOG  ##################################
        log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                    text=f"Start Copy Clicked", 
                                    code="Mc000")
        self.logger.create_new_log(message=log_msg)
        #######################################################################




        self.set_error_btn(error_count = 0)
        
        name = self.ui.combo_copy_train_name.currentText()

        ret = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=name)

        if len(ret)!=1:
            print('Error in get data')

            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Get train info from DB error {ret}", 
                                            code="Mu001")
                self.logger.create_new_log(message=log_msg)
            except:
                print('Create log function start_copy ui_update_copy_parms error')
                pass
            #######################################################################



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
                self.show_message('timeline', "Start can not Later Than End ", 4000,style = error_style)
                return

            self.date_time_ranges = (start_date_time, end_date_time)

            #------------------------------------------------------------
            if GUIBackend.get_checkbox_value(self.ui.only_copy_new_checkbox):
                self.status_of_file = 'new'
            else:
                self.status_of_file = None



            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Timeline Selected {self.date_time_ranges}", 
                                            code="Ms000")
                self.logger.create_new_log(message=log_msg)
            except:
                print('Create log function start copy error')
                pass
            #######################################################################





            

        self.trasformer = transformModule(self.copy_ip, src_path, dst_path, self.copy_username, self.copy_password)
        self.show_message('copy', 'Check Connection...')



        ############################### LOG  ##################################
        try:
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                        text=f"Show Message : check connection - src_path: {src_path} - dst_path : {dst_path}", 
                                        code="Ms001")
            self.logger.create_new_log(message=log_msg)
        except:
            pass
        #######################################################################

        
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
            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Error : check connection {status_code} {msg}", 
                                            code="Mstep1000")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################
            return
        
        elif status_code == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
            self.show_message('copy', 'Searching Files...')
            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                            text=f"Show Message : SearchingFiles", 
                                            code="Mscce001")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################
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
        

        self.show_message('copy', 'Check Storage')

        # ret = self.check_storage(needed_size = sum(sizes))



        # if not ret:
        #     self.start_cleaning(self,needed_size = sum(sizes))
        #     return

        if status_code == StatusCodes.findFilesStatusCodes.DIR_NOT_EXISTS:
            self.show_message('copy', f"Path doesn't exists: {self.trasformer.src_path} ", )
            GUIBackend.set_disable_enable(self.ui.copy_button, True)
            self.set_loading_progress_bar(False)


            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Error : {status_code} - Path doesn't exists: {self.trasformer.src_path}", 
                                            code="Ms001")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################

            return
        


        if len(paths) == 0:
            GUIBackend.set_disable_enable(self.ui.copy_button, True)
            self.show_message('copy', 'No Files Found to Copy')
            self.set_loading_progress_bar(False)

            if self.flag_copy_log and not self.start_copy_logs:
                self.copy_logs()
            else:
                self.set_loading_progress_bar(False)



            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"No Files Found to Copy - flag_copy_log : {self.flag_copy_log} , start_copy_logs : {self.start_copy_logs}", 
                                            code="Ms001")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################


            return
        
        self.show_message('copy', 'Check For Enough Space')


        res , space_should_be_delete = self.storage_obj.has_enough_space_for_files(files_path=paths,
                                                    sizes=sizes,
                                                    src_dir=self.trasformer.src_path,
                                                    dst_dir=self.trasformer.dst_path)




        if not res:
            # START CLEANING 

            self.storage_obj.send_clean_request(name='milad',size=space_should_be_delete)
            func = transormUtils.pass_extra_arg_event(event_func=self.clening_finish_signal,extra_args=(paths,sizes))
            self.storage_obj.finish_cleaning_signal.connect(func)
            self.storage_obj.progress_signal.connect(self.show_remove_files)

            clean_thread = threading.Thread(target=self.storage_obj.run,daemon=True)
            clean_thread.start()

        else:

            self.clening_finish_signal(name_id='', status=True,paths=paths,sizes=sizes)



    def show_remove_files(self,name_id,remove_path,deleted,total):

        print(remove_path)
        self.show_message('copy',f"Delete {deleted.toMB()}/{total.toMB()} - Removed {remove_path}")



    def clening_finish_signal(self,name_id, status,paths,sizes):

        if status:

            ## space is ready

            move = False
            rename_src = True

            if self.log_search:
                move = True
                rename_src = False

            self.ui.progress_bar.setMinimum(0)
            self.ui.progress_bar.setMaximum(100)
            self.ui.progress_bar.setValue(0)
            self.trasformer.start_copy(paths, 
                                    sizes, 
                                    finish_func=self.step3_copy_finish_event,
                                    speed_func=self.step2_update_speed,
                                    progress_func=self.step2_update_progress,
                                    msg_callback=self.step2_log,
                                    rename_src=rename_src,
                                    move=move)
            


            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                            text=f"Start Copy", 
                                            code="Mstep2002")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################


        else:

            self.show_message('copy','Space Not Enough For Download')
            self.ui.copy_button.setEnabled(True)
            self.ui.btn_local_update.click()




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

            

            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Step3 Error : Disconnected {status_code}", 
                                            code="Mstep3000")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################

            self.update_exist_videos()
            return
        # a = transormUtils.dateTimeRanges( avaiabilities['11BG21']['right'], 600 )

        GUIBackend.set_disable_enable(self.ui.copy_button, True)
        self.show_message('copy', "Copy Videos Finish Success")

        self.set_loading_progress_bar(loading=False)



        ############################### LOG  ##################################
        try:
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                        text=f"Copy Videos Finish Success", 
                                        code="Mstep3001")
            self.logger.create_new_log(message=log_msg)
        except:
            pass
        #######################################################################


        if self.log_search and self.start_copy_logs:

            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                            text=f"Start For Show Logs,CheckRemoteTime,UpdateArchive", 
                                            code="Mstep3003")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################


            new_logs = self.trasformer.searcher_worker.res_paths
            self.show_logs(new_logs)
            self.check_remote_time()
            self.update_exist_videos()

        if self.flag_copy_log and not self.start_copy_logs:

            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                            text=f"Start Copy Logs in Step3", 
                                            code="Mstep3002")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################

            self.update_exist_videos()
            
            self.copy_logs()




    def check_storage(self,size):

        print('needed size = ',size)
        ret , msg = self.storage_object.check_storage(needed_size_MB=size)
        self.show_message('copy',msg)

        return ret




    def start_cleaning(self,size):

        self.storage_object.start(space_should_be_clean_MB=size)





    def check_remote_time(self):

        
        try:

            name = self.ui.combo_copy_train_name.currentText()
            db_results = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=name)

            if len(db_results)!=1:
                print('Error in get data')
                return
            
            db_res = db_results[0]
            ip = db_res['ip']

            remote_time, local_time = timeSetting.get_time_from_remote_system(ip_address=ip)


            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                            text=f"Check Remote Time - remote_time: {remote_time} , local_time : {local_time}", 
                                            code="Mchek_remote_time001")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################


            if  remote_time is not None and local_time is not None:


                # Calculate the time delta between the two datetime objects
                time_delta = abs(remote_time - local_time)


                # Check if the delta is greater than one minute (60 seconds)
                if time_delta.total_seconds() < 60:
                    return

                else:
                    self.ui.check_time_btn.click()

                    ############################### LOG  ##################################
                    try:
                        log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                                    text=f"check_time_btn Clicked", 
                                                    code="Mchek_remote_time003")
                        self.logger.create_new_log(message=log_msg)
                    except:
                        pass
                    #######################################################################






        except Exception as e:

            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                            text=f"Error in check remote time {e}", 
                                            code="Mchek_remote_time002")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################


            





    def show_logs(self,new_logs):

        

        try:

            self.errors = 0
            if len(new_logs)==0:
                return

            if SHOW_LASTLOG:
                if len(new_logs)>1:
                    new_logs = [new_logs[-1]]

            for log in new_logs:
                split = log.split('\\')
                file = split[-1]
                folder = split[-2]

                log_path = os.path.join(self.dst_log_path,folder,file)

                errors = self.read_log(log_path=log_path)
                self.errors+=errors




            self.set_error_btn(error_count = self.errors)



            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                            text=f"Show Logs {self.errors} ", 
                                            code="Mshow_logs000")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################


        except:



            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                            text=f"Error in Show Logs ", 
                                            code="Mshow_logs001")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################




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

        try:

            self.show_message('copy', "Local Updateing You Can Remove Trian Connection")
            self.show_message('setting_msg', "Local Updateing You Can Remove Trian Connection")
            self.set_loading_progress_bar(loading=True)
            self.archive_manager = archiveManager(self.dst_utils_path)
            self.archive_manager.update_archive(self.dst_image_path, self.save_exist_videos)

            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                            text=f"Local Updateing You Can Remove Trian Connection", 
                                            code="Mupdate_exist_videos000")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################





        except Exception as e:

            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                            text=f"Error : Except in update exist Videos ", 
                                            code="Mupdate_exist_videos001")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################
        



    def save_exist_videos(self,status_code,):
        # print(status_code)
        if status_code == StatusCodes.findFilesStatusCodes.DIR_NOT_EXISTS:
            self.show_message('copy', "archive directory not exist")

            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Error : Archive directory not exist", 
                                            code="Msave_exist_videos001")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################
            return
        
        if status_code == StatusCodes.findFilesStatusCodes.SUCCESS:
            self.show_message('copy', "archive updated")

        self.set_loading_progress_bar(False)
            

        ############################### LOG  ##################################
        try:
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                        text=f"Archive Updated", 
                                        code="Msave_exist_videos002")
            self.logger.create_new_log(message=log_msg)
        except:
            pass
        #######################################################################


        return


    # Custom JSON encoder function
    def custom_json_handler(self,obj):
        if isinstance(obj, JalaliDateTime):
            return obj.strftime('%Y-%m-%d %H:%M')  # Convert to string format
        

        ############################### LOG  ##################################
        try:
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                        text=f"Type {type(obj)} is not serializable", 
                                        code="Mcustom_json_handler000")
            self.logger.create_new_log(message=log_msg)
        except:
            pass
        #######################################################################

        
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


        ############################### LOG  ##################################
        try:
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                        text=f"Start Copy Logs ", 
                                        code="Mcopy_logs000")
            self.logger.create_new_log(message=log_msg)
        except:
            pass
        #######################################################################




        name = self.ui.combo_copy_train_name.currentText()

        ret = self.db.fetch_spec_parm_table(table_name='TrainConfig',col_name='name',spec_row=name)

        if len(ret)!=1:
            print('Error in get data')

            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Error in Get data Copy Logs", 
                                            code="Mcopy_logs001")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################




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

        ############################### LOG  ##################################
        try:
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                        text=f"Start step1_check_connection_event in copy logs", 
                                        code="Mcopy_logs002")
            self.logger.create_new_log(message=log_msg)
        except:
            pass
        #######################################################################








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
            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Error in Save Train Config name:{name},ip:{ip},username:{username},password{password} ", 
                                            code="Msave_train_config000")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################
            return
        

        if not self.is_valid_ip(ip):
            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Error in IP Error {ip} ", 
                                            code="Msave_train_config001")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################
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

                ############################### LOG  ##################################
                try:
                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                                text=f"Train Add Complete {ip},{username}", 
                                                code="Msave_train_config000")
                    self.logger.create_new_log(message=log_msg)
                except:
                    pass
                #######################################################################
            
            else:

                ############################### LOG  ##################################
                try:
                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                                text=f"Error in add Train to database {ip},{username}", 
                                                code="Msave_train_config000")
                    self.logger.create_new_log(message=log_msg)
                except:
                    pass
                #######################################################################
                






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



        



    def show_ui_storage(self):




        height = 140
        if self.ui.frame_storage.height()>0:
            height = 0

        # if not(mode):
        #     height = 0
            
        self.ui.frame_storage.setMaximumHeight(height)
        self.ui.frame_storage.setMinimumHeight(height)

        # self.ui.line_current_password.setText('')
        # self.ui.line_new_password.setText('')
        # self.ui.line_confirm_password.setText('')






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
            
            # self.ui.group_camera_1.setChecked(False)
            if edit :
                group = eval('self.ui.group_camera_{}_edit'.format(iter+1))
            
            else:
                group = eval('self.ui.group_camera_{}'.format(iter+1))

                GUIBackend.set_input(self.ui.line_train_name, '')
            # group.setChecked(False)


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


    def convert_motion2bool(self,value):

        if value == 'Enable':
            return True
        
        return False



    def save_camera_config(self):
        train_name = self.get_train_name_config()
        codec_ui = GUIBackend.get_combobox_selected(self.ui.new_profile_compression)
        codec = self.mapDict.value2key('codec', codec_ui)

        motion = GUIBackend.get_combobox_selected(self.ui.new_profile_motion)
        motion = self.convert_motion2bool(motion)


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

            config = self.update_base_json(config,camera_configs,train_name, codec , motion=motion)

            self.save_json(save_name=train_name,json_data=config)

            self.clear_ui_profile()

            self.refresh_edit_profile()



    def update_base_json(self,json_data,camera_configs=None,train_name=None, codec=None,motion=None):

        if camera_configs:
            json_data['cameras'] = camera_configs
        if train_name:
            json_data ['train_id'] = train_name
        if codec:
            json_data['video_codec'] = codec
        if motion is not None : 
            json_data['motion'] = motion

        return json_data
    

    def check_train_name(self,train_name):


        reserved_names = [
            "CON", "PRN", "AUX", "NUL",
            "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
            "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
        ]

        # Invalid characters in Windows filenames
        invalid_chars = '<>:"/\\|?_*'

        only_name = train_name

        exist_json = os.listdir(CONFIG_PATH)
        train_name = train_name+'.json'

        if train_name =='.json':
            return False,'Train Name Is Empty'
        elif train_name in exist_json:
            return False,'Duplicate Name , Change Train Name'


        if train_name[0]=='.':
            return False , 'Filename Dont Start with .'

        # Check for invalid characters
        if any(char in invalid_chars for char in train_name):
            return False, "Filename contains invalid characters."

        # Check for reserved names
        if only_name.upper() in reserved_names:
            return False, "Filename is a reserved name in Windows."


        # Ensure filename is not too long
        if len(train_name) > 100:
            return False, "Filename is too long."

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


    def convert_bool2motion(self,value):

        if bool(value):
            return 'Enable'
        
        return 'Disable'



    def edit_profile(self):
        profile = self.ui.combo_train_name_profile.currentText()

        json_data = self.load_json(json_name=profile)

        train_id = json_data['train_id']
        camera_configs = json_data['cameras']
        codec = json_data['video_codec']
        motion = json_data['motion']

        codec_ui = self.mapDict.key2value('codec', codec)
        motion = self.convert_bool2motion(motion)


        GUIBackend.set_combobox_current_item(self.ui.edit_profile_compression, codec_ui)
        GUIBackend.set_combobox_current_item(self.ui.edit_profile_motion, motion)
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

            motion = GUIBackend.get_combobox_selected(self.ui.edit_profile_motion)
            motion = self.convert_motion2bool(motion)

            json_data = self.update_base_json(json_data,camera_configs, train_name=new_train_id, codec=codec,motion = motion)

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
        try:
            if status_code == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
                if msg !='':
                    self.show_message('copy', msg)
                else:
                    self.show_message('copy', 'Connection Faild. check ip and cables connections')
                GUIBackend.set_disable_enable(self.ui.btn_update_train, True)
                self.set_loading_progress_bar(False)


                ############################### LOG  ##################################
                try:
                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                                text=f"Error : Show Remote Update", 
                                                code="Mremote_update_event001")
                    self.logger.create_new_log(message=log_msg)
                except:
                    pass
                #######################################################################



                return
            
            elif status_code == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
                
                GUIBackend.set_disable_enable(self.ui.btn_update_train, False)
                tsd = updateRemote( self.ip , user_name=self.db_res['username'],password=self.db_res['password'],name=self.db_res['name'] )
                # tsd.exec()
                tsd.show()

                GUIBackend.set_disable_enable(self.ui.btn_update_train, True)



                ############################### LOG  ##################################
                try:
                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO,
                                                text=f"Show Remote Update", 
                                                code="Mremote_update_event000")
                    self.logger.create_new_log(message=log_msg)
                except:
                    pass
                #######################################################################

        except Exception as e:


            ############################### LOG  ##################################
            try:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"Error : Show Remote Update {e}", 
                                            code="Mremote_update_event003")
                self.logger.create_new_log(message=log_msg)
            except:
                pass
            #######################################################################











    def save_storage_config(self):

        try:
            min = self.ui.spinBox_min_allow.value()
            max = self.ui.spinBox_max_allow.value()

            if min>=max:
                self.show_message(name='setting_msg',txt='Max Should be Higher',disapear=2000,style=error_style)
                return
            
            else:

                max_ret = self.db.update_row_by_input(table_name='storage',column_name='max',new_value=max,condition_field='id',condition_value=0)
                min_ret = self.db.update_row_by_input(table_name='storage',column_name='min',new_value=min,condition_field='id',condition_value=0)


                ############################### LOG  ##################################
                try:
                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                                text=f"database parms updated : max{max} - {max_ret},min{min} - {min_ret}", 
                                                code="Msave_storage_config000")
                    self.logger.create_new_log(message=log_msg)
                except:
                    pass
                #######################################################################


                if max_ret and min_ret:
                    self.show_message(name='setting_msg',txt='New Values Updated',disapear=2000,style=success_style)

                else:
                    self.show_message(name='setting_msg',txt='Error in Save New Values',disapear=2000,style=error_style)

                self.load_storage_values()



        except:
            pass


    

    def load_storage_values(self):


        values = self.db.fetch_table_as_dict(table_name='storage')
        print(values)

        if values[0] !=[]:
            values = values[0]
            self.min_allowed = int(values['min'])
            self.max_allowed = int(values['max'])
            self.ui.spinBox_min_allow.setValue(self.min_allowed)
            self.ui.spinBox_max_allow.setValue(self.max_allowed)

            self.storage_obj.update_max_storage(max_usage=(self.max_allowed/100))

            self.storage_object.update_percentages(min=self.min_allowed,max = self.max_allowed)
        
        else:
            print('Error in get data from database')







    def manual_delete(self):


        

        storage_info = get_current_drive_storage(mode=Storage.B)

        total,used,free = storage_info['total_space'] , storage_info['used_space'] ,storage_info['free_space'] 
        min_allowed = 100  - self.min_allowed
        min_byte = (min_allowed*total / 100)

        if min_byte - free <0:
            self.show_message('copy','Free Space is Higher Than Minimum Threshold')
            return
        
        self.ui.copy_button.setEnabled(False)

        try:

            space_should_be_delete = Space( min_byte - free)


            self.storage_obj.send_clean_request(name='milad',size=space_should_be_delete)
            # func = transormUtils.pass_extra_arg_event(event_func=self.clening_finish_signal,extra_args=(paths,sizes))
            self.storage_obj.finish_cleaning_signal.connect(self.enble_copy_btn)
            self.storage_obj.progress_signal.connect(self.show_remove_files)

            clean_thread = threading.Thread(target=self.storage_obj.run,daemon=True)
            clean_thread.start()

        except:
            self.ui.copy_button.setEnabled(True)
            self.show_message('copy','Error in Deleting Files')

    
    def enble_copy_btn(self,name_id,status):

        self.ui.copy_button.setEnabled(True)
        if status:
            self.show_message('copy','CleanUp Finished')
        
        else:
            self.show_message('copy','Files Not Found for Deletion')





# if __name__ == "__main__":


#     os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'calendar.ui'), os.path.join('UIFiles', 'calendar.py')))


#     app = sQApplication()
#     win = UI_main_window_org()

#     win.show()
#     sys.exit(app.exec())