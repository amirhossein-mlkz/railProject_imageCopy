import json
import os, sys, threading, time
from PySide6.QtCore import QThread, Signal, QObject, QTimer, Qt
from PySide6.QtGui import QMovie , QFont, QColor, QPalette
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from jdatetime import datetime as JalaliDateTime
from Tranform.transformUtils import transormUtils
from PySide6.QtWidgets import QApplication as sQApplication


DEBUG = True

# Worker class for running the process in another thread
class Worker(QObject):
    finished = Signal()
    error = Signal(str)

    def __init__(self, avaiabilities, dst_exist_videos_path):
        super().__init__()
        self.avaiabilities = avaiabilities
        self.dst_exist_videos_path = dst_exist_videos_path

    def run(self):
        
        try:
            if self.avaiabilities != {}:
                for train_name in self.avaiabilities.keys():
                    train = self.avaiabilities[train_name]
                    if DEBUG:
                        time.sleep(3)
                    else:
                        for camera in train.keys():
                            try:
                                date_times = train[camera]
                                times = transormUtils.dateTimeRanges(date_times=date_times, step_lenght_sec=600, max_gap_sec=10)
                                train[camera] = times
                            except Exception as e:
                                print(f'Error in Convert timtimes to ranges: {e}')

            json_exist_videos = self.dst_exist_videos_path

            if os.path.exists(json_exist_videos):
                os.remove(json_exist_videos)

            with open(json_exist_videos, 'w', encoding='utf-8') as f:
                if DEBUG:
                    print('asd')
                    # json.dump(self.avaiabilities, f, ensure_ascii=False, indent=4)
                else:
                    json.dump(self.avaiabilities, f, ensure_ascii=False, indent=4, default=self.custom_json_handler)

            self.finished.emit()
        
        except Exception as e:
            self.error.emit(str(e))


# Main widget class with automatic processing
class WidgetUpdateExistVideos(QWidget):
    def __init__(self, avaiabilities, dst_exist_videos_path, parent=None):
        super().__init__(parent)
        self.avaiabilities = avaiabilities
        self.dst_exist_videos_path = dst_exist_videos_path
        self.thread = None

        # Remove window frame and make it fully transparent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Create the UI elements
        self.center_widgets()
        self.set_transparency(1)




    def set_transparency(self, opacity_value):
        palette = self.palette()
        transparent_color = QColor(0, 0, 0, int(opacity_value * 255))  # Adjust opacity
        palette.setColor(QPalette.Window, transparent_color)
        self.setPalette(palette)


    def center_widgets(self):
        # Set layout with centered alignment
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)  # Center everything vertically and horizontally

        # Create a label to show the loading GIF
        self.loading_label = QLabel(self)
        self.loading_movie = QMovie("UIFiles\\Assets\\icons\\loading6.gif")
        self.loading_label.setMovie(self.loading_movie)

        # Add loading label to the layout
        layout.addWidget(self.loading_label, alignment=Qt.AlignCenter)

        # Label for transparency percentage or status
        self.status_label = QLabel("Initializing...", self)
        self.status_label.setStyleSheet("color: white; font-size: 24px;")  # Font size 24px
        layout.addWidget(self.status_label, alignment=Qt.AlignCenter)  # Center the label

        self.setLayout(layout)



    def showEvent(self, event):
        self.status_label.setText("Local Updateing .... ")
        self.loading_movie.start()
        self.process_in_thread(self.avaiabilities)
        if self.parent() is None:
            self.center_on_screen()
        else:
            self.center_on_parent()

    def process_in_thread(self, avaiabilities):
        self.thread = QThread()
        self.worker = Worker(avaiabilities, self.dst_exist_videos_path)
        self.worker.moveToThread(self.thread)

        self.worker.finished.connect(self.on_finished)
        self.worker.error.connect(self.on_error)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)

        self.copy_thread = threading.Thread(target=self.worker.run, daemon=True)
        self.copy_thread.start()

    def on_finished(self):
        # Display "completed" GIF
        self.status_label.setText(" Update Completed ")

        self.loading_movie.stop()
        self.loading_movie = QMovie("UIFiles\Assets\icons\loading1.gif")
        self.loading_label.setMovie(self.loading_movie)
        self.loading_movie.start()

        # Show GIF for 1 second before closing
        QTimer.singleShot(1000, self.close)

    def on_error(self, error_message):
        self.status_label.setText(f"Error occurred: {error_message}")
        self.close()







    def center_on_screen(self):
        # Get the geometry of the screen
        screen_geometry = self.screen().geometry()

        # Calculate x, y position to center the widget
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        # Move the widget to the center
        self.move(x, y)


    def center_on_parent(self):
        # Get the geometry of the parent window
        parent_geometry = self.parent().geometry()

        # Calculate x, y position to center the widget within the parent
        x = parent_geometry.x() + (parent_geometry.width() - self.width()) // 2
        y = parent_geometry.y() + (parent_geometry.height() - self.height()) // 2

        # Move the widget to the center of the parent window
        self.move(x, y)




if __name__ == "__main__":
    path = r'C:\test_share\rail_share\utils\ExistVideos.json'
    with open(path, 'r', encoding='utf-8') as f:
        available = json.load(f)

    app = sQApplication()
    win = WidgetUpdateExistVideos(avaiabilities=available, dst_exist_videos_path='test.json')

    win.show()
    sys.exit(app.exec())
