import sys
import json
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QGroupBox, QFormLayout, QScrollArea
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

# Sample JSON data
data = {
    "cameras": [
        {"name": "right", "ip": "192.168.1.18", "username": "test", "password": "test"},
        {"name": "left", "ip": "", "username": "", "password": ""},
        {"name": "3", "ip": "", "username": "", "password": ""},
        {"name": "4", "ip": "", "username": "", "password": ""}
    ],
    "path": "c:/rail_share",
    "temp_folder": "temp_videos",
    "max_allowed_storage": 0.7,
    "train_id": "11BG21",
    "motion": "false",
    "motion_sens": 3000,
    "output": "video",
    "video_fps": 25,
    "video_duration": 600,
    "name": "test4"
}

class ShowConfig(QWidget):
    def __init__(self,data):
        super().__init__()
        self.setWindowTitle("Profile Configuration")
        self.resize(500, 600)  # Set window size
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f4f4;
                color: #333;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QGroupBox {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 8px;
                margin-top: 20px;
                padding: 10px;
            }
            QGroupBox:title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 3px;
                font-weight: bold;
                color: #444;
            }
            QLabel {
                padding: 2px;
                color: #555;
            }
        """)
        
        layout = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        # Set font for headers
        header_font = QFont("Arial", 10, QFont.Bold)

        # Display cameras information
        for camera in data['cameras']:
            camera_group = QGroupBox(f"Camera: {camera['name']}")
            camera_layout = QFormLayout()
            camera_layout.addRow("IP:", QLabel(camera['ip']))
            camera_layout.addRow("Username:", QLabel(camera['username']))
            camera_layout.addRow("Password:", QLabel(camera['password']))
            camera_group.setLayout(camera_layout)
            scroll_layout.addWidget(camera_group)

        # Display other settings
        general_group = QGroupBox("General Settings")
        general_layout = QFormLayout()

        # general_layout.addRow("Path:", QLabel(data['path']))
        general_layout.addRow("Temp Folder:", QLabel(data['temp_folder']))
        general_layout.addRow("Max Storage:", QLabel(str(data['max_allowed_storage'])))
        general_layout.addRow("Train ID:", QLabel(data['train_id']))
        general_layout.addRow("Motion:", QLabel(data['motion']))
        general_layout.addRow("Motion Sensitivity:", QLabel(str(data['motion_sens'])))
        general_layout.addRow("Output:", QLabel(data['output']))
        general_layout.addRow("Video FPS:", QLabel(str(data['video_fps'])))
        general_layout.addRow("Video Duration:", QLabel(str(data['video_duration'])))
        general_group.setLayout(general_layout)
        scroll_layout.addWidget(general_group)

        scroll.setWidget(scroll_widget)
        layout.addWidget(scroll)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShowConfig()
    window.show()
    sys.exit(app.exec_())
