# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

from uiUtils.GUIComponents import timeSpinBox
import assets_rc

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(705, 657)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        self.globalStyleSheet = QWidget(main)
        self.globalStyleSheet.setObjectName(u"globalStyleSheet")
        self.globalStyleSheet.setStyleSheet(u"/**************************Global Font***************************/\n"
"\n"
"QWidget\n"
"{\n"
"	font: auto \"Roboto\";\n"
"}\n"
"\n"
"/**************************QLabel***************************/\n"
"\n"
"QLabel\n"
"{\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QLabel:disabled\n"
"{\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"/**************************QScrollBar***************************/\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    width: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    background: #D7D7D9;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical \n"
"{\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical \n"
"{\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
""
                        "    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical \n"
"{\n"
"    border: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical \n"
"{\n"
"    background: #F7F8FA;\n"
"}\n"
"\n"
"QScrollBar:horizontal \n"
"{\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    background: #D7D7D9;\n"
"    min-width: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal \n"
"{\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal \n"
"{\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::le"
                        "ft-arrow:horizontal, QScrollBar::right-arrow:horizontal \n"
"{\n"
"    border: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal \n"
"{\n"
"    background: none;\n"
"	background: #F7F8FA;\n"
"}\n"
"\n"
"/**************************QCheckBox***************************/\n"
"\n"
"QCheckBox \n"
"{\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator \n"
"{\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked \n"
"{\n"
"    border: 2px solid #CED1D9;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked \n"
"{\n"
"    border: 2px solid #7892DF;\n"
"    background-color: #7892DF;\n"
"    image: url(:/icons/icons/tick_icon.png) \n"
"}\n"
"\n"
"QCheckBox::indicator:hover \n"
"{\n"
"    border: 2px solid rgba(194, 197, 204, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled \n"
"{\n"
"    border: 2px solid #E0E4EC;\n"
"    background-color: #F6F6F6;"
                        "\n"
"}\n"
"\n"
"/**************************QGraphicsView***************************/\n"
"\n"
"QGraphicsView\n"
"{\n"
"	border: None;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/**************************QLineEdit***************************/\n"
"\n"
"QLineEdit \n"
"{\n"
"  	border:1px solid #E0E4EC;\n"
"	background-color: #F7F8FA;\n"
"	border-radius: 10px;\n"
"	min-height: 25px;\n"
"	min-width: 70px;\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	font-size: 16px;\n"
"	alignment: center;\n"
"}\n"
"\n"
"QLineEdit:focus \n"
"{\n"
"	border-bottom: 2px solid #7892DF;\n"
"}\n"
"\n"
"QLineEdit:disabled \n"
"{\n"
"	color: rgb(120,120,120);\n"
"}\n"
"\n"
"\n"
"/*****************QSpinBox, QDoubleSpinBox*******************/\n"
"\n"
"QSpinBox, QDoubleSpinBox\n"
"{\n"
"	background-color: transparent;\n"
"	border-bottom: 2px solid #D7D7D9;\n"
"	border-radius: None;\n"
"	font-size: 16px;\n"
"	min-height: 25px;\n"
"	min-width: 70px;\n"
"	qproperty-alignment: AlignCenter;\n"
"}\n"
"\n"
"QSpinBox:disabled ,\n"
""
                        "QDoubleSpinBox:disabled\n"
"{\n"
"	border-bottom: 2px solid #F0F0F2;\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QSpinBox::up-arrow, \n"
"QDoubleSpinBox::up-arrow\n"
"{   \n"
"	image: url(:/icons/icons/plus_icon_black.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow,  \n"
"QDoubleSpinBox::down-arrow\n"
"{   \n"
"	image: url(:/icons/icons/minus_icon_black.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled, \n"
"QDoubleSpinBox::up-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/icons/plus_icon_gray.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled ,  \n"
"QDoubleSpinBox::down-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/icons/minus_icon_gray.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"	border:none;\n"
"    min-width:30px;\n"
"    min-height: 29px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: right;\n"
"    top: 0"
                        "px;\n"
"    right: 0px;\n"
"}\n"
"\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    min-width:30px;\n"
"    min-height: 29px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left;\n"
"    top: 0px;\n"
"    right: 0px;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QSpinBox::up-button:disabled ,\n"
"QSpinBox::down-button:disabled ,\n"
"QDoubleSpinBox::up-button:disabled ,\n"
"QDoubleSpinBox::down-button:disabled\n"
"{\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus\n"
"{\n"
"	border-bottom: 2px solid #7892DF;\n"
"}\n"
"\n"
"/***************************QDateEdit****************************/\n"
"\n"
"QDateEdit\n"
"{\n"
"	border:1px solid #E0E4EC;\n"
"	background-color: #F7F8FA;\n"
"	border-radius: 10px;\n"
"	min-height: 35px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QDateEdit:disabled\n"
"{\n"
"	border: 2p"
                        "x solid #F0F0F2;\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QDateEdit::up-button,\n"
"QDateEdit::down-button\n"
"{\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QDateEdit:focus\n"
"{\n"
"	border-bottom: 2px solid #7892DF;\n"
"}\n"
"\n"
"/**************************QTabWidget***************************/\n"
"\n"
"QTabWidget \n"
"{\n"
"    background-color: #F7F8FA;\n"
"}\n"
"\n"
"QTabBar::tab \n"
"{\n"
"    background-color: #BDBDBF;\n"
"    color: rgb(20, 20, 20);\n"
"	min-width: 100px;\n"
"    padding: 8px 16px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:hover \n"
"{\n"
"    background-color: #D7D7D9;\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"    border: 1px solid #E0E4EC;\n"
"    border-top: none;\n"
"    background-color: #E0E4EC;\n"
"}\n"
"\n"
"QTabBar::tab:selected \n"
"{\n"
"    background-color: #E0E4EC;\n"
"    border-bottom: 2px solid #7892DF; \n"
"}\n"
"\n"
"/**************************"
                        "QTableWidget***************************/\n"
"\n"
"QTableWidget \n"
"{\n"
"    background-color: #F7F8FA;\n"
"	gridline-color: #D7D7D9;\n"
"	color: rgb(20, 20, 20);\n"
"	border: 2px solid #F7F8FA;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section \n"
"{\n"
"    background-color: #F7F8FA;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom: 2px solid #BDBDBF;\n"
"	border-right: 1px solid #D7D7D9;\n"
"	font-weight: bold;\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QHeaderView::section:first \n"
"{\n"
"   border-top-left-radius: 4px;\n"
"	border-left: None;\n"
"}\n"
"\n"
"QHeaderView::section:last \n"
"{\n"
"   border-top-right-radius: 4px;\n"
"	border-right: None;\n"
"}\n"
"\n"
"QTableWidget::item:selected \n"
"{\n"
"    background-color: #E0E4EC;\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QTableWidget::item:hover \n"
"{\n"
"    background-color: #D7D7D9;\n"
"}\n"
"\n"
"QHeaderView::up-arrow \n"
"{\n"
"	image: url(:/icons/icons/table_sort_icon.png);\n"
"}\n"
"\n"
"\n"
"/********"
                        "******************QTextEdit***************************/\n"
"\n"
"QTextEdit \n"
"{\n"
"    background-color: #E0E4EC;\n"
"    border-radius: 5px;\n"
"    color: rgb(20, 20, 20);\n"
"	font: 11pt \"Arial\";\n"
"    font-size: 12pt;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"/**************************QGroupBox***************************/\n"
"\n"
"QGroupBox \n"
"{\n"
"    font: bold 14px;\n"
"    color: #333;\n"
"    border:1px solid #E0E4EC;\n"
"    border-radius: 2px;\n"
"    margin-top: 7px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title \n"
"{\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"	padding-left: 5px;\n"
"    color: #555;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/**************************Line***************************/\n"
"Line \n"
"{\n"
"	borerd: 0px;\n"
"    max-height: 0px;\n"
"}\n"
"\n"
"/**************************QSplitter***************************/\n"
"QSplitter::handle \n"
"{ \n"
"	background-color: transparent \n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.globalStyleSheet)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.localStyleSheet = QWidget(self.globalStyleSheet)
        self.localStyleSheet.setObjectName(u"localStyleSheet")
        self.localStyleSheet.setStyleSheet(u"/**************************LsideFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"LsideFrameStyle\"]\n"
"{\n"
"	background-color: #17203A;\n"
"}\n"
"\n"
"*[styleSheet=\"LsideFrameStyle\"]  .QPushButton{\n"
"	border: 0px;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"/**************************LtopFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"LtopFrameStyle\"]\n"
"{\n"
"	background-color: #F7F8FA;\n"
"	border:1px solid #D7D7D9;\n"
"}\n"
"\n"
"*[styleSheet=\"LtopFrameStyle\"] .QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"/**************************LpagesFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"LpagesFrameStyle\"] .QFrame\n"
"{\n"
"	background-color: #F7F8FA;\n"
"	border:1px solid #D7D7D9;\n"
"}\n"
"\n"
"*[styleSheet=\"LpagesFrameStyle\"] .QWidget\n"
"{\n"
"	background-color: transparent;\n"
"	border:None;\n"
"}\n"
"\n"
"*[styleSheet=\"LpagesFrameStyle\"] .QScrollArea\n"
"{\n"
"	background-color: transparent;\n"
"	border: None;\n"
"}\n"
"\n"
"/*****"
                        "********************LpagesBoldLabelStyle**************************/\n"
"\n"
"*[styleSheet=\"LpagesBoldLabelStyle\"] .QLabel\n"
"{\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"/*********************LshowStepsFrameStyle**********************/\n"
"\n"
"*[styleSheet=\"LshowStepsFrameStyle\"]\n"
"{\n"
"	border: None;\n"
"}\n"
"\n"
"*[styleSheet=\"LshowStepsFrameStyle\"]  .QFrame\n"
"{\n"
"	border: 2px solid #7E84A2;\n"
"	min-height: 0px;\n"
"	max-height: 0px;\n"
"}\n"
"\n"
"*[styleSheet=\"LshowStepsFrameStyle\"]  .QPushButton\n"
"{\n"
"	background-color: transparent;\n"
"	border:5px solid #7E84A2;\n"
"	border-radius: 32px;\n"
"	min-width: 55px;\n"
"	max-width: 55px;\n"
"	min-height: 55px;\n"
"	max-height: 55px;\n"
"	font-size: 24px;\n"
"	color: rgb(20, 20, 20);\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"*[styleSheet=\"LshowStepsFrameStyle\"]  .QPushButton:hover\n"
"{\n"
"	border:5px solid #BDBDBF;\n"
"}\n"
"\n"
"/*************************LfilterByFrameStyle**************************/\n"
"\n"
"*[styleShe"
                        "et=\"LfilterByFrameStyle\"] .QFrame\n"
"{\n"
"	border: None;\n"
"}\n"
"\n"
"*[styleSheet=\"LfilterByFrameStyle\"] .QLabel\n"
"{\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"/*************************************************/\n"
"QLabel[styleClass=\"msgStyle\"]\n"
"{\n"
"	color: rgb(0, 123, 253);\n"
"}\n"
"\n"
"\n"
"QPushButton[styleClass=\"fillBtn\"] {\n"
"	font-size: 14px;\n"
"	padding: 5px 10px;\n"
"    border: 1px solid #007BFF;\n"
"    border-radius: 5px;\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"}\n"
"QPushButton[styleClass=\"fillBtn\"]:hover {\n"
"	background-color: #0056b3;\n"
"}\n"
"QPushButton[styleClass=\"fillBtn\"]:pressed {\n"
"   background-color: #003d80;\n"
"}\n"
"\n"
"QPushButton[styleClass=\"fillBtn\"]:disabled {\n"
"   background-color: #c0c0c0;\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton[styleSheet=\"calendar\"]{\n"
"background:transparent;\n"
"icon:url(:/asstets/icons/calendar.png);\n"
"border:none;\n"
"icon-size:25px;\n"
"width:25px;\n"
"height:25px"
                        ";\n"
"}\n"
"\n"
"QPushButton[styleSheet=\"calendar\"]:hover{\n"
"icon:url(:/asstets/icons/calendar-hover.png);\n"
"\n"
"}\n"
"\n"
"QPushButton[styleSheet=\"calendar\"]:disabled{\n"
"icon:url(:/asstets/icons/calendar-disable.png);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.localStyleSheet)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftSideFrame = QFrame(self.localStyleSheet)
        self.leftSideFrame.setObjectName(u"leftSideFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftSideFrame.sizePolicy().hasHeightForWidth())
        self.leftSideFrame.setSizePolicy(sizePolicy1)
        self.leftSideFrame.setMinimumSize(QSize(0, 0))
        self.leftSideFrame.setMaximumSize(QSize(109, 16777211))
        self.leftSideFrame.setStyleSheet(u"LsideFrameStyle")
        self.leftSideFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftSideFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.leftSideFrame)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.dorsa_lbl = QLabel(self.leftSideFrame)
        self.dorsa_lbl.setObjectName(u"dorsa_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dorsa_lbl.sizePolicy().hasHeightForWidth())
        self.dorsa_lbl.setSizePolicy(sizePolicy2)
        self.dorsa_lbl.setMinimumSize(QSize(96, 45))
        self.dorsa_lbl.setMaximumSize(QSize(50, 65))
        self.dorsa_lbl.setPixmap(QPixmap(u"assets/icons/2.png"))
        self.dorsa_lbl.setScaledContents(True)
        self.dorsa_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_67.addWidget(self.dorsa_lbl)

        self.verticalSpacer = QSpacerItem(20, 23, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_67.addItem(self.verticalSpacer)

        self.side_copy_btn = QPushButton(self.leftSideFrame)
        self.side_copy_btn.setObjectName(u"side_copy_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.side_copy_btn.sizePolicy().hasHeightForWidth())
        self.side_copy_btn.setSizePolicy(sizePolicy3)
        self.side_copy_btn.setMinimumSize(QSize(0, 50))
        self.side_copy_btn.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setBold(True)
        font.setItalic(False)
        self.side_copy_btn.setFont(font)
        self.side_copy_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_copy_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/live_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.side_copy_btn.setIcon(icon)
        self.side_copy_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_67.addWidget(self.side_copy_btn)

        self.side_profile_btn = QPushButton(self.leftSideFrame)
        self.side_profile_btn.setObjectName(u"side_profile_btn")
        sizePolicy3.setHeightForWidth(self.side_profile_btn.sizePolicy().hasHeightForWidth())
        self.side_profile_btn.setSizePolicy(sizePolicy3)
        self.side_profile_btn.setMinimumSize(QSize(0, 50))
        self.side_profile_btn.setMaximumSize(QSize(16777215, 50))
        self.side_profile_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/settings_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.side_profile_btn.setIcon(icon1)
        self.side_profile_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_67.addWidget(self.side_profile_btn)

        self.side_about_btn = QPushButton(self.leftSideFrame)
        self.side_about_btn.setObjectName(u"side_about_btn")
        sizePolicy3.setHeightForWidth(self.side_about_btn.sizePolicy().hasHeightForWidth())
        self.side_about_btn.setSizePolicy(sizePolicy3)
        self.side_about_btn.setMinimumSize(QSize(0, 50))
        self.side_about_btn.setMaximumSize(QSize(16777215, 50))
        self.side_about_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/about_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.side_about_btn.setIcon(icon2)
        self.side_about_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_67.addWidget(self.side_about_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_67.addItem(self.verticalSpacer_2)

        self.verticalLayout_67.setStretch(3, 10)
        self.verticalLayout_67.setStretch(4, 10)
        self.verticalLayout_67.setStretch(5, 28)

        self.horizontalLayout_2.addWidget(self.leftSideFrame)

        self.frame = QFrame(self.localStyleSheet)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(self.frame)
        self.topFrame.setObjectName(u"topFrame")
        sizePolicy.setHeightForWidth(self.topFrame.sizePolicy().hasHeightForWidth())
        self.topFrame.setSizePolicy(sizePolicy)
        self.topFrame.setMinimumSize(QSize(0, 50))
        self.topFrame.setMaximumSize(QSize(16777215, 50))
        self.topFrame.setStyleSheet(u"LtopFrameStyle")
        self.topFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 6, -1, 6)
        self.login_btn = QPushButton(self.topFrame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setEnabled(True)
        self.login_btn.setMinimumSize(QSize(0, 0))
        self.login_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_btn.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.login_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.logined_username_lbl = QLabel(self.topFrame)
        self.logined_username_lbl.setObjectName(u"logined_username_lbl")

        self.horizontalLayout_14.addWidget(self.logined_username_lbl)

        self.help_btn = QPushButton(self.topFrame)
        self.help_btn.setObjectName(u"help_btn")
        sizePolicy3.setHeightForWidth(self.help_btn.sizePolicy().hasHeightForWidth())
        self.help_btn.setSizePolicy(sizePolicy3)
        self.help_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"assets/icons/help_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.help_btn.setIcon(icon3)
        self.help_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout_14.addWidget(self.help_btn)

        self.minimize_btn = QPushButton(self.topFrame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy3.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy3)
        self.minimize_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"assets/icons/minus_icon_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon4)
        self.minimize_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.topFrame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy3.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy3)
        self.close_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"assets/icons/close_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon5)
        self.close_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_14.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.topFrame)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.copy = QWidget()
        self.copy.setObjectName(u"copy")
        self.verticalLayout_2 = QVBoxLayout(self.copy)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.copy)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_10.addWidget(self.label)

        self.ip_input = QLineEdit(self.frame_2)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout_10.addWidget(self.ip_input)

        self.save_btn_ip = QPushButton(self.frame_2)
        self.save_btn_ip.setObjectName(u"save_btn_ip")
        self.save_btn_ip.setMaximumSize(QSize(20, 16777215))
        self.save_btn_ip.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_btn_ip.setStyleSheet(u"background-color: transparent;")
        icon6 = QIcon()
        icon6.addFile(u"assets/icons/save_image_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_btn_ip.setIcon(icon6)

        self.horizontalLayout_10.addWidget(self.save_btn_ip)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.ip_address_msg = QLabel(self.frame_2)
        self.ip_address_msg.setObjectName(u"ip_address_msg")

        self.verticalLayout_3.addWidget(self.ip_address_msg)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.copy)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.username_input = QLineEdit(self.frame_3)
        self.username_input.setObjectName(u"username_input")

        self.horizontalLayout_3.addWidget(self.username_input)

        self.save_btn_username = QPushButton(self.frame_3)
        self.save_btn_username.setObjectName(u"save_btn_username")
        self.save_btn_username.setMaximumSize(QSize(20, 16777215))
        self.save_btn_username.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_btn_username.setStyleSheet(u"background-color: transparent;")
        self.save_btn_username.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.save_btn_username)


        self.verticalLayout_16.addLayout(self.horizontalLayout_3)

        self.username_msg = QLabel(self.frame_3)
        self.username_msg.setObjectName(u"username_msg")

        self.verticalLayout_16.addWidget(self.username_msg)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.copy)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(19, -1, -1, -1)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.password_input = QLineEdit(self.frame_4)
        self.password_input.setObjectName(u"password_input")

        self.horizontalLayout_4.addWidget(self.password_input)

        self.save_btn_password = QPushButton(self.frame_4)
        self.save_btn_password.setObjectName(u"save_btn_password")
        self.save_btn_password.setMaximumSize(QSize(20, 16777215))
        self.save_btn_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_btn_password.setStyleSheet(u"background-color: transparent;")
        self.save_btn_password.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.save_btn_password)


        self.verticalLayout_17.addLayout(self.horizontalLayout_4)

        self.password_msg = QLabel(self.frame_4)
        self.password_msg.setObjectName(u"password_msg")

        self.verticalLayout_17.addWidget(self.password_msg)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.timeline_groupbox = QGroupBox(self.copy)
        self.timeline_groupbox.setObjectName(u"timeline_groupbox")
        self.timeline_groupbox.setMinimumSize(QSize(0, 160))
        self.timeline_groupbox.setCheckable(True)
        self.verticalLayout_19 = QVBoxLayout(self.timeline_groupbox)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_7 = QFrame(self.timeline_groupbox)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 120))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_date_2 = QFrame(self.frame_7)
        self.frame_date_2.setObjectName(u"frame_date_2")
        self.frame_date_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_date_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_date_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_date_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.label_31 = QLabel(self.frame_date_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setEnabled(True)
        self.label_31.setStyleSheet(u"QLabel{\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	color:rgb(0, 123, 255);\n"
"}\n"
"\n"
"QLabel:disabled{\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	color:rgb(177, 177, 177);\n"
"}")

        self.gridLayout.addWidget(self.label_31, 1, 8, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_date_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_32 = QLabel(self.frame_date_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 0, 6, 1, 1)

        self.label_34 = QLabel(self.frame_date_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 1, 6, 1, 1)

        self.label_6 = QLabel(self.frame_date_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(38, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 5, 1, 1)

        self.start_time_hour = timeSpinBox(self.frame_date_2)
        self.start_time_hour.setObjectName(u"start_time_hour")
        self.start_time_hour.setMaximum(23)

        self.gridLayout.addWidget(self.start_time_hour, 0, 7, 1, 1)

        self.end_calendar_btn = QPushButton(self.frame_date_2)
        self.end_calendar_btn.setObjectName(u"end_calendar_btn")
        self.end_calendar_btn.setMinimumSize(QSize(0, 0))
        self.end_calendar_btn.setStyleSheet(u"calendar")

        self.gridLayout.addWidget(self.end_calendar_btn, 1, 4, 1, 1)

        self.end_date = QLineEdit(self.frame_date_2)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setMinimumSize(QSize(102, 27))
        self.end_date.setMaximumSize(QSize(120, 16777215))
        self.end_date.setReadOnly(True)

        self.gridLayout.addWidget(self.end_date, 1, 3, 1, 1)

        self.label_30 = QLabel(self.frame_date_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(40, 0))
        self.label_30.setStyleSheet(u"QLabel{\n"
"	font-size:16px;\n"
"	color:rgb(0, 123, 255);\n"
"}\n"
"\n"
"QLabel:disabled{\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	color:rgb(177, 177, 177);\n"
"}")

        self.gridLayout.addWidget(self.label_30, 1, 0, 1, 1)

        self.label_10 = QLabel(self.frame_date_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(40, 0))
        self.label_10.setStyleSheet(u"QLabel{\n"
"	font-size:16px;\n"
"	color:rgb(0, 123, 255);\n"
"}\n"
"\n"
"QLabel:disabled{\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	color:rgb(177, 177, 177);\n"
"}")

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.start_date = QLineEdit(self.frame_date_2)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setMinimumSize(QSize(102, 27))
        self.start_date.setMaximumSize(QSize(120, 16777215))
        self.start_date.setReadOnly(True)

        self.gridLayout.addWidget(self.start_date, 0, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(38, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 5, 1, 1)

        self.start_calendar_btn = QPushButton(self.frame_date_2)
        self.start_calendar_btn.setObjectName(u"start_calendar_btn")
        self.start_calendar_btn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.start_calendar_btn.sizePolicy().hasHeightForWidth())
        self.start_calendar_btn.setSizePolicy(sizePolicy2)
        self.start_calendar_btn.setMinimumSize(QSize(25, 25))
        self.start_calendar_btn.setMaximumSize(QSize(16777210, 16777215))
        self.start_calendar_btn.setStyleSheet(u"calendar")

        self.gridLayout.addWidget(self.start_calendar_btn, 0, 4, 1, 1)

        self.label_8 = QLabel(self.frame_date_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	color:rgb(0, 123, 255);\n"
"}\n"
"\n"
"QLabel:disabled{\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	color:rgb(177, 177, 177);\n"
"}")

        self.gridLayout.addWidget(self.label_8, 0, 8, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)

        self.end_time_hour = timeSpinBox(self.frame_date_2)
        self.end_time_hour.setObjectName(u"end_time_hour")
        self.end_time_hour.setMaximum(23)

        self.gridLayout.addWidget(self.end_time_hour, 1, 7, 1, 1)

        self.start_time_minute = timeSpinBox(self.frame_date_2)
        self.start_time_minute.setObjectName(u"start_time_minute")
        self.start_time_minute.setMaximum(59)

        self.gridLayout.addWidget(self.start_time_minute, 0, 9, 1, 1)

        self.end_time_minute = timeSpinBox(self.frame_date_2)
        self.end_time_minute.setObjectName(u"end_time_minute")
        self.end_time_minute.setMaximum(59)

        self.gridLayout.addWidget(self.end_time_minute, 1, 9, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_date_2)

        self.time_line_msg = QLabel(self.frame_7)
        self.time_line_msg.setObjectName(u"time_line_msg")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.time_line_msg.setFont(font1)
        self.time_line_msg.setStyleSheet(u"color:rgb(230, 62, 5);")

        self.verticalLayout_20.addWidget(self.time_line_msg)


        self.verticalLayout_19.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.timeline_groupbox)

        self.copy_button = QPushButton(self.copy)
        self.copy_button.setObjectName(u"copy_button")
        self.copy_button.setEnabled(True)
        self.copy_button.setMinimumSize(QSize(200, 0))
        self.copy_button.setMaximumSize(QSize(200, 16777215))
        self.copy_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.copy_button.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.copy_button, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.copy_log_lbl = QLabel(self.copy)
        self.copy_log_lbl.setObjectName(u"copy_log_lbl")
        sizePolicy1.setHeightForWidth(self.copy_log_lbl.sizePolicy().hasHeightForWidth())
        self.copy_log_lbl.setSizePolicy(sizePolicy1)
        self.copy_log_lbl.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_2.addWidget(self.copy_log_lbl)

        self.frame_5 = QFrame(self.copy)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 80))
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.completed_copy_lbl = QLabel(self.frame_5)
        self.completed_copy_lbl.setObjectName(u"completed_copy_lbl")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.completed_copy_lbl.sizePolicy().hasHeightForWidth())
        self.completed_copy_lbl.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.completed_copy_lbl)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy5.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.total_copy_lbl = QLabel(self.frame_5)
        self.total_copy_lbl.setObjectName(u"total_copy_lbl")
        sizePolicy5.setHeightForWidth(self.total_copy_lbl.sizePolicy().hasHeightForWidth())
        self.total_copy_lbl.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.total_copy_lbl)

        self.total_copy_lbl_2 = QLabel(self.frame_5)
        self.total_copy_lbl_2.setObjectName(u"total_copy_lbl_2")
        sizePolicy5.setHeightForWidth(self.total_copy_lbl_2.sizePolicy().hasHeightForWidth())
        self.total_copy_lbl_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.total_copy_lbl_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.copy_speed_lbl = QLabel(self.frame_5)
        self.copy_speed_lbl.setObjectName(u"copy_speed_lbl")
        sizePolicy5.setHeightForWidth(self.copy_speed_lbl.sizePolicy().hasHeightForWidth())
        self.copy_speed_lbl.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.copy_speed_lbl)


        self.verticalLayout_18.addLayout(self.horizontalLayout_5)

        self.progress_bar = QProgressBar(self.frame_5)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.verticalLayout_18.addWidget(self.progress_bar)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.copy)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.verticalLayout_4 = QVBoxLayout(self.profile)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.profile)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_16 = QFrame(self.tab)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame_16)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 145))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.groupBox_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_15.addWidget(self.label_12)

        self.line_ip_camera_right = QLineEdit(self.frame_13)
        self.line_ip_camera_right.setObjectName(u"line_ip_camera_right")

        self.horizontalLayout_15.addWidget(self.line_ip_camera_right)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.groupBox_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.line_username_camera_right = QLineEdit(self.frame_14)
        self.line_username_camera_right.setObjectName(u"line_username_camera_right")

        self.horizontalLayout_16.addWidget(self.line_username_camera_right)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_15)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_17.addWidget(self.label_14)

        self.line_password_camera_right = QLineEdit(self.frame_15)
        self.line_password_camera_right.setObjectName(u"line_password_camera_right")

        self.horizontalLayout_17.addWidget(self.line_password_camera_right)


        self.horizontalLayout_16.addWidget(self.frame_15)


        self.verticalLayout_6.addWidget(self.frame_14)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.frame_16)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.groupBox)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.line_ip_camera_left = QLineEdit(self.frame_10)
        self.line_ip_camera_left.setObjectName(u"line_ip_camera_left")

        self.horizontalLayout_11.addWidget(self.line_ip_camera_left)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.groupBox)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.line_username_camera_left = QLineEdit(self.frame_11)
        self.line_username_camera_left.setObjectName(u"line_username_camera_left")

        self.horizontalLayout_12.addWidget(self.line_username_camera_left)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.line_password_camera_left = QLineEdit(self.frame_12)
        self.line_password_camera_left.setObjectName(u"line_password_camera_left")

        self.horizontalLayout_13.addWidget(self.line_password_camera_left)


        self.horizontalLayout_12.addWidget(self.frame_12)


        self.verticalLayout_5.addWidget(self.frame_11)


        self.verticalLayout_7.addWidget(self.groupBox)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.groupBox_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_18.addWidget(self.label_15)

        self.line_train_id = QLineEdit(self.frame_17)
        self.line_train_id.setObjectName(u"line_train_id")

        self.horizontalLayout_18.addWidget(self.line_train_id)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_19.addWidget(self.label_16)

        self.line_max_image = QLineEdit(self.frame_18)
        self.line_max_image.setObjectName(u"line_max_image")

        self.horizontalLayout_19.addWidget(self.line_max_image)


        self.horizontalLayout_18.addWidget(self.frame_18)


        self.verticalLayout_9.addWidget(self.frame_17)


        self.verticalLayout_8.addWidget(self.groupBox_3)

        self.frame_19 = QFrame(self.tab)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_20.addWidget(self.label_17)

        self.line_name = QLineEdit(self.frame_19)
        self.line_name.setObjectName(u"line_name")

        self.horizontalLayout_20.addWidget(self.line_name)

        self.save_btn = QPushButton(self.frame_19)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_20.addWidget(self.save_btn)


        self.verticalLayout_8.addWidget(self.frame_19)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_14 = QVBoxLayout(self.tab_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_20 = QFrame(self.tab_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.frame_20)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_21.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.frame_20)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_21.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_20)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_21.addWidget(self.pushButton_3)


        self.verticalLayout_14.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.tab_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_21)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.frame_21)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(16777215, 145))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.groupBox_4)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_22)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_22.addWidget(self.label_18)

        self.line_ip_camera_right_2 = QLineEdit(self.frame_22)
        self.line_ip_camera_right_2.setObjectName(u"line_ip_camera_right_2")

        self.horizontalLayout_22.addWidget(self.line_ip_camera_right_2)


        self.verticalLayout_10.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.groupBox_4)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_23)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_23.addWidget(self.label_19)

        self.line_username_camera_right_2 = QLineEdit(self.frame_23)
        self.line_username_camera_right_2.setObjectName(u"line_username_camera_right_2")

        self.horizontalLayout_23.addWidget(self.line_username_camera_right_2)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_24)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_24.addWidget(self.label_20)

        self.line_password_camera_right_2 = QLineEdit(self.frame_24)
        self.line_password_camera_right_2.setObjectName(u"line_password_camera_right_2")

        self.horizontalLayout_24.addWidget(self.line_password_camera_right_2)


        self.horizontalLayout_23.addWidget(self.frame_24)


        self.verticalLayout_10.addWidget(self.frame_23)


        self.verticalLayout_13.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.frame_21)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.groupBox_6)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_27)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_27.addWidget(self.label_23)

        self.line_ip_camera_left_2 = QLineEdit(self.frame_27)
        self.line_ip_camera_left_2.setObjectName(u"line_ip_camera_left_2")

        self.horizontalLayout_27.addWidget(self.line_ip_camera_left_2)


        self.verticalLayout_12.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.groupBox_6)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_28)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_28.addWidget(self.label_24)

        self.line_username_camera_left_2 = QLineEdit(self.frame_28)
        self.line_username_camera_left_2.setObjectName(u"line_username_camera_left_2")

        self.horizontalLayout_28.addWidget(self.line_username_camera_left_2)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_29)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_29.addWidget(self.label_25)

        self.line_password_camera_left_2 = QLineEdit(self.frame_29)
        self.line_password_camera_left_2.setObjectName(u"line_password_camera_left_2")

        self.horizontalLayout_29.addWidget(self.line_password_camera_left_2)


        self.horizontalLayout_28.addWidget(self.frame_29)


        self.verticalLayout_12.addWidget(self.frame_28)


        self.verticalLayout_13.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.frame_21)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.groupBox_5)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_25)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_25.addWidget(self.label_21)

        self.line_train_id_2 = QLineEdit(self.frame_25)
        self.line_train_id_2.setObjectName(u"line_train_id_2")

        self.horizontalLayout_25.addWidget(self.line_train_id_2)

        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_26)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_26.addWidget(self.label_22)

        self.line_max_image_2 = QLineEdit(self.frame_26)
        self.line_max_image_2.setObjectName(u"line_max_image_2")

        self.horizontalLayout_26.addWidget(self.line_max_image_2)


        self.horizontalLayout_25.addWidget(self.frame_26)


        self.verticalLayout_11.addWidget(self.frame_25)


        self.verticalLayout_13.addWidget(self.groupBox_5)


        self.verticalLayout_14.addWidget(self.frame_21)

        self.line = QFrame(self.tab_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.groupBox_7 = QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.groupBox_7)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_30)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_30.addWidget(self.label_26)

        self.line_ip_camera_left_3 = QLineEdit(self.frame_30)
        self.line_ip_camera_left_3.setObjectName(u"line_ip_camera_left_3")

        self.horizontalLayout_30.addWidget(self.line_ip_camera_left_3)


        self.verticalLayout_15.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.groupBox_7)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_31)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_31.addWidget(self.label_27)

        self.line_username_camera_left_3 = QLineEdit(self.frame_31)
        self.line_username_camera_left_3.setObjectName(u"line_username_camera_left_3")

        self.horizontalLayout_31.addWidget(self.line_username_camera_left_3)

        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_32)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_32.addWidget(self.label_28)

        self.line_password_camera_left_3 = QLineEdit(self.frame_32)
        self.line_password_camera_left_3.setObjectName(u"line_password_camera_left_3")

        self.horizontalLayout_32.addWidget(self.line_password_camera_left_3)


        self.horizontalLayout_31.addWidget(self.frame_32)


        self.verticalLayout_15.addWidget(self.frame_31)

        self.pushButton_4 = QPushButton(self.groupBox_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_15.addWidget(self.pushButton_4)


        self.verticalLayout_14.addWidget(self.groupBox_7)

        self.label_29 = QLabel(self.tab_2)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_14.addWidget(self.label_29)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.profile)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.localStyleSheet)

        main.setCentralWidget(self.globalStyleSheet)
        self.statusBar = QStatusBar(main)
        self.statusBar.setObjectName(u"statusBar")
        main.setStatusBar(self.statusBar)

        self.retranslateUi(main)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"MainWindow", None))
        self.dorsa_lbl.setText("")
        self.side_copy_btn.setText(QCoreApplication.translate("main", u"Copy", None))
        self.side_profile_btn.setText(QCoreApplication.translate("main", u"Profile", None))
        self.side_about_btn.setText(QCoreApplication.translate("main", u" About Us ", None))
        self.login_btn.setText(QCoreApplication.translate("main", u"Login", None))
        self.login_btn.setProperty("styleClass", QCoreApplication.translate("main", u"fillBtn", None))
        self.logined_username_lbl.setText("")
        self.help_btn.setText("")
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("main", u"IP Address : ", None))
        self.save_btn_ip.setText("")
        self.ip_address_msg.setText(QCoreApplication.translate("main", u"message", None))
        self.ip_address_msg.setProperty("styleClass", QCoreApplication.translate("main", u"msgStyle", None))
        self.label_2.setText(QCoreApplication.translate("main", u"User Name :", None))
        self.save_btn_username.setText("")
        self.username_msg.setText(QCoreApplication.translate("main", u"message", None))
        self.username_msg.setProperty("styleClass", QCoreApplication.translate("main", u"msgStyle", None))
        self.label_3.setText(QCoreApplication.translate("main", u"Password : ", None))
        self.save_btn_password.setText("")
        self.password_msg.setText(QCoreApplication.translate("main", u"message", None))
        self.password_msg.setProperty("styleClass", QCoreApplication.translate("main", u"msgStyle", None))
        self.timeline_groupbox.setTitle(QCoreApplication.translate("main", u"Time Line Filter", None))
        self.label_31.setText(QCoreApplication.translate("main", u":", None))
        self.label_7.setText(QCoreApplication.translate("main", u"date", None))
        self.label_32.setText(QCoreApplication.translate("main", u"Time", None))
        self.label_34.setText(QCoreApplication.translate("main", u"Time", None))
        self.label_6.setText(QCoreApplication.translate("main", u"date", None))
        self.end_calendar_btn.setText("")
        self.end_calendar_btn.setProperty("styleClass", "")
        self.label_30.setText(QCoreApplication.translate("main", u"To", None))
        self.label_10.setText(QCoreApplication.translate("main", u"From", None))
        self.start_calendar_btn.setText("")
        self.start_calendar_btn.setProperty("styleClass", "")
        self.label_8.setText(QCoreApplication.translate("main", u":", None))
        self.time_line_msg.setText(QCoreApplication.translate("main", u"TextLabel", None))
        self.copy_button.setText(QCoreApplication.translate("main", u"Start Copy", None))
        self.copy_button.setProperty("styleClass", QCoreApplication.translate("main", u"fillBtn", None))
        self.copy_log_lbl.setText(QCoreApplication.translate("main", u"message", None))
        self.copy_log_lbl.setProperty("styleClass", QCoreApplication.translate("main", u"msgStyle", None))
        self.completed_copy_lbl.setText(QCoreApplication.translate("main", u"-", None))
        self.label_9.setText(QCoreApplication.translate("main", u"/", None))
        self.total_copy_lbl.setText(QCoreApplication.translate("main", u"-", None))
        self.total_copy_lbl_2.setText(QCoreApplication.translate("main", u"MB", None))
        self.copy_speed_lbl.setText(QCoreApplication.translate("main", u"Speed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("main", u"Right Camera", None))
        self.label_12.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_13.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_14.setText(QCoreApplication.translate("main", u"Password :", None))
        self.groupBox.setTitle(QCoreApplication.translate("main", u"Left Camera", None))
        self.label_4.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_5.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_11.setText(QCoreApplication.translate("main", u"Password :", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("main", u"Other Settings", None))
        self.label_15.setText(QCoreApplication.translate("main", u"Train ID :", None))
        self.label_16.setText(QCoreApplication.translate("main", u"Max Image :", None))
        self.label_17.setText(QCoreApplication.translate("main", u"Name :", None))
        self.save_btn.setText(QCoreApplication.translate("main", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main", u"Create New Profile", None))
        self.pushButton.setText(QCoreApplication.translate("main", u"Select", None))
        self.pushButton_3.setText(QCoreApplication.translate("main", u"Delete", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("main", u"Right Camera", None))
        self.label_18.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_19.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_20.setText(QCoreApplication.translate("main", u"Password :", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("main", u"Left Camera", None))
        self.label_23.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_24.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_25.setText(QCoreApplication.translate("main", u"Password :", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("main", u"Other Settings", None))
        self.label_21.setText(QCoreApplication.translate("main", u"Train ID :", None))
        self.label_22.setText(QCoreApplication.translate("main", u"Max Image :", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("main", u"Remote System", None))
        self.label_26.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_27.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_28.setText(QCoreApplication.translate("main", u"Password :", None))
        self.pushButton_4.setText(QCoreApplication.translate("main", u"Send", None))
        self.label_29.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("main", u"Load - Send", None))
    # retranslateUi

