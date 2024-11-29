from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QProgressBar , QPushButton , QMessageBox , QHBoxLayout,QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt
import shutil
import os
import threading
# from guiBackend import GUIBackend


GB = 'GB'
MB = 'MB'

# Function to get drive storage information
def get_current_drive_storage(drive_root=r'C:\\',mode = GB):
    try:
        total, used, free = shutil.disk_usage(drive_root)
        if mode == GB:
            total = total / (1024 ** 3)
            free = free / (1024 ** 3)
            used = total - free

        elif mode == MB:

            total = total / (1024 ** 2)
            free = free / (1024 ** 2)
            used = total - free


        return {
            "drive": drive_root,
            "total_space": round(total, 2),
            "used_space": round(used, 2),
            "free_space": round(free, 2),
        }
    

    except:


        return {
            "drive": drive_root,
            "total_space":0,
            "used_space":0,
            "free_space": 0,
        }




def conver_GB2MB(size):

    return size/1024




# Modernized StorageWidget
class StorageWidget(QWidget):


    GB = 'GB'
    MB = 'MB'

    def __init__(self,path,percentage_max_allowed = 89 ,percentage_low_limit = 88):
        super().__init__()
        self.setStyleSheet(self.get_stylesheet("#4CAF50"))
        self.setContentsMargins(0, 0, 0, 0)

        self.percentage_max_allowed = percentage_max_allowed
        self.percentage_low_limit = percentage_low_limit

        self.start_cleaning = False
        self.path = path
        # Layout setup
        layout = QHBoxLayout()
        layout.setSpacing(0)


        self.progress_bar = QProgressBar()

        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFixedHeight(25)
        layout.addWidget(self.progress_bar)


        # Add 20px vertical space
        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        layout.addItem(spacer)

        # Action button (initially disabled)
        self.action_button = QPushButton("ClenUp")
        self.action_button.setEnabled(True)
        self.action_button.clicked.connect(self.handle_confirmation)
        self.action_button.setStyleSheet(self.get_cleanup_button_stylesheet())
        self.action_button.setMaximumHeight(30)
        self.action_button.setMinimumHeight(30)
        layout.addWidget(self.action_button)

        self.setLayout(layout)




        # Set layout
        self.setLayout(layout)


        self.timer_checker()




    def timer_checker(self):

        # try:
        self.update_storage()
        # except:
        #     pass

        threading.Timer(30,self.timer_checker).start()




    def get_storage(self,mode=GB):
        storage_info = get_current_drive_storage(mode=mode)
        return storage_info



    def update_storage(self):
        storage_info = get_current_drive_storage()
        self.set_storage(storage_info=storage_info)


    def set_storage(self,storage_info,mode=GB):
        # Progress bar for used space
        if mode==GB:
            used_percentage = (storage_info['used_space'] / storage_info['total_space']) * 100

        elif mode == MB:
            used_percentage = (storage_info['used_space'] *1024 / storage_info['total_space']*1024) * 100



        self.progress_bar.setValue(int(used_percentage))
        self.progress_bar.setFormat("Used: %.2f GB (%.0f%%)" % (storage_info['used_space'], used_percentage))


        if used_percentage > self.percentage_max_allowed:

            self.progress_bar.setStyleSheet(self.get_stylesheet(color="#FF0000"))

            if not self.start_cleaning:
                self.action_button.setVisible(True)  # Enable action button
        else:
            self.progress_bar.setStyleSheet(self.get_stylesheet(color="#4CAF50"))
            self.action_button.setVisible(False)  # Disable action button



    def show_confirm_button(self):
        self.confirm_button.setVisible(True)

    def handle_confirmation(self):

        
        # QMessageBox.information(self, "Action Confirmed", "You confirmed the action!")

        ret = self.show_question(title='CleanUp',message='Are you sure you want to clean up?')
        if ret:

            ret , space_should_be_clean_MB = self.calc_space_need()

            if ret:

                self.start(space_should_be_clean_MB=space_should_be_clean_MB)
            
            else:
                print('dont need delete')



    def calc_space_need(self):

        space_should_be_clean_MB =0

        storage_info = get_current_drive_storage(mode = MB)

        free_percentage = (storage_info['free_space']  / storage_info['total_space']) * 100

        if free_percentage > (100-self.percentage_max_allowed):
            return False,space_should_be_clean_MB
        
        
        low_limit = ((100-self.percentage_low_limit) *  storage_info['total_space']) / 100

        space_should_be_clean_MB = low_limit - storage_info['free_space']

        return True , space_should_be_clean_MB





    def start(self, space_should_be_clean_MB = 1000 ):

        storage_info = get_current_drive_storage(mode = MB)

        start_used_space = storage_info['used_space']
        target_used_space = start_used_space - space_should_be_clean_MB
        self.start_cleaning = True
        
        while True:
            storage_info = get_current_drive_storage(mode = MB)
            used_space = storage_info['used_space']

            if target_used_space>used_space:
                print('Cleaning Done')
                break
            
            res = self.get_oldets_files(self.path,1)
            

            # if free_space > space_should_be_clean_MB:
                # break
            # else:
            #     pass
                ####get path 
                ######### delete

            self.set_storage(storage_info=storage_info,mode=MB)

            break   ##############  TEMP



    def check_storage(self,needed_size_MB):

        storage_info = self.get_storage(mode=MB)

        free_space = storage_info['free_space']

        if free_space<=needed_size_MB:

            return False,'Need More Space {}'.format(needed_size_MB-free_space)
        
        else:
            return True , 'Space is Enough'

    



    

    def __sort_file_number(self, files:list[str]):
        def key(x):
            try:
                return int(x)
            except:
                return 0
        files.sort(key=key)
        return files


    def get_oldets_files(self,path, n=1) -> list[list[str]]:
        results = []
        for train in os.listdir(path):
            train_path = os.path.join(self.path, train)
            if not os.path.isdir(train_path):
                continue

            for cam in os.listdir(train_path):
                cam_path = os.path.join(train_path, cam)
                if not os.path.isdir(cam_path):
                    continue
                
                years = os.listdir(cam_path)
                years = self.__sort_file_number(years)

                last_hours_paths_per_cam = []

                for year in years:
                    year_path = os.path.join(cam_path, year)
                    if not os.path.isdir(year_path):
                        continue
                    months = os.listdir(year_path)
                    months = self.__sort_file_number(months)
                    for month in months:
                        month_path = os.path.join(year_path, month)
                        if not os.path.isdir(month_path):
                            continue
                        days = os.listdir(month_path)
                        days = self.__sort_file_number(days)
                        for day in days:
                            day_path = os.path.join(month_path, day)
                            if not os.path.isdir(day_path):
                                continue
                            hours = os.listdir(day_path)
                            hours = self.__sort_file_number(hours)

                            for hour in hours:
                                houre_path = os.path.join(day_path, hour)
                                if not os.path.isdir(houre_path):
                                    continue
                                last_hours_paths_per_cam.append(houre_path)
                                if len(last_hours_paths_per_cam) >= n:
                                    break
                            if len(last_hours_paths_per_cam) >= n:
                                break
                        if len(last_hours_paths_per_cam) >= n:
                                break
                    if len(last_hours_paths_per_cam) >= n:
                                break
                
                results.append(last_hours_paths_per_cam)
        return results
                























    def show_question(self, title, message, question=True):
        # Create the custom QMessageBox
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # Set the font size to 20 for the message box
        # font = QFont()
        # font.setPointSize(10)
        # msg_box.setFont(font)

        if question:
            # Add custom buttons for "بلی" and "خیر"
            yes_button = msg_box.addButton("Yes", QMessageBox.YesRole)
            # # yes_button.setFont(font)
            yes_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px; padding: 5px 10px;")
        
            no_button = msg_box.addButton("No", QMessageBox.NoRole)
            # # no_button.setFont(font)
            no_button.setStyleSheet("background-color: red; color: white; border-radius: 5px; padding: 5px 10px;")


            # # Set default button (optional)
            # msg_box.setDefaultButton(no_button)

            # Execute and check which button was clicked
            msg_box.exec_()

            if msg_box.clickedButton() == no_button:
                return False
            if msg_box.clickedButton() == yes_button:
                return True

        else:
            # Add the "تایید" button for simple confirmations
            ok_button = msg_box.addButton("Confirm", QMessageBox.AcceptRole)

            # Execute and check if Ok (or تایید) was clicked
            msg_box.exec_()

            if msg_box.clickedButton() == ok_button:
                return True










    # @staticmethod
    def get_stylesheet(self,color="#4CAF50"):
        return f"""
        QProgressBar {{
            border: 1px solid #d3d3d3;
            border-radius: 0px;
            text-align: center;
            background: #f0f0f0;
            color:white;
        }}
        QProgressBar::chunk {{
            background-color: {color};
            border-radius: 0px;
        }}
        """

    def get_cleanup_button_stylesheet(self):
        return """
        QPushButton {
            background-color: #FF4C4C;  /* Bright red */
            color: white;  /* Text color */
            border: none;
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 14px;
            font-weight: bold;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }

        QPushButton:hover {
            background-color: #FF3333;  /* Darker red on hover */
            transform: scale(1.05);  /* Slight enlargement */
        }

        QPushButton:pressed {
            background-color: #CC0000;  /* Even darker red when pressed */
            transform: scale(0.95);  /* Slight shrinkage */
        }

        QPushButton:disabled {
            background-color: #FFA1A1;  /* Light red for disabled */
            color: #FFFFFF;  /* Keep the text readable */
            border: none;
        }
    """
















# MainWindow to integrate StorageWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Drive Storage UI")
        # self.setMinimumSize(400, 300)

        # Add the StorageWidget to the main window
        storage_widget = StorageWidget(path='C:\image_share')
        self.setCentralWidget(storage_widget)

# Application entry point
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
