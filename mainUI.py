
from PySide6 import QtCore as sQtCore
from PySide6.QtWidgets import QMainWindow as sQMainWindow
from PySide6.QtWidgets import QApplication as sQApplication
import sqlite3
import sys,os,platform,time,subprocess,threading
from database import DataBase
# from copy_ping import ShareCopyWorker
from persiantools.jdatetime import JalaliDateTime
import jdatetime
from Calendar import  JalaliCalendarDialog
from guiBackend import GUIBackend
from PySide6.QtCore import QTimer
from login import LoginPage
from PySide6.QtWidgets import QGraphicsBlurEffect

from UIFiles.main_UI import Ui_main
from uiUtils.GUIComponents import single_timer_runner

from Tranform.transformModule import transformModule
from Tranform.sharingConstans import StatusCodes





# ui class
class mainUI(sQMainWindow):

    def __init__(self):
        super().__init__()


        self.ui = Ui_main()
        self.ui.setupUi(self)

        self.login_ui = LoginPage(self)
        self.login_ui.login_button_connector(self.check_password)
        self.login_ui.close_button_connector(self.close_login)

        # window setup
        flags = sQtCore.Qt.WindowFlags(
            sQtCore.Qt.FramelessWindowHint
        )  # remove the windows frame of ui
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self._old_pos = None
        self.show_timeline(mode=False) 
        self.ui.stackedWidget.setCurrentWidget(self.ui.copy)
        self.db = DataBase('data.db')
        self.button_connector()
        self.load_fields()
        self.load_pathes()


        self.fields_msg = {
            'ip': self.ui.ip_address_msg,
            'username': self.ui.username_msg,
            'password': self.ui.password_msg,
            'copy': self.ui.copy_log_lbl,
        }
        

     

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

        self.preview_login = False
        self.all_style_repoblish()
        self.startup()

    def startup(self,):
        for name in self.fields_msg.keys():
            self.show_message(name, None)


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
        self.ui.minimize_btn.clicked.connect(self.minimize_win)
        self.ui.save_btn_ip.clicked.connect(self.save_ip)
        self.ui.save_btn_username.clicked.connect(self.save_username)
        self.ui.save_btn_password.clicked.connect(self.save_password)
        self.ui.copy_button.clicked.connect(self.ui_copy)
        self.ui.side_copy_btn.clicked.connect(self.set_stack_widget)
        self.ui.side_profile_btn.clicked.connect(self.set_stack_widget)
        self.ui.timeline_btn.clicked.connect(self.show_login)
        self.ui.timeline_copy_btn.clicked.connect(self.time_line_copy)

    def show_login(self):
        GUIBackend.set_disable_enable(self.ui.timeline_copy_btn, False)
        self.applyBlurEffect()
        self.login_ui.show()

    def close_login(self):
        GUIBackend.set_disable_enable(self.ui.timeline_copy_btn, True)
        self.login_ui.close()

    def check_password(self):

        password = self.login_ui.get_hash_pass()
        if password == '':
            self.login_ui.write_error('Please Enter Password')
            return
        

        
        passwords_db = self.db.fetch_table_as_dict(table_name='password')
        for pass_db in passwords_db:    
            if str(password) == str(pass_db['password']):
                self.login_ui.close()
                self.show_timeline(mode=True)

            else:
                self.login_ui.write_error("Password is Incorrect")

    def time_line_copy(self):
        self.show_timeline(mode=False)

        if  self.ui.start_date.text() !='' and  self.ui.end_date.text() !='':

            start_time={}
            get_date = self.calenders['start'].date
            # get_date = get_date.jdate()
            get_time = self.ui.timeEdit_end.time()
            h = get_time.hour()
            m = get_time.minute()

            start_time = get_date.replace(hour=h,minute=m)


            print(start_time)


            get_time = self.ui.timeEdit_end.time()
            h = get_time.hour()
            m = get_time.minute()
            get_date = self.ui.end_date.text().split('/')
            end_time = JalaliDateTime.now()
            end_time = end_time.replace(year=int(get_date[0]),month=int(get_date[1]),day = int(get_date[2]), hour=h,minute=m)

            print(end_time)

            if end_time<start_time:
                print('End time should be bigger than start time')
                self.show_error('End time should be bigger than start time')

            else:

                print('Start Doing Copy')

                self.image_condition = {'start':start_time,'end':end_time}
                self.start_copy(image_condition=self.image_condition)











    def covert_date(self,jdatetime):
        date = jdatetime.strftime('%Y/%m/%d')
        return date
    
    def set_stack_widget(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "side_copy_btn":
            self.ui.stackedWidget.setCurrentWidget(self.ui.copy)
        if btnName == "side_profile_btn":
            self.ui.stackedWidget.setCurrentWidget(self.ui.profile)


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
        self.close()
        # pid = os.getpid()
        # os.kill(pid, SIGKILL)
        sys.exit()

    def minimize_win(self):
        self.showMinimized()

    def load_fields(self):
        res = self.db.fetch_table_as_dict()
        if len(res)==1:
            res = res[0]
            self.ui.ip_input.setText(res['ip'])
            self.ui.username_input.setText(res['username'])
            self.ui.password_input.setText(res['password'])

    
    def show_message(self, name, txt, disapear=None):
        if txt:
            # GUIBackend.set_wgt_visible(self.fields_msg[name], True)
            GUIBackend.set_label_text(self.fields_msg[name], txt)
            if disapear is not None:
                timer = QTimer()
                timer.singleShot(disapear, lambda: self.show_message(name, None))
        else:
            txt = ''
            GUIBackend.set_label_text(self.fields_msg[name], txt)
            # GUIBackend.set_wgt_visible(self.fields_msg[name], False)
            

        

    def save_ip(self):
        self.db.update_row_by_id_zero(column_name='ip',new_value=self.ui.ip_input.text())
        self.show_message('ip', 'saved successfuly', disapear=2000)
        

    def save_username(self):
        self.db.update_row_by_id_zero(column_name='username',new_value=self.ui.username_input.text())
        self.show_message('username', 'saved successfuly', disapear=2000)
        

    def save_password(self):
        self.db.update_row_by_id_zero(column_name='password',new_value=self.ui.password_input.text())
        self.show_message('password', 'saved successfuly', disapear=2000)
        

    def load_pathes(self):
        res = self.db.fetch_table_as_dict(table_name='pathes')
        if len(res)==1:
            res = res[0]
            self.src_path = res['folder_to_copy']
            self.dst_path = res['destination_folder']


    def ui_copy(self):

        self.show_timeline(mode=False) 
        self.start_copy()

    




    def start_copy(self,image_condition=None):
        ip = self.ui.ip_input.text()
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        src_path = self.src_path
        dst_path = self.dst_path

        self.trasformer = transformModule(ip, src_path, dst_path, username, password)
        self.show_message('copy', 'Check Connection...')
        GUIBackend.set_disable_enable(self.ui.copy_button, False)
        self.trasformer.check_connection(self.step1_check_connection_event)


    def step1_check_connection_event(self, status_code):
        if status_code == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            self.show_message('copy', 'Connection Faild. check ip and cables connections')
            GUIBackend.set_disable_enable(self.ui.copy_button, True)
            return
        
        elif status_code == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
            self.show_message('copy', 'Searching Files...')
            self.trasformer.find_files( trains= None,
                                        dates_tange=None,
                                        finish_event_func=self.step2_files_list_ready_event,
                                        log_event_func=self.step1_log_event)

    def step1_log_event(self, log:str):
        txt = f'Searching Files: {log}'
        self.show_message('copy', txt)

    def step2_files_list_ready_event(self, 
                                     status_code, 
                                     paths:list[str], 
                                     sizes:list[int], 
                                     avaiabilities:dict[str,dict[str, list]]):
        
        if status_code == StatusCodes.findFilesStatusCodes.DIR_NOT_EXISTS:
            self.show_message('copy', "Path dosen't exists")
            GUIBackend.set_disable_enable(self.ui.copy_button, True)
            return
        


        if len(paths) == 0:
            GUIBackend.set_disable_enable(self.ui.copy_button, True)
            self.show_message('copy', 'No Files Found to Copy')
            return

        self.ui.progress_bar.setMinimum(0)
        self.ui.progress_bar.setMaximum(100)
        self.ui.progress_bar.setValue(0)
        self.trasformer.start_copy(paths, 
                                   sizes, 
                                   finish_func=self.step3_copy_finish_event,
                                   speed_func=self.step2_update_speed,
                                   progress_func=self.step2_update_progress,
                                   msg_callback=self.step2_log )

    def step2_update_progress(self, completed:int, total:int):
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
            return
        # a = transormUtils.dateTimeRanges( avaiabilities['11BG21']['right'], 600 )
        GUIBackend.set_disable_enable(self.ui.copy_button, True)
        self.show_message('copy', "Finish Success")
        



    def show_timeline(self,mode):
        self.ui.frame_date.setVisible(mode) 

        



    def applyBlurEffect(self):
        current_effect = self.graphicsEffect()
        if current_effect:
            self.setGraphicsEffect(None)
        else:
            blur_effect = QGraphicsBlurEffect()
            blur_effect.setBlurRadius(10)
            self.setGraphicsEffect(blur_effect)









# if __name__ == "__main__":


#     os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'calendar.ui'), os.path.join('UIFiles', 'calendar.py')))


#     app = sQApplication()
#     win = UI_main_window_org()

#     win.show()
#     sys.exit(app.exec())