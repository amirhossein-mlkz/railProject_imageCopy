from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtCore import QTimer


import hashlib,sys


class LoginPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):

        # Remove window close button and add rounded corners
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Window)
        self.pos_ = self.pos()
        self._old_pos = None

        # Create widgets
        self.password_label = QLabel('Password:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password input

        self.error_label = QLabel('', self)  # Label for displaying error messages
        self.error_label.setStyleSheet("color: red;")  # Set the error message color to red

        self.login_button = QPushButton('Login', self)
        # self.login_button.setDefault(True)  # This makes the button triggered by Enter key
        self.close_button = QPushButton('Close', self)

        # Set up layouts
        main_layout = QVBoxLayout()

        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.close_button)

        main_layout.addLayout(password_layout)
        main_layout.addWidget(self.error_label)  # Add error label to the layout
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Set styles
        self.setStyleSheet("""
            QWidget#LoginPage {
                background-color: #f0f0f0;
                border: 2px solid #007BFF;
                border-radius: 15px;
                                        
                           
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLineEdit {
                font-size: 14px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #fff;
            }
            QPushButton {
                font-size: 14px;
                padding: 5px 10px;
                border: 1px solid #007BFF;
                border-radius: 5px;
                background-color: #007BFF;
                color: white;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #003d80;
            }
        """)

        # Connect buttons

        self.setWindowTitle('Login Page')
        self.setGeometry(300, 150, 300, 150)

    def show(self,):
        self.write_error('')
        self.password_input.setText('')
        super().show()
        self.centerOnParent()

    


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.login_button.click()  # Simulate a button click





    def write_error(self, txt:str, t=2000):
        self.error_label.setText(txt)
        if txt:
            timer = QTimer()
            timer.singleShot(t, lambda: self.write_error(''))
        
    def centerOnParent(self):
        if self.parent():
            parent_geometry = self.parent().geometry()
            self_geometry = self.frameGeometry()
            center_point = parent_geometry.center()
            self_geometry.moveCenter(center_point)
            self.move(self_geometry.topLeft())

    def login_button_connector(self, func):
        self.login_button.clicked.connect(func)

    def close_button_connector(self, func):
        self.close_button.clicked.connect( func )
        
    
    def get_hash_pass(self, ):
        password = self.password_input.text()
        if password == '':
            return password
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return password_hash


    def convert_pass2hash(self,password):


        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return password_hash


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_page = LoginPage()
    sys.exit(app.exec())