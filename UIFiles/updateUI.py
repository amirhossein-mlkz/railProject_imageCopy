# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(710, 306)
        Form.setStyleSheet(u"background-color:rgb(220, 221, 180);")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.topFrame = QFrame(Form)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.NoFrame)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.topFrame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.name = QLabel(self.topFrame)
        self.name.setObjectName(u"name")

        self.horizontalLayout_5.addWidget(self.name)

        self.ip = QLabel(self.topFrame)
        self.ip.setObjectName(u"ip")

        self.horizontalLayout_5.addWidget(self.ip)

        self.horizontalSpacer = QSpacerItem(624, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.topFrame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/asstets/icons/close_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.close_btn)


        self.verticalLayout_2.addWidget(self.topFrame)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 37))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gb_image_grabber = QGroupBox(self.frame_2)
        self.gb_image_grabber.setObjectName(u"gb_image_grabber")
        self.verticalLayout = QVBoxLayout(self.gb_image_grabber)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_check_version_ig = QPushButton(self.gb_image_grabber)
        self.btn_check_version_ig.setObjectName(u"btn_check_version_ig")
        self.btn_check_version_ig.setEnabled(True)
        self.btn_check_version_ig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_check_version_ig)

        self.frame_3 = QFrame(self.gb_image_grabber)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lbl_exist_version_ig = QLabel(self.frame_3)
        self.lbl_exist_version_ig.setObjectName(u"lbl_exist_version_ig")

        self.horizontalLayout_2.addWidget(self.lbl_exist_version_ig)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.gb_image_grabber)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lbl_remote_version_ig = QLabel(self.frame)
        self.lbl_remote_version_ig.setObjectName(u"lbl_remote_version_ig")

        self.horizontalLayout.addWidget(self.lbl_remote_version_ig)


        self.verticalLayout.addWidget(self.frame)

        self.btn_update_ig = QPushButton(self.gb_image_grabber)
        self.btn_update_ig.setObjectName(u"btn_update_ig")
        self.btn_update_ig.setEnabled(False)
        self.btn_update_ig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_update_ig)

        self.progressBar_ig = QProgressBar(self.gb_image_grabber)
        self.progressBar_ig.setObjectName(u"progressBar_ig")
        self.progressBar_ig.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_ig)


        self.horizontalLayout_3.addWidget(self.gb_image_grabber)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.gb_image_grabber_2 = QGroupBox(self.frame_2)
        self.gb_image_grabber_2.setObjectName(u"gb_image_grabber_2")
        self.gb_image_grabber_2.setEnabled(False)
        self.verticalLayout_4 = QVBoxLayout(self.gb_image_grabber_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_check_version_copy = QPushButton(self.gb_image_grabber_2)
        self.btn_check_version_copy.setObjectName(u"btn_check_version_copy")
        self.btn_check_version_copy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_check_version_copy)

        self.frame_7 = QFrame(self.gb_image_grabber_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lbl_exist_version_copy = QLabel(self.frame_7)
        self.lbl_exist_version_copy.setObjectName(u"lbl_exist_version_copy")

        self.horizontalLayout_7.addWidget(self.lbl_exist_version_copy)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.gb_image_grabber_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lbl_remote_version_copy = QLabel(self.frame_8)
        self.lbl_remote_version_copy.setObjectName(u"lbl_remote_version_copy")

        self.horizontalLayout_8.addWidget(self.lbl_remote_version_copy)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.btn_update_copy = QPushButton(self.gb_image_grabber_2)
        self.btn_update_copy.setObjectName(u"btn_update_copy")
        self.btn_update_copy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_update_copy)

        self.progressBar_copy = QProgressBar(self.gb_image_grabber_2)
        self.progressBar_copy.setObjectName(u"progressBar_copy")
        self.progressBar_copy.setValue(0)

        self.verticalLayout_4.addWidget(self.progressBar_copy)


        self.horizontalLayout_3.addWidget(self.gb_image_grabber_2)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.gb_image_grabber_3 = QGroupBox(self.frame_2)
        self.gb_image_grabber_3.setObjectName(u"gb_image_grabber_3")
        self.gb_image_grabber_3.setEnabled(False)
        self.verticalLayout_5 = QVBoxLayout(self.gb_image_grabber_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_check_version_server = QPushButton(self.gb_image_grabber_3)
        self.btn_check_version_server.setObjectName(u"btn_check_version_server")
        self.btn_check_version_server.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_check_version_server)

        self.frame_9 = QFrame(self.gb_image_grabber_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lbl_exist_version_server = QLabel(self.frame_9)
        self.lbl_exist_version_server.setObjectName(u"lbl_exist_version_server")

        self.horizontalLayout_9.addWidget(self.lbl_exist_version_server)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.gb_image_grabber_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lbl_remote_version_server = QLabel(self.frame_10)
        self.lbl_remote_version_server.setObjectName(u"lbl_remote_version_server")

        self.horizontalLayout_10.addWidget(self.lbl_remote_version_server)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.btn_update_server = QPushButton(self.gb_image_grabber_3)
        self.btn_update_server.setObjectName(u"btn_update_server")
        self.btn_update_server.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_update_server)

        self.progressBar_server = QProgressBar(self.gb_image_grabber_3)
        self.progressBar_server.setObjectName(u"progressBar_server")
        self.progressBar_server.setValue(0)

        self.verticalLayout_5.addWidget(self.progressBar_server)


        self.horizontalLayout_3.addWidget(self.gb_image_grabber_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 38))
        self.frame_4.setMaximumSize(QSize(16777215, 35))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_msg = QLabel(self.frame_4)
        self.lbl_msg.setObjectName(u"lbl_msg")

        self.horizontalLayout_4.addWidget(self.lbl_msg, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Remote : ", None))
        self.name.setText("")
        self.ip.setText("")
        self.close_btn.setText("")
        self.gb_image_grabber.setTitle(QCoreApplication.translate("Form", u"Image Grabber", None))
        self.btn_check_version_ig.setText(QCoreApplication.translate("Form", u"Check Version", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Exist Version :", None))
        self.lbl_exist_version_ig.setText(QCoreApplication.translate("Form", u"-", None))
        self.label.setText(QCoreApplication.translate("Form", u"Remote Version :", None))
        self.lbl_remote_version_ig.setText(QCoreApplication.translate("Form", u"-", None))
        self.btn_update_ig.setText(QCoreApplication.translate("Form", u"Start Update", None))
        self.gb_image_grabber_2.setTitle(QCoreApplication.translate("Form", u"Copy", None))
        self.btn_check_version_copy.setText(QCoreApplication.translate("Form", u"Check Version", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Exist Version :", None))
        self.lbl_exist_version_copy.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Remote Version :", None))
        self.lbl_remote_version_copy.setText(QCoreApplication.translate("Form", u"-", None))
        self.btn_update_copy.setText(QCoreApplication.translate("Form", u"Start Update", None))
        self.gb_image_grabber_3.setTitle(QCoreApplication.translate("Form", u"Server", None))
        self.btn_check_version_server.setText(QCoreApplication.translate("Form", u"Check Version", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Exist Version :", None))
        self.lbl_exist_version_server.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Remote Version :", None))
        self.lbl_remote_version_server.setText(QCoreApplication.translate("Form", u"-", None))
        self.btn_update_server.setText(QCoreApplication.translate("Form", u"Start Update", None))
        self.lbl_msg.setText("")
    # retranslateUi

