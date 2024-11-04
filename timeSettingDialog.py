from datetime import datetime
import os

from PySide6.QtWidgets import QDialog
from persiantools.jdatetime import JalaliDateTime
from PySide6.QtCore import QTimer

from UIFiles.timeSync_UI import Ui_SysncTImeDialog
from timeSetting import timeSetting
from uiUtils.guiBackend import GUIBackend
from Tranform.transformUtils import transormUtils
from pathConstans import pathConstants

class timeSettingDialog(QDialog):

    def __init__(self, ip,):
        super().__init__()


        self.ui = Ui_SysncTImeDialog()
        self.ui.setupUi(self)

        self.ip = ip

        GUIBackend.button_connector(self.ui.sync_btn, self.sync_time)
        self.setup()
    
    

    def setup(self,):
        remote_time, local_time = timeSetting.get_time_from_remote_system(self.ip)
        if remote_time is None or local_time is None:
            self.show_error("Some Error Happend Plase Try Again")
            self.ui.sync_btn.hide()

        
        else:
            self.show_error(None)
            self.ui.sync_btn.show()

            self.remote_jtime = JalaliDateTime.fromtimestamp(remote_time.timestamp())
            self.local_jtime = JalaliDateTime.fromtimestamp(local_time.timestamp())
            self.remote_time = remote_time
            self.local_time = local_time

            self.ui.system_time_lbl.setText(self.local_jtime.strftime('%Y/%m/%d  %H:%M'))
            self.ui.train_system_time_lbl.setText(self.remote_jtime.strftime('%Y/%m/%d  %H:%M'))


            diff = (self.remote_jtime - self.local_jtime).total_seconds()
            if abs(diff) > 10:
                self.ui.sync_warning.show()
            else:
                self.ui.sync_warning.hide()
        
        self.ui.loadingframe.hide()

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


    def sync_time(self, ):
        self.ui.loadingframe.show()
        path = transormUtils.build_share_path(self.ip, pathConstants.OTHER_CLOCK_SHARE_PATH,)

        status, result = transormUtils.run_with_timeout(
                        func=timeSetting.save_time_setting,
                        timeout=2,
                        path=path, 
                        local_time = self.local_time, 
                        remote_time = self.remote_time
                    )
        if status:
            #timeSetting.save_time_setting(path, self.local_time, self.remote_time)

            GUIBackend.set_disable_enable(self.ui.sync_btn, False)
            timer = QTimer()
            timer.singleShot(1000, self.check_time_is_update)

        else:
            self.show_error('Disconnected', disapear=2000)
            self.ui.loadingframe.hide()


    def check_time_is_update(self,):
        path = transormUtils.build_share_path(self.ip, pathConstants.OTHER_CLOCK_SHARE_PATH,)
        timeout_status, res = transormUtils.run_with_timeout( func= os.path.exists,
                                        timeout=2,
                                        path=path
                                        )
        if timeout_status: 
            #check file not exist        
            if not res:
                self.setup()
                self.ui.loadingframe.hide()
                GUIBackend.set_disable_enable(self.ui.sync_btn, True)
            else:
                timer = QTimer()
                timer.singleShot(1000, self.check_time_is_update)
        else:
            self.show_error('Disconnected', disapear=2000)
            self.ui.loadingframe.hide()



