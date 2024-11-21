# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timeSyncUI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_SysncTImeDialog(object):
    def setupUi(self, SysncTImeDialog):
        if not SysncTImeDialog.objectName():
            SysncTImeDialog.setObjectName(u"SysncTImeDialog")
        SysncTImeDialog.resize(497, 230)
        SysncTImeDialog.setMinimumSize(QSize(0, 230))
        SysncTImeDialog.setMaximumSize(QSize(16777215, 230))
        icon = QIcon()
        icon.addFile(u":/asstets/icons/refresh_5730689.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SysncTImeDialog.setWindowIcon(icon)
        SysncTImeDialog.setStyleSheet(u"SysncTImeDialog{\n"
"	background-color: rgb(243, 243, 243);\n"
"}")
        self.verticalLayout = QVBoxLayout(SysncTImeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 7, -1, -1)
        self.sync_warning = QLabel(SysncTImeDialog)
        self.sync_warning.setObjectName(u"sync_warning")
        self.sync_warning.setStyleSheet(u"font-weight:bold;\n"
"color:rgb(230, 63, 66);")

        self.horizontalLayout.addWidget(self.sync_warning)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label = QLabel(SysncTImeDialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight:bold")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(SysncTImeDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-weight:bold")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.system_time_lbl = QLabel(SysncTImeDialog)
        self.system_time_lbl.setObjectName(u"system_time_lbl")

        self.gridLayout.addWidget(self.system_time_lbl, 0, 1, 1, 1)

        self.train_system_time_lbl = QLabel(SysncTImeDialog)
        self.train_system_time_lbl.setObjectName(u"train_system_time_lbl")

        self.gridLayout.addWidget(self.train_system_time_lbl, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.loadingframe = QFrame(SysncTImeDialog)
        self.loadingframe.setObjectName(u"loadingframe")
        self.loadingframe.setMinimumSize(QSize(0, 0))
        self.loadingframe.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.loadingframe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.progressBar = QProgressBar(self.loadingframe)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.label_2 = QLabel(self.loadingframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.loadingframe)

        self.error_lbl = QLabel(SysncTImeDialog)
        self.error_lbl.setObjectName(u"error_lbl")
        self.error_lbl.setStyleSheet(u"color:rgb(230, 63, 66);")
        self.error_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.error_lbl)

        self.sync_btn = QPushButton(SysncTImeDialog)
        self.sync_btn.setObjectName(u"sync_btn")
        self.sync_btn.setEnabled(True)
        self.sync_btn.setMinimumSize(QSize(150, 27))
        self.sync_btn.setMaximumSize(QSize(150, 16777215))
        self.sync_btn.setSizeIncrement(QSize(0, 0))
        self.sync_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"background-color: rgb(85, 85, 255);\n"
"border: 1px solid  rgb(85, 85, 255);\n"
"border-radius:12px;\n"
"min-height: 25px;\n"
"color:#fff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(71, 71, 213);	\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: rgb(185, 185, 185);\n"
"border: 1px solid  rgb(185, 185, 185);\n"
"}")

        self.verticalLayout.addWidget(self.sync_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(SysncTImeDialog)

        QMetaObject.connectSlotsByName(SysncTImeDialog)
    # setupUi

    def retranslateUi(self, SysncTImeDialog):
        SysncTImeDialog.setWindowTitle(QCoreApplication.translate("SysncTImeDialog", u"Sync TIme", None))
        self.sync_warning.setText(QCoreApplication.translate("SysncTImeDialog", u"WARNING: The system times are not synchronized!", None))
        self.label.setText(QCoreApplication.translate("SysncTImeDialog", u"System Time:", None))
        self.label_3.setText(QCoreApplication.translate("SysncTImeDialog", u"Train System Time:", None))
        self.system_time_lbl.setText(QCoreApplication.translate("SysncTImeDialog", u"----", None))
        self.train_system_time_lbl.setText(QCoreApplication.translate("SysncTImeDialog", u"----", None))
        self.label_2.setText(QCoreApplication.translate("SysncTImeDialog", u"Please wait a few seconds...", None))
        self.error_lbl.setText(QCoreApplication.translate("SysncTImeDialog", u"PLease Wait a few seconds", None))
        self.sync_btn.setText(QCoreApplication.translate("SysncTImeDialog", u"Sync TIme", None))
    # retranslateUi

