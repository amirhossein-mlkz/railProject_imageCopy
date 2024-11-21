# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)
# import assets_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(587, 381)
        Form.setStyleSheet(u"\n"
"/* Main window background */\n"
"QWidget {\n"
"    background-color: #2E2E2E; /* Dark gray, resembling a military interface */\n"
"}\n"
"\n"
"/* Video widget border and background */\n"
"QVideoWidget {\n"
"    background-color: #000000; /* Black background for the video */\n"
"    border: 2px solid #4B5320; /* Army green border */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Play and Pause buttons */\n"
"QPushButton {\n"
"    background-color: #4B5320; /* Army green button */\n"
"    color: #FFFFFF; /* White text */\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #808000; /* Olive border */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #556B2F; /* Dark olive green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #6B8E23; /* Light olive green when pressed */\n"
"}\n"
"\n"
"/* Video progress slider */\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #4B5320; /* Army green */\n"
"    height: 8px;\n"
" "
                        "   background-color: #3B3B3B; /* Dark gray groove */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #808000; /* Olive handle */\n"
"    border: 2px solid #4B5320;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #556B2F; /* Dark olive green on hover */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #556B2F; /* Dark olive green for the part of the slider that indicates progress */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Time label */\n"
"QLabel {\n"
"    color: #C0C0C0; /* Light gray text for the time label */\n"
"    font-family: \"Arial\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(Form)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 34))
        self.frame_top.setMaximumSize(QSize(16777215, 34))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_top)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(100, 0))
        self.frame_2.setMaximumSize(QSize(100, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 33))
        self.label_2.setMaximumSize(QSize(50, 33))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/download.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 33))
        self.label_5.setMaximumSize(QSize(50, 33))
        self.label_5.setPixmap(QPixmap(u":/icons/icons/kerman.JPG"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_5)


        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_title = QLabel(self.frame_top)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout.addWidget(self.label_title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_3 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.frame = QFrame(self.frame_top)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_maximize = QPushButton(self.frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_maximize.setStyleSheet(u"background-color:transparent;\n"
"border:None;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/maximize-army.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_maximize.setIcon(icon)
        self.btn_maximize.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(30, 16777215))
        self.btn_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_close.setStyleSheet(u"background-color:transparent;\n"
"border:None;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/exit_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_top)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame_video = QFrame(Form)
        self.frame_video.setObjectName(u"frame_video")
        font = QFont()
        font.setPointSize(12)
        self.frame_video.setFont(font)
        self.frame_video.setFrameShape(QFrame.Box)
        self.frame_video.setFrameShadow(QFrame.Raised)
        self.frame_video.setLineWidth(2)
        self.verticalLayout_2 = QVBoxLayout(self.frame_video)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout.addWidget(self.frame_video)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 56))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.play_button = QPushButton(self.frame_3)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setEnabled(True)
        self.play_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/play (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_button.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.play_button)

        self.pause_button = QPushButton(self.frame_3)
        self.pause_button.setObjectName(u"pause_button")
        self.pause_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pause_button.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.pause_button)

        self.video_slider = QSlider(self.frame_3)
        self.video_slider.setObjectName(u"video_slider")
        self.video_slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.video_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.video_slider)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.elapssed_time = QLabel(self.frame_4)
        self.elapssed_time.setObjectName(u"elapssed_time")

        self.horizontalLayout_2.addWidget(self.elapssed_time)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.duration_time = QLabel(self.frame_4)
        self.duration_time.setObjectName(u"duration_time")

        self.horizontalLayout_2.addWidget(self.duration_time)

        self.btn_fullscreen = QPushButton(self.frame_4)
        self.btn_fullscreen.setObjectName(u"btn_fullscreen")
        self.btn_fullscreen.setMinimumSize(QSize(30, 0))
        self.btn_fullscreen.setMaximumSize(QSize(40, 16777215))
        self.btn_fullscreen.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_fullscreen.setStyleSheet(u"border:none;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/maximize-size.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_fullscreen.setIcon(icon4)
        self.btn_fullscreen.setIconSize(QSize(28, 29))

        self.horizontalLayout_2.addWidget(self.btn_fullscreen)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.label_5.setText("")
        self.label_title.setText(QCoreApplication.translate("Form", u"\u0639\u0646\u0648\u0627\u0646", None))
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.play_button.setText(QCoreApplication.translate("Form", u"Play", None))
        self.pause_button.setText(QCoreApplication.translate("Form", u"Pause", None))
        self.elapssed_time.setText(QCoreApplication.translate("Form", u"00:00", None))
        self.label.setText(QCoreApplication.translate("Form", u"/", None))
        self.duration_time.setText(QCoreApplication.translate("Form", u"00:00", None))
        self.btn_fullscreen.setText("")
    # retranslateUi

