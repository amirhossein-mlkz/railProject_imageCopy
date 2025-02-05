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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

from uiUtils.GUIComponents import timeSpinBox
import assets_rc

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.setEnabled(True)
        main.resize(604, 629)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        main.setMinimumSize(QSize(0, 0))
        main.setMaximumSize(QSize(700, 16777215))
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
"	image: url(:/asstets/icons/check-wight-24.png);\n"
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
"    background-color: #F6F"
                        "6F6;\n"
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
"	background: #413B47;\n"
"}\n"
"\n"
"*[styleSheet=\"LsideFrameStyle\"]  .QPushButton{\n"
"	border: 0px;\n"
"	color: #f0f0f0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"*[styleSheet=\"LsideFrameStyle\"]  .QPushButton:disabled{\n"
"	border: 0px;\n"
"\n"
"	color: rgb(212, 212, 212);\n"
"	font-weight: bold;\n"
"	background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"\n"
"/**************************LtopFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"LtopFrameStyle\"]\n"
"{\n"
"	background-color:rgb(220, 221, 180);\n"
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
"\n"
"\n"
"	border:1px solid #D7D7D9;\n"
"}\n"
"\n"
"*[styleSheet=\"LpagesFrameStyle\""
                        "] .QWidget\n"
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
"/*************************LpagesBoldLabelStyle**************************/\n"
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
""
                        "}\n"
"\n"
"*[styleSheet=\"LshowStepsFrameStyle\"]  .QPushButton:hover\n"
"{\n"
"	border:5px solid #BDBDBF;\n"
"}\n"
"\n"
"/*************************LfilterByFrameStyle**************************/\n"
"\n"
"*[styleSheet=\"LfilterByFrameStyle\"] .QFrame\n"
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
""
                        "	border:none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D7D7D9;\n"
"    padding: 5px;\n"
"    border-radius: 4px;\n"
"    color: #17203A;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #D7D7D9;\n"
"    background-color: #F7F8FA;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/asstets/icons/down_icon_black.png); /* Adjust the path to your arrow icon */\n"
"    width:15px; /* Set the arrow width */\n"
"    height: 15px; /* Set the arrow height */\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(:/asstets/icons/down_icon_black.png);\n"
"    width: 12px; /* Set the arrow width */\n"
"    height: 12px; /* Set the arrow height */\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/asstets/icons/down_icon_black.png);\n"
""
                        "    width: 12px; /* Set the arrow width */\n"
"    height: 12px; /* Set the arrow height */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D7D7D9;\n"
"    selection-background-color: #007BFF;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* ComboBox for Disabled State */\n"
"QComboBox:disabled {\n"
"    background-color: #E0E0E0;\n"
"    color: #A0A0A0;\n"
"    border: 1px solid #D7D7D9;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/**************************LGroupBoxStyle***************************/\n"
"\n"
"QGroupBox {\n"
"    background-color: #F7F8FA;  /* Background color inside the group box */\n"
"    border: 1px solid #D7D7D9;  /* Border around the group box */\n"
"    border-radius: 5px;         /* Slight rounded corners */\n"
"    margin-top: 20px;           /* Space between title and top edge */\n"
"    padding: 10px;              /* Padding inside the group box */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-ori"
                        "gin: margin;  /* Position title over the border */\n"
"    subcontrol-position: top left; /* Title alignment */\n"
"\n"
"	background-color: rgb(89, 89, 89);\n"
"    padding: 5px 10px;          /* Padding around the title */\n"
"    color: white;               /* Title text color */\n"
"    border-radius: 3px;         /* Rounded corners for the title */\n"
"    font-weight: bold;          /* Bold title text */\n"
"}\n"
"\n"
"QGroupBox:disabled {\n"
"    background-color: #E0E0E0;  /* Background when disabled */\n"
"    color: #A0A0A0;             /* Text color when disabled */\n"
"    border: 1px solid #D7D7D9;  /* Same border when disabled */\n"
"}\n"
"\n"
"\n"
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
        self.leftSideFrame.setMinimumSize(QSize(120, 0))
        self.leftSideFrame.setMaximumSize(QSize(120, 16777211))
        self.leftSideFrame.setStyleSheet(u"LsideFrameStyle")
        self.leftSideFrame.setFrameShape(QFrame.NoFrame)
        self.leftSideFrame.setLineWidth(1)
        self.verticalLayout_67 = QVBoxLayout(self.leftSideFrame)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.leftSideFrame)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 12))
        self.frame_28.setMaximumSize(QSize(16777215, 12))
        self.frame_28.setStyleSheet(u"background-color:rgb(220, 221, 180);")
        self.frame_28.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_67.addWidget(self.frame_28)

        self.line_5 = QFrame(self.leftSideFrame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_5)

        self.side_copy_btn = QPushButton(self.leftSideFrame)
        self.side_copy_btn.setObjectName(u"side_copy_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.side_copy_btn.sizePolicy().hasHeightForWidth())
        self.side_copy_btn.setSizePolicy(sizePolicy2)
        self.side_copy_btn.setMinimumSize(QSize(0, 50))
        self.side_copy_btn.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setBold(True)
        font.setItalic(False)
        self.side_copy_btn.setFont(font)
        self.side_copy_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_copy_btn.setStyleSheet(u"\n"
"background-color: rgb(241, 229, 139);\n"
"color:black;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/live_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.side_copy_btn.setIcon(icon)
        self.side_copy_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_67.addWidget(self.side_copy_btn)

        self.line_4 = QFrame(self.leftSideFrame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_4)

        self.side_profile_btn = QPushButton(self.leftSideFrame)
        self.side_profile_btn.setObjectName(u"side_profile_btn")
        sizePolicy2.setHeightForWidth(self.side_profile_btn.sizePolicy().hasHeightForWidth())
        self.side_profile_btn.setSizePolicy(sizePolicy2)
        self.side_profile_btn.setMinimumSize(QSize(0, 50))
        self.side_profile_btn.setMaximumSize(QSize(16777215, 50))
        self.side_profile_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/settings_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.side_profile_btn.setIcon(icon1)
        self.side_profile_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_67.addWidget(self.side_profile_btn)

        self.line_6 = QFrame(self.leftSideFrame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_6)

        self.side_train_config_btn = QPushButton(self.leftSideFrame)
        self.side_train_config_btn.setObjectName(u"side_train_config_btn")
        sizePolicy2.setHeightForWidth(self.side_train_config_btn.sizePolicy().hasHeightForWidth())
        self.side_train_config_btn.setSizePolicy(sizePolicy2)
        self.side_train_config_btn.setMinimumSize(QSize(0, 50))
        self.side_train_config_btn.setMaximumSize(QSize(16777215, 50))
        self.side_train_config_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_train_config_btn.setIcon(icon1)
        self.side_train_config_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_67.addWidget(self.side_train_config_btn)

        self.line_7 = QFrame(self.leftSideFrame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_7)

        self.side_setting_btn = QPushButton(self.leftSideFrame)
        self.side_setting_btn.setObjectName(u"side_setting_btn")
        sizePolicy2.setHeightForWidth(self.side_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_setting_btn.setSizePolicy(sizePolicy2)
        self.side_setting_btn.setMinimumSize(QSize(0, 50))
        self.side_setting_btn.setMaximumSize(QSize(16777215, 50))
        self.side_setting_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_setting_btn.setIcon(icon1)
        self.side_setting_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_67.addWidget(self.side_setting_btn)

        self.line_2 = QFrame(self.leftSideFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_2)

        self.side_about_btn = QPushButton(self.leftSideFrame)
        self.side_about_btn.setObjectName(u"side_about_btn")
        self.side_about_btn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.side_about_btn.sizePolicy().hasHeightForWidth())
        self.side_about_btn.setSizePolicy(sizePolicy2)
        self.side_about_btn.setMinimumSize(QSize(0, 50))
        self.side_about_btn.setMaximumSize(QSize(16777215, 50))
        self.side_about_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/about_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.side_about_btn.setIcon(icon2)
        self.side_about_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_67.addWidget(self.side_about_btn)

        self.line_8 = QFrame(self.leftSideFrame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_67.addItem(self.verticalSpacer_2)

        self.label_66 = QLabel(self.leftSideFrame)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(0, 80))
        self.label_66.setMaximumSize(QSize(100, 80))
        self.label_66.setPixmap(QPixmap(u":/asstets/icons/logo_aryan.png"))
        self.label_66.setScaledContents(True)

        self.verticalLayout_67.addWidget(self.label_66, 0, Qt.AlignHCenter)

        self.label_65 = QLabel(self.leftSideFrame)
        self.label_65.setObjectName(u"label_65")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy3)
        self.label_65.setMinimumSize(QSize(28, 120))
        self.label_65.setMaximumSize(QSize(100, 120))
        self.label_65.setSizeIncrement(QSize(50, 0))
        self.label_65.setPixmap(QPixmap(u":/asstets/icons/rahahan-logo.png"))
        self.label_65.setScaledContents(True)

        self.verticalLayout_67.addWidget(self.label_65, 0, Qt.AlignHCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_67.addItem(self.verticalSpacer_11)

        self.login_btn = QPushButton(self.leftSideFrame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setEnabled(True)
        self.login_btn.setMinimumSize(QSize(0, 0))
        self.login_btn.setMaximumSize(QSize(85, 16777215))
        self.login_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/asstets/icons/login_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.login_btn.setIcon(icon3)
        self.login_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_67.addWidget(self.login_btn, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 19, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_67.addItem(self.verticalSpacer_5)


        self.horizontalLayout_2.addWidget(self.leftSideFrame)

        self.frame = QFrame(self.localStyleSheet)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setLineWidth(0)
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
        self.topFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_14 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_14.setSpacing(11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 6, -1, 6)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.logined_username_lbl = QLabel(self.topFrame)
        self.logined_username_lbl.setObjectName(u"logined_username_lbl")

        self.horizontalLayout_14.addWidget(self.logined_username_lbl)

        self.help_btn = QPushButton(self.topFrame)
        self.help_btn.setObjectName(u"help_btn")
        sizePolicy2.setHeightForWidth(self.help_btn.sizePolicy().hasHeightForWidth())
        self.help_btn.setSizePolicy(sizePolicy2)
        self.help_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"../../../.designer/backup/assets/icons/help_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.help_btn.setIcon(icon4)
        self.help_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout_14.addWidget(self.help_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)

        self.minimize_btn = QPushButton(self.topFrame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy2.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy2)
        self.minimize_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/asstets/icons/minus_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon5)
        self.minimize_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.topFrame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy2.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy2)
        self.close_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/asstets/icons/close_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon6)
        self.close_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_14.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.topFrame)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QPushButton{\n"
"	font-size: 14px;\n"
"	padding: 2px 2px;\n"
"    border: 1px solid #007BFF;\n"
"    border-radius: 5px;\n"
"    background-color: 007BFF;\n"
"	background-color: rgb(33, 33, 33);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0056b3;\n"
"}\n"
"QPushButton:pressed {\n"
"   background-color: #003d80;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"\n"
"\n"
"	background-color: rgb(112, 112, 112);\n"
"	border:none;\n"
"}")
        self.copy = QWidget()
        self.copy.setObjectName(u"copy")
        self.verticalLayout_2 = QVBoxLayout(self.copy)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_2 = QScrollArea(self.copy)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 514, 650))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, 9, -1)
        self.frame_56 = QFrame(self.scrollAreaWidgetContents)
        self.frame_56.setObjectName(u"frame_56")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy4)
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_56)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.label)

        self.combo_copy_train_name = QComboBox(self.frame_56)
        self.combo_copy_train_name.setObjectName(u"combo_copy_train_name")
        self.combo_copy_train_name.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.combo_copy_train_name)


        self.verticalLayout_17.addWidget(self.frame_56)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_58 = QFrame(self.frame_13)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setEnabled(False)
        self.frame_58.setMinimumSize(QSize(0, 80))
        self.frame_58.setMaximumSize(QSize(16777215, 90))
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_35 = QVBoxLayout(self.frame_58)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(35, 0, 35, 0)
        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        sizePolicy4.setHeightForWidth(self.frame_60.sizePolicy().hasHeightForWidth())
        self.frame_60.setSizePolicy(sizePolicy4)
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_33 = QVBoxLayout(self.frame_60)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, -1, -1, -1)
        self.label_2 = QLabel(self.frame_60)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_54.addWidget(self.label_2)

        self.ip_input = QLineEdit(self.frame_60)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ip_input.setReadOnly(True)

        self.horizontalLayout_54.addWidget(self.ip_input)


        self.verticalLayout_33.addLayout(self.horizontalLayout_54)


        self.verticalLayout_35.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_58)
        self.frame_61.setObjectName(u"frame_61")
        sizePolicy4.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy4)
        self.frame_61.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_34 = QVBoxLayout(self.frame_61)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, -1, -1, -1)
        self.label_17 = QLabel(self.frame_61)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_55.addWidget(self.label_17)

        self.username_input = QLineEdit(self.frame_61)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setReadOnly(True)

        self.horizontalLayout_55.addWidget(self.username_input)


        self.verticalLayout_34.addLayout(self.horizontalLayout_55)


        self.verticalLayout_35.addWidget(self.frame_61)


        self.verticalLayout_10.addWidget(self.frame_58)

        self.frame_7 = QFrame(self.frame_13)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.timeline_groupbox = QGroupBox(self.frame_7)
        self.timeline_groupbox.setObjectName(u"timeline_groupbox")
        self.timeline_groupbox.setMinimumSize(QSize(0, 250))
        self.timeline_groupbox.setCheckable(True)
        self.verticalLayout_19 = QVBoxLayout(self.timeline_groupbox)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, -1, 0, -1)
        self.frame_21 = QFrame(self.timeline_groupbox)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 120))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_20 = QVBoxLayout(self.frame_21)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, -1, 0, -1)
        self.frame_date_2 = QFrame(self.frame_21)
        self.frame_date_2.setObjectName(u"frame_date_2")
        self.frame_date_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_date_2.setFrameShape(QFrame.NoFrame)
        self.gridLayout = QGridLayout(self.frame_date_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.start_time_hour = timeSpinBox(self.frame_date_2)
        self.start_time_hour.setObjectName(u"start_time_hour")
        self.start_time_hour.setMaximumSize(QSize(75, 16777215))
        self.start_time_hour.setMaximum(23)

        self.gridLayout.addWidget(self.start_time_hour, 0, 5, 1, 1)

        self.end_calendar_btn = QPushButton(self.frame_date_2)
        self.end_calendar_btn.setObjectName(u"end_calendar_btn")
        self.end_calendar_btn.setMinimumSize(QSize(0, 0))
        self.end_calendar_btn.setStyleSheet(u"QPushButton{\n"
"background:transparent;\n"
"icon:url(:/asstets/icons/calendar.png);\n"
"border:none;\n"
"icon-size:25px;\n"
"width:25px;\n"
"height:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"icon:url(:/asstets/icons/calendar-hover.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"icon:url(:/asstets/icons/calendar-disable.png);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.end_calendar_btn, 1, 2, 1, 1)

        self.start_calendar_btn = QPushButton(self.frame_date_2)
        self.start_calendar_btn.setObjectName(u"start_calendar_btn")
        self.start_calendar_btn.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.start_calendar_btn.sizePolicy().hasHeightForWidth())
        self.start_calendar_btn.setSizePolicy(sizePolicy3)
        self.start_calendar_btn.setMinimumSize(QSize(25, 25))
        self.start_calendar_btn.setMaximumSize(QSize(16777210, 16777215))
        self.start_calendar_btn.setStyleSheet(u"QPushButton{\n"
"background:transparent;\n"
"icon:url(:/asstets/icons/calendar.png);\n"
"border:none;\n"
"icon-size:25px;\n"
"width:25px;\n"
"height:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"icon:url(:/asstets/icons/calendar-hover.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"icon:url(:/asstets/icons/calendar-disable.png);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.start_calendar_btn, 0, 2, 1, 1)

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

        self.gridLayout.addWidget(self.label_31, 1, 6, 1, 1)

        self.start_time_minute = timeSpinBox(self.frame_date_2)
        self.start_time_minute.setObjectName(u"start_time_minute")
        self.start_time_minute.setMaximumSize(QSize(75, 16777215))
        self.start_time_minute.setMaximum(59)

        self.gridLayout.addWidget(self.start_time_minute, 0, 7, 1, 1)

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

        self.gridLayout.addWidget(self.label_8, 0, 6, 1, 1)

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

        self.end_date = QLineEdit(self.frame_date_2)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setMinimumSize(QSize(102, 27))
        self.end_date.setMaximumSize(QSize(120, 16777215))
        self.end_date.setReadOnly(True)

        self.gridLayout.addWidget(self.end_date, 1, 1, 1, 1)

        self.label_32 = QLabel(self.frame_date_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 0, 4, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(38, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 3, 1, 1)

        self.end_time_hour = timeSpinBox(self.frame_date_2)
        self.end_time_hour.setObjectName(u"end_time_hour")
        self.end_time_hour.setMaximumSize(QSize(75, 16777215))
        self.end_time_hour.setMaximum(23)

        self.gridLayout.addWidget(self.end_time_hour, 1, 5, 1, 1)

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

        self.label_34 = QLabel(self.frame_date_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 1, 4, 1, 1)

        self.end_time_minute = timeSpinBox(self.frame_date_2)
        self.end_time_minute.setObjectName(u"end_time_minute")
        self.end_time_minute.setMaximumSize(QSize(75, 16777215))
        self.end_time_minute.setMaximum(59)

        self.gridLayout.addWidget(self.end_time_minute, 1, 7, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(38, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 3, 1, 1)

        self.start_date = QLineEdit(self.frame_date_2)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setMinimumSize(QSize(102, 27))
        self.start_date.setMaximumSize(QSize(120, 16777215))
        self.start_date.setReadOnly(True)

        self.gridLayout.addWidget(self.start_date, 0, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_date_2)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(-1, 6, -1, -1)
        self.only_copy_new_checkbox = QCheckBox(self.frame_21)
        self.only_copy_new_checkbox.setObjectName(u"only_copy_new_checkbox")
        self.only_copy_new_checkbox.setChecked(True)
        self.only_copy_new_checkbox.setTristate(False)

        self.horizontalLayout_59.addWidget(self.only_copy_new_checkbox)


        self.verticalLayout_20.addLayout(self.horizontalLayout_59)

        self.time_line_msg = QLabel(self.frame_21)
        self.time_line_msg.setObjectName(u"time_line_msg")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.time_line_msg.setFont(font1)
        self.time_line_msg.setStyleSheet(u"color:rgb(230, 62, 5);")

        self.verticalLayout_20.addWidget(self.time_line_msg)


        self.verticalLayout_19.addWidget(self.frame_21)


        self.verticalLayout_12.addWidget(self.timeline_groupbox)


        self.verticalLayout_10.addWidget(self.frame_7)


        self.verticalLayout_17.addWidget(self.frame_13)

        self.copy_button = QPushButton(self.scrollAreaWidgetContents)
        self.copy_button.setObjectName(u"copy_button")
        self.copy_button.setEnabled(True)
        self.copy_button.setMinimumSize(QSize(415, 31))
        self.copy_button.setMaximumSize(QSize(415, 16777215))
        self.copy_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.copy_button.setStyleSheet(u"QPushButton{\n"
"	\n"
"background-color: rgb(85, 85, 255);\n"
"min-height: 25px;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(71, 71, 213);	\n"
"}")

        self.verticalLayout_17.addWidget(self.copy_button, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.check_time_btn = QPushButton(self.frame_3)
        self.check_time_btn.setObjectName(u"check_time_btn")
        self.check_time_btn.setEnabled(True)
        self.check_time_btn.setMinimumSize(QSize(200, 33))
        self.check_time_btn.setMaximumSize(QSize(200, 16777215))
        self.check_time_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_time_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	\n"
"color: rgb(85, 85, 255);\n"
"background-color: transparent;\n"
"border:2px solid rgb(85, 85, 255);\n"
"min-height: 25px;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(71, 71, 213);	\n"
"color:#fff;\n"
"}")

        self.horizontalLayout_15.addWidget(self.check_time_btn)

        self.btn_update_train = QPushButton(self.frame_3)
        self.btn_update_train.setObjectName(u"btn_update_train")
        self.btn_update_train.setEnabled(True)
        self.btn_update_train.setMinimumSize(QSize(200, 33))
        self.btn_update_train.setMaximumSize(QSize(200, 16777215))
        self.btn_update_train.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_update_train.setStyleSheet(u"\n"
"QPushButton{\n"
"	\n"
"color: rgb(85, 85, 255);\n"
"background-color: transparent;\n"
"border:2px solid rgb(85, 85, 255);\n"
"min-height: 25px;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(71, 71, 213);	\n"
"color:#fff;\n"
"}")

        self.horizontalLayout_15.addWidget(self.btn_update_train)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.frame_24 = QFrame(self.scrollAreaWidgetContents)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 110))
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_13 = QVBoxLayout(self.frame_24)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.verticalLayout_17.addWidget(self.frame_24)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_29 = QVBoxLayout(self.frame_11)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_20 = QFrame(self.frame_11)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.copy_log_lbl = QLabel(self.frame_20)
        self.copy_log_lbl.setObjectName(u"copy_log_lbl")
        sizePolicy1.setHeightForWidth(self.copy_log_lbl.sizePolicy().hasHeightForWidth())
        self.copy_log_lbl.setSizePolicy(sizePolicy1)
        self.copy_log_lbl.setMaximumSize(QSize(16777215, 40))
        self.copy_log_lbl.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_34.addWidget(self.copy_log_lbl)

        self.progressBar = QProgressBar(self.frame_20)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(100, 16777215))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #FFA726;\n"
"    border-radius: 10px;\n"
"    background-color: #FFF3E0;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: QLinearGradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 #FFB74D,\n"
"        stop: 1 #FB8C00\n"
"    );\n"
"    border-radius: 8px;\n"
"    width: 20px;\n"
"    margin: 2px;\n"
"\n"
"}\n"
"\n"
"@keyframes moveSlow {\n"
"    0% { margin-left: 0px; }\n"
"    50% { margin-left: 80px; }\n"
"    100% { margin-left: 0px; }\n"
"}")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_34.addWidget(self.progressBar)


        self.verticalLayout_29.addWidget(self.frame_20)

        self.btn_found_errors = QPushButton(self.frame_11)
        self.btn_found_errors.setObjectName(u"btn_found_errors")
        self.btn_found_errors.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_found_errors.setFont(font2)
        self.btn_found_errors.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_found_errors.setStyleSheet(u"background-color: none;\n"
"color:red;\n"
"border:none;")

        self.verticalLayout_29.addWidget(self.btn_found_errors)


        self.verticalLayout_17.addWidget(self.frame_11)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.lbl_ip_error = QLabel(self.copy)
        self.lbl_ip_error.setObjectName(u"lbl_ip_error")
        self.lbl_ip_error.setMinimumSize(QSize(0, 25))
        self.lbl_ip_error.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.lbl_ip_error)

        self.frame_5 = QFrame(self.copy)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 80))
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setFrameShape(QFrame.NoFrame)
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

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.copy_speed_lbl = QLabel(self.frame_5)
        self.copy_speed_lbl.setObjectName(u"copy_speed_lbl")
        sizePolicy5.setHeightForWidth(self.copy_speed_lbl.sizePolicy().hasHeightForWidth())
        self.copy_speed_lbl.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.copy_speed_lbl)


        self.verticalLayout_18.addLayout(self.horizontalLayout_5)

        self.progress_bar = QProgressBar(self.frame_5)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setStyleSheet(u"    QProgressBar {\n"
"        border: 2px solid #555;          /* Border color */\n"
"        border-radius: 10px;             /* Rounded corners */\n"
"        text-align: center;              /* Hide text */\n"
"        background-color: #f3f3f3;       /* Background color */\n"
"    }\n"
"\n"
"    QProgressBar::chunk {\n"
"        background-color: #4caf50;       /* Color of the moving chunk */\n"
"        width: 25px;                     /* Width of the moving element */\n"
"        margin: 0px;                     /* No gap between chunks */\n"
"\n"
"    }\n"
"\n"
"    @keyframes move {\n"
"        0% { margin-left: 0%; }\n"
"        50% { margin-left: 80%; }\n"
"        100% { margin-left: 0%; }\n"
"    }")
        self.progress_bar.setValue(0)

        self.verticalLayout_18.addWidget(self.progress_bar)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.copy)
        self.camera_config = QWidget()
        self.camera_config.setObjectName(u"camera_config")
        self.verticalLayout_4 = QVBoxLayout(self.camera_config)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.camera_config)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_14 = QVBoxLayout(self.tab)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, -1, 9)
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 436, 703))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 9)
        self.frame_10 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 30))
        self.frame_10.setMaximumSize(QSize(16777215, 30))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.label_4)

        self.line_train_name = QLineEdit(self.frame_10)
        self.line_train_name.setObjectName(u"line_train_name")

        self.horizontalLayout_11.addWidget(self.line_train_name)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.line_22 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_22)

        self.horizontalFrame1111 = QFrame(self.scrollAreaWidgetContents_3)
        self.horizontalFrame1111.setObjectName(u"horizontalFrame1111")
        sizePolicy4.setHeightForWidth(self.horizontalFrame1111.sizePolicy().hasHeightForWidth())
        self.horizontalFrame1111.setSizePolicy(sizePolicy4)
        self.horizontalLayout_58 = QHBoxLayout(self.horizontalFrame1111)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_67 = QLabel(self.horizontalFrame1111)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(100, 0))
        self.label_67.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_58.addWidget(self.label_67)

        self.new_profile_compression = QComboBox(self.horizontalFrame1111)
        self.new_profile_compression.setObjectName(u"new_profile_compression")

        self.horizontalLayout_58.addWidget(self.new_profile_compression)

        self.horizontalFrame1111_4 = QFrame(self.horizontalFrame1111)
        self.horizontalFrame1111_4.setObjectName(u"horizontalFrame1111_4")
        sizePolicy4.setHeightForWidth(self.horizontalFrame1111_4.sizePolicy().hasHeightForWidth())
        self.horizontalFrame1111_4.setSizePolicy(sizePolicy4)
        self.horizontalLayout_62 = QHBoxLayout(self.horizontalFrame1111_4)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_89 = QLabel(self.horizontalFrame1111_4)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(62, 0))
        self.label_89.setMaximumSize(QSize(62, 16777215))

        self.horizontalLayout_62.addWidget(self.label_89)

        self.new_profile_motion = QComboBox(self.horizontalFrame1111_4)
        self.new_profile_motion.setObjectName(u"new_profile_motion")

        self.horizontalLayout_62.addWidget(self.new_profile_motion)


        self.horizontalLayout_58.addWidget(self.horizontalFrame1111_4)


        self.verticalLayout_6.addWidget(self.horizontalFrame1111)

        self.line_24 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.VLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_24)

        self.line_15 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_15)

        self.group_camera_1 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.group_camera_1.setObjectName(u"group_camera_1")
        self.group_camera_1.setMaximumSize(QSize(16777215, 156))
        self.group_camera_1.setCheckable(True)
        self.group_camera_1.setChecked(False)
        self.gridLayout_6 = QGridLayout(self.group_camera_1)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.group_camera_1)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 1, 0, 1, 1)

        self.label_39 = QLabel(self.group_camera_1)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 0, 0, 1, 1)

        self.line_ip_camera_1 = QLineEdit(self.group_camera_1)
        self.line_ip_camera_1.setObjectName(u"line_ip_camera_1")

        self.gridLayout_6.addWidget(self.line_ip_camera_1, 1, 1, 1, 1)

        self.label_35 = QLabel(self.group_camera_1)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_6.addWidget(self.label_35, 1, 2, 1, 1)

        self.line_port_camera_1 = QLineEdit(self.group_camera_1)
        self.line_port_camera_1.setObjectName(u"line_port_camera_1")

        self.gridLayout_6.addWidget(self.line_port_camera_1, 1, 3, 1, 1)

        self.line_name_camera_1 = QLineEdit(self.group_camera_1)
        self.line_name_camera_1.setObjectName(u"line_name_camera_1")
        self.line_name_camera_1.setMaximumSize(QSize(174, 16777215))

        self.gridLayout_6.addWidget(self.line_name_camera_1, 0, 1, 1, 1)

        self.label_40 = QLabel(self.group_camera_1)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 2, 0, 1, 1)

        self.line_username_camera_1 = QLineEdit(self.group_camera_1)
        self.line_username_camera_1.setObjectName(u"line_username_camera_1")

        self.gridLayout_6.addWidget(self.line_username_camera_1, 2, 1, 1, 1)

        self.label_41 = QLabel(self.group_camera_1)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 2, 2, 1, 1)

        self.line_password_camera_1 = QLineEdit(self.group_camera_1)
        self.line_password_camera_1.setObjectName(u"line_password_camera_1")

        self.gridLayout_6.addWidget(self.line_password_camera_1, 2, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.group_camera_1)

        self.group_camera_2 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.group_camera_2.setObjectName(u"group_camera_2")
        self.group_camera_2.setEnabled(True)
        self.group_camera_2.setCheckable(True)
        self.group_camera_2.setChecked(False)
        self.gridLayout_7 = QGridLayout(self.group_camera_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.line_port_camera_2 = QLineEdit(self.group_camera_2)
        self.line_port_camera_2.setObjectName(u"line_port_camera_2")

        self.gridLayout_7.addWidget(self.line_port_camera_2, 1, 3, 1, 1)

        self.label_43 = QLabel(self.group_camera_2)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_7.addWidget(self.label_43, 1, 0, 1, 1)

        self.label_44 = QLabel(self.group_camera_2)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_7.addWidget(self.label_44, 1, 2, 1, 1)

        self.line_name_camera_2 = QLineEdit(self.group_camera_2)
        self.line_name_camera_2.setObjectName(u"line_name_camera_2")
        self.line_name_camera_2.setMaximumSize(QSize(174, 16777215))

        self.gridLayout_7.addWidget(self.line_name_camera_2, 0, 1, 1, 1)

        self.line_ip_camera_2 = QLineEdit(self.group_camera_2)
        self.line_ip_camera_2.setObjectName(u"line_ip_camera_2")

        self.gridLayout_7.addWidget(self.line_ip_camera_2, 1, 1, 1, 1)

        self.label_42 = QLabel(self.group_camera_2)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_7.addWidget(self.label_42, 0, 0, 1, 1)

        self.label_45 = QLabel(self.group_camera_2)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_7.addWidget(self.label_45, 2, 0, 1, 1)

        self.line_username_camera_2 = QLineEdit(self.group_camera_2)
        self.line_username_camera_2.setObjectName(u"line_username_camera_2")

        self.gridLayout_7.addWidget(self.line_username_camera_2, 2, 1, 1, 1)

        self.label_46 = QLabel(self.group_camera_2)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_7.addWidget(self.label_46, 2, 2, 1, 1)

        self.line_password_camera_2 = QLineEdit(self.group_camera_2)
        self.line_password_camera_2.setObjectName(u"line_password_camera_2")

        self.gridLayout_7.addWidget(self.line_password_camera_2, 2, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.group_camera_2)

        self.group_camera_3 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.group_camera_3.setObjectName(u"group_camera_3")
        self.group_camera_3.setEnabled(True)
        self.group_camera_3.setCheckable(True)
        self.group_camera_3.setChecked(False)
        self.gridLayout_8 = QGridLayout(self.group_camera_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.group_camera_3)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_8.addWidget(self.label_48, 1, 0, 1, 1)

        self.line_name_camera_3 = QLineEdit(self.group_camera_3)
        self.line_name_camera_3.setObjectName(u"line_name_camera_3")
        self.line_name_camera_3.setMaximumSize(QSize(174, 16777215))

        self.gridLayout_8.addWidget(self.line_name_camera_3, 0, 1, 1, 1)

        self.line_port_camera_3 = QLineEdit(self.group_camera_3)
        self.line_port_camera_3.setObjectName(u"line_port_camera_3")

        self.gridLayout_8.addWidget(self.line_port_camera_3, 1, 3, 1, 1)

        self.label_47 = QLabel(self.group_camera_3)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_8.addWidget(self.label_47, 0, 0, 1, 1)

        self.line_ip_camera_3 = QLineEdit(self.group_camera_3)
        self.line_ip_camera_3.setObjectName(u"line_ip_camera_3")

        self.gridLayout_8.addWidget(self.line_ip_camera_3, 1, 1, 1, 1)

        self.label_49 = QLabel(self.group_camera_3)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_8.addWidget(self.label_49, 1, 2, 1, 1)

        self.label_50 = QLabel(self.group_camera_3)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_8.addWidget(self.label_50, 2, 0, 1, 1)

        self.line_username_camera_3 = QLineEdit(self.group_camera_3)
        self.line_username_camera_3.setObjectName(u"line_username_camera_3")

        self.gridLayout_8.addWidget(self.line_username_camera_3, 2, 1, 1, 1)

        self.label_63 = QLabel(self.group_camera_3)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_8.addWidget(self.label_63, 2, 2, 1, 1)

        self.line_password_camera_3 = QLineEdit(self.group_camera_3)
        self.line_password_camera_3.setObjectName(u"line_password_camera_3")

        self.gridLayout_8.addWidget(self.line_password_camera_3, 2, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.group_camera_3)

        self.group_camera_4 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.group_camera_4.setObjectName(u"group_camera_4")
        self.group_camera_4.setEnabled(True)
        self.group_camera_4.setCheckable(True)
        self.group_camera_4.setChecked(False)
        self.gridLayout_9 = QGridLayout(self.group_camera_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.line_name_camera_4 = QLineEdit(self.group_camera_4)
        self.line_name_camera_4.setObjectName(u"line_name_camera_4")
        self.line_name_camera_4.setMaximumSize(QSize(174, 16777215))

        self.gridLayout_9.addWidget(self.line_name_camera_4, 0, 1, 1, 1)

        self.line_port_camera_4 = QLineEdit(self.group_camera_4)
        self.line_port_camera_4.setObjectName(u"line_port_camera_4")

        self.gridLayout_9.addWidget(self.line_port_camera_4, 1, 3, 1, 1)

        self.label_86 = QLabel(self.group_camera_4)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_9.addWidget(self.label_86, 1, 2, 1, 1)

        self.label_64 = QLabel(self.group_camera_4)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_9.addWidget(self.label_64, 0, 0, 1, 1)

        self.line_ip_camera_4 = QLineEdit(self.group_camera_4)
        self.line_ip_camera_4.setObjectName(u"line_ip_camera_4")

        self.gridLayout_9.addWidget(self.line_ip_camera_4, 1, 1, 1, 1)

        self.label_85 = QLabel(self.group_camera_4)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_9.addWidget(self.label_85, 1, 0, 1, 1)

        self.label_87 = QLabel(self.group_camera_4)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_9.addWidget(self.label_87, 2, 0, 1, 1)

        self.line_username_camera_4 = QLineEdit(self.group_camera_4)
        self.line_username_camera_4.setObjectName(u"line_username_camera_4")

        self.gridLayout_9.addWidget(self.line_username_camera_4, 2, 1, 1, 1)

        self.label_88 = QLabel(self.group_camera_4)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_9.addWidget(self.label_88, 2, 2, 1, 1)

        self.line_password_camera_4 = QLineEdit(self.group_camera_4)
        self.line_password_camera_4.setObjectName(u"line_password_camera_4")

        self.gridLayout_9.addWidget(self.line_password_camera_4, 2, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.group_camera_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_14.addWidget(self.scrollArea)

        self.label_profile_message = QLabel(self.tab)
        self.label_profile_message.setObjectName(u"label_profile_message")
        self.label_profile_message.setMinimumSize(QSize(0, 30))
        self.label_profile_message.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_14.addWidget(self.label_profile_message)

        self.btn_save_profile = QPushButton(self.tab)
        self.btn_save_profile.setObjectName(u"btn_save_profile")
        self.btn_save_profile.setMinimumSize(QSize(95, 0))
        self.btn_save_profile.setMaximumSize(QSize(95, 16777215))
        self.btn_save_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_profile.setIconSize(QSize(29, 23))

        self.verticalLayout_14.addWidget(self.btn_save_profile, 0, Qt.AlignHCenter)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 9)
        self.frame_12 = QFrame(self.tab_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 30))
        self.frame_12.setMaximumSize(QSize(16777215, 30))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 0))
        self.label_11.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_13.addWidget(self.label_11)

        self.btn_refresh_profile_name = QPushButton(self.frame_12)
        self.btn_refresh_profile_name.setObjectName(u"btn_refresh_profile_name")
        self.btn_refresh_profile_name.setEnabled(True)
        self.btn_refresh_profile_name.setMinimumSize(QSize(20, 0))
        self.btn_refresh_profile_name.setMaximumSize(QSize(20, 16777215))
        self.btn_refresh_profile_name.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_refresh_profile_name.setStyleSheet(u"background-color: None;\n"
"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/asstets/icons/refresh_5730689.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_refresh_profile_name.setIcon(icon7)
        self.btn_refresh_profile_name.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.btn_refresh_profile_name)

        self.combo_train_name_profile = QComboBox(self.frame_12)
        self.combo_train_name_profile.setObjectName(u"combo_train_name_profile")

        self.horizontalLayout_13.addWidget(self.combo_train_name_profile)

        self.btn_edit_profile = QPushButton(self.frame_12)
        self.btn_edit_profile.setObjectName(u"btn_edit_profile")
        self.btn_edit_profile.setEnabled(True)
        self.btn_edit_profile.setMinimumSize(QSize(30, 0))
        self.btn_edit_profile.setMaximumSize(QSize(30, 16777215))
        self.btn_edit_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_edit_profile.setStyleSheet(u"background-color: None;\n"
"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/asstets/icons/pencil_5171801.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_edit_profile.setIcon(icon8)
        self.btn_edit_profile.setIconSize(QSize(30, 30))

        self.horizontalLayout_13.addWidget(self.btn_edit_profile)

        self.btn_delete_profile = QPushButton(self.frame_12)
        self.btn_delete_profile.setObjectName(u"btn_delete_profile")
        self.btn_delete_profile.setMaximumSize(QSize(30, 16777215))
        self.btn_delete_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_profile.setStyleSheet(u"background-color: None;\n"
"border:none;")
        icon9 = QIcon()
        icon9.addFile(u":/asstets/icons/trash_9915690.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_profile.setIcon(icon9)
        self.btn_delete_profile.setIconSize(QSize(30, 30))

        self.horizontalLayout_13.addWidget(self.btn_delete_profile)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.frame_profile_edit = QScrollArea(self.tab_2)
        self.frame_profile_edit.setObjectName(u"frame_profile_edit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_profile_edit.sizePolicy().hasHeightForWidth())
        self.frame_profile_edit.setSizePolicy(sizePolicy6)
        self.frame_profile_edit.setMaximumSize(QSize(16777215, 16777215))
        self.frame_profile_edit.setFrameShape(QFrame.NoFrame)
        self.frame_profile_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.frame_profile_edit.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 436, 800))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalFrame1111_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.horizontalFrame1111_3.setObjectName(u"horizontalFrame1111_3")
        sizePolicy4.setHeightForWidth(self.horizontalFrame1111_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame1111_3.setSizePolicy(sizePolicy4)
        self.horizontalLayout_65 = QHBoxLayout(self.horizontalFrame1111_3)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_111 = QLabel(self.horizontalFrame1111_3)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMinimumSize(QSize(100, 0))
        self.label_111.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_65.addWidget(self.label_111)

        self.edit_profile_name = QLineEdit(self.horizontalFrame1111_3)
        self.edit_profile_name.setObjectName(u"edit_profile_name")

        self.horizontalLayout_65.addWidget(self.edit_profile_name)


        self.verticalLayout_3.addWidget(self.horizontalFrame1111_3)

        self.horizontalFrame1111_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.horizontalFrame1111_2.setObjectName(u"horizontalFrame1111_2")
        sizePolicy4.setHeightForWidth(self.horizontalFrame1111_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame1111_2.setSizePolicy(sizePolicy4)
        self.horizontalLayout_60 = QHBoxLayout(self.horizontalFrame1111_2)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_68 = QLabel(self.horizontalFrame1111_2)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(100, 0))
        self.label_68.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_60.addWidget(self.label_68)

        self.edit_profile_compression = QComboBox(self.horizontalFrame1111_2)
        self.edit_profile_compression.setObjectName(u"edit_profile_compression")

        self.horizontalLayout_60.addWidget(self.edit_profile_compression)

        self.horizontalFrame1111_5 = QFrame(self.horizontalFrame1111_2)
        self.horizontalFrame1111_5.setObjectName(u"horizontalFrame1111_5")
        sizePolicy4.setHeightForWidth(self.horizontalFrame1111_5.sizePolicy().hasHeightForWidth())
        self.horizontalFrame1111_5.setSizePolicy(sizePolicy4)
        self.horizontalLayout_63 = QHBoxLayout(self.horizontalFrame1111_5)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_90 = QLabel(self.horizontalFrame1111_5)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMinimumSize(QSize(62, 0))
        self.label_90.setMaximumSize(QSize(62, 16777215))

        self.horizontalLayout_63.addWidget(self.label_90)

        self.edit_profile_motion = QComboBox(self.horizontalFrame1111_5)
        self.edit_profile_motion.setObjectName(u"edit_profile_motion")

        self.horizontalLayout_63.addWidget(self.edit_profile_motion)


        self.horizontalLayout_60.addWidget(self.horizontalFrame1111_5)


        self.verticalLayout_3.addWidget(self.horizontalFrame1111_2)

        self.group_camera_1_edit = QGroupBox(self.scrollAreaWidgetContents_2)
        self.group_camera_1_edit.setObjectName(u"group_camera_1_edit")
        self.group_camera_1_edit.setEnabled(True)
        self.group_camera_1_edit.setMinimumSize(QSize(0, 160))
        self.group_camera_1_edit.setMaximumSize(QSize(16777215, 160))
        self.group_camera_1_edit.setCheckable(True)
        self.group_camera_1_edit.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.group_camera_1_edit)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_70 = QLabel(self.group_camera_1_edit)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_2.addWidget(self.label_70, 1, 2, 1, 1)

        self.label_69 = QLabel(self.group_camera_1_edit)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_2.addWidget(self.label_69, 0, 0, 1, 1)

        self.line_name_camera_1_edit = QLineEdit(self.group_camera_1_edit)
        self.line_name_camera_1_edit.setObjectName(u"line_name_camera_1_edit")
        self.line_name_camera_1_edit.setMaximumSize(QSize(177, 16777215))

        self.gridLayout_2.addWidget(self.line_name_camera_1_edit, 0, 1, 1, 1)

        self.line_ip_camera_1_edit = QLineEdit(self.group_camera_1_edit)
        self.line_ip_camera_1_edit.setObjectName(u"line_ip_camera_1_edit")

        self.gridLayout_2.addWidget(self.line_ip_camera_1_edit, 1, 1, 1, 1)

        self.line_port_camera_1_edit = QLineEdit(self.group_camera_1_edit)
        self.line_port_camera_1_edit.setObjectName(u"line_port_camera_1_edit")

        self.gridLayout_2.addWidget(self.line_port_camera_1_edit, 1, 3, 1, 1)

        self.label_51 = QLabel(self.group_camera_1_edit)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_2.addWidget(self.label_51, 1, 0, 1, 1)

        self.label_71 = QLabel(self.group_camera_1_edit)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_2.addWidget(self.label_71, 2, 0, 1, 1)

        self.line_username_camera_1_edit = QLineEdit(self.group_camera_1_edit)
        self.line_username_camera_1_edit.setObjectName(u"line_username_camera_1_edit")

        self.gridLayout_2.addWidget(self.line_username_camera_1_edit, 2, 1, 1, 1)

        self.label_72 = QLabel(self.group_camera_1_edit)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_2.addWidget(self.label_72, 2, 2, 1, 1)

        self.line_password_camera_1_edit = QLineEdit(self.group_camera_1_edit)
        self.line_password_camera_1_edit.setObjectName(u"line_password_camera_1_edit")

        self.gridLayout_2.addWidget(self.line_password_camera_1_edit, 2, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.group_camera_1_edit)

        self.group_camera_2_edit = QGroupBox(self.scrollAreaWidgetContents_2)
        self.group_camera_2_edit.setObjectName(u"group_camera_2_edit")
        self.group_camera_2_edit.setEnabled(True)
        self.group_camera_2_edit.setMinimumSize(QSize(0, 160))
        self.group_camera_2_edit.setCheckable(True)
        self.group_camera_2_edit.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.group_camera_2_edit)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_port_camera_2_edit = QLineEdit(self.group_camera_2_edit)
        self.line_port_camera_2_edit.setObjectName(u"line_port_camera_2_edit")

        self.gridLayout_3.addWidget(self.line_port_camera_2_edit, 1, 3, 1, 1)

        self.line_ip_camera_2_edit = QLineEdit(self.group_camera_2_edit)
        self.line_ip_camera_2_edit.setObjectName(u"line_ip_camera_2_edit")

        self.gridLayout_3.addWidget(self.line_ip_camera_2_edit, 1, 1, 1, 1)

        self.line_name_camera_2_edit = QLineEdit(self.group_camera_2_edit)
        self.line_name_camera_2_edit.setObjectName(u"line_name_camera_2_edit")
        self.line_name_camera_2_edit.setMaximumSize(QSize(177, 16777215))

        self.gridLayout_3.addWidget(self.line_name_camera_2_edit, 0, 1, 1, 1)

        self.label_52 = QLabel(self.group_camera_2_edit)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_3.addWidget(self.label_52, 1, 0, 1, 1)

        self.label_73 = QLabel(self.group_camera_2_edit)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_3.addWidget(self.label_73, 0, 0, 1, 1)

        self.label_74 = QLabel(self.group_camera_2_edit)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_3.addWidget(self.label_74, 1, 2, 1, 1)

        self.label_75 = QLabel(self.group_camera_2_edit)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_3.addWidget(self.label_75, 2, 0, 1, 1)

        self.line_username_camera_2_edit = QLineEdit(self.group_camera_2_edit)
        self.line_username_camera_2_edit.setObjectName(u"line_username_camera_2_edit")

        self.gridLayout_3.addWidget(self.line_username_camera_2_edit, 2, 1, 1, 1)

        self.label_76 = QLabel(self.group_camera_2_edit)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_3.addWidget(self.label_76, 2, 2, 1, 1)

        self.line_password_camera_2_edit = QLineEdit(self.group_camera_2_edit)
        self.line_password_camera_2_edit.setObjectName(u"line_password_camera_2_edit")

        self.gridLayout_3.addWidget(self.line_password_camera_2_edit, 2, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.group_camera_2_edit)

        self.group_camera_3_edit = QGroupBox(self.scrollAreaWidgetContents_2)
        self.group_camera_3_edit.setObjectName(u"group_camera_3_edit")
        self.group_camera_3_edit.setEnabled(True)
        self.group_camera_3_edit.setMinimumSize(QSize(0, 160))
        self.group_camera_3_edit.setCheckable(True)
        self.group_camera_3_edit.setChecked(False)
        self.gridLayout_4 = QGridLayout(self.group_camera_3_edit)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_ip_camera_3_edit = QLineEdit(self.group_camera_3_edit)
        self.line_ip_camera_3_edit.setObjectName(u"line_ip_camera_3_edit")

        self.gridLayout_4.addWidget(self.line_ip_camera_3_edit, 1, 1, 1, 1)

        self.line_name_camera_3_edit = QLineEdit(self.group_camera_3_edit)
        self.line_name_camera_3_edit.setObjectName(u"line_name_camera_3_edit")
        self.line_name_camera_3_edit.setMaximumSize(QSize(177, 16777215))

        self.gridLayout_4.addWidget(self.line_name_camera_3_edit, 0, 1, 1, 1)

        self.label_61 = QLabel(self.group_camera_3_edit)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_4.addWidget(self.label_61, 1, 0, 1, 1)

        self.label_78 = QLabel(self.group_camera_3_edit)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_4.addWidget(self.label_78, 1, 2, 1, 1)

        self.line_port_camera_3_edit = QLineEdit(self.group_camera_3_edit)
        self.line_port_camera_3_edit.setObjectName(u"line_port_camera_3_edit")

        self.gridLayout_4.addWidget(self.line_port_camera_3_edit, 1, 3, 1, 1)

        self.label_77 = QLabel(self.group_camera_3_edit)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_4.addWidget(self.label_77, 0, 0, 1, 1)

        self.label_79 = QLabel(self.group_camera_3_edit)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_4.addWidget(self.label_79, 2, 0, 1, 1)

        self.line_username_camera_3_edit = QLineEdit(self.group_camera_3_edit)
        self.line_username_camera_3_edit.setObjectName(u"line_username_camera_3_edit")

        self.gridLayout_4.addWidget(self.line_username_camera_3_edit, 2, 1, 1, 1)

        self.label_80 = QLabel(self.group_camera_3_edit)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_4.addWidget(self.label_80, 2, 2, 1, 1)

        self.line_password_camera_3_edit = QLineEdit(self.group_camera_3_edit)
        self.line_password_camera_3_edit.setObjectName(u"line_password_camera_3_edit")

        self.gridLayout_4.addWidget(self.line_password_camera_3_edit, 2, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.group_camera_3_edit)

        self.group_camera_4_edit = QGroupBox(self.scrollAreaWidgetContents_2)
        self.group_camera_4_edit.setObjectName(u"group_camera_4_edit")
        self.group_camera_4_edit.setEnabled(True)
        self.group_camera_4_edit.setMinimumSize(QSize(0, 160))
        self.group_camera_4_edit.setCheckable(True)
        self.group_camera_4_edit.setChecked(False)
        self.gridLayout_5 = QGridLayout(self.group_camera_4_edit)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.line_port_camera_4_edit = QLineEdit(self.group_camera_4_edit)
        self.line_port_camera_4_edit.setObjectName(u"line_port_camera_4_edit")

        self.gridLayout_5.addWidget(self.line_port_camera_4_edit, 1, 3, 1, 1)

        self.label_81 = QLabel(self.group_camera_4_edit)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_5.addWidget(self.label_81, 0, 0, 1, 1)

        self.line_name_camera_4_edit = QLineEdit(self.group_camera_4_edit)
        self.line_name_camera_4_edit.setObjectName(u"line_name_camera_4_edit")
        self.line_name_camera_4_edit.setMaximumSize(QSize(177, 16777215))

        self.gridLayout_5.addWidget(self.line_name_camera_4_edit, 0, 1, 1, 1)

        self.line_ip_camera_4_edit = QLineEdit(self.group_camera_4_edit)
        self.line_ip_camera_4_edit.setObjectName(u"line_ip_camera_4_edit")

        self.gridLayout_5.addWidget(self.line_ip_camera_4_edit, 1, 1, 1, 1)

        self.label_62 = QLabel(self.group_camera_4_edit)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_5.addWidget(self.label_62, 1, 0, 1, 1)

        self.label_82 = QLabel(self.group_camera_4_edit)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_5.addWidget(self.label_82, 1, 2, 1, 1)

        self.label_83 = QLabel(self.group_camera_4_edit)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_5.addWidget(self.label_83, 2, 0, 1, 1)

        self.line_username_camera_4_edit = QLineEdit(self.group_camera_4_edit)
        self.line_username_camera_4_edit.setObjectName(u"line_username_camera_4_edit")

        self.gridLayout_5.addWidget(self.line_username_camera_4_edit, 2, 1, 1, 1)

        self.label_84 = QLabel(self.group_camera_4_edit)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_5.addWidget(self.label_84, 2, 2, 1, 1)

        self.line_password_camera_4_edit = QLineEdit(self.group_camera_4_edit)
        self.line_password_camera_4_edit.setObjectName(u"line_password_camera_4_edit")

        self.gridLayout_5.addWidget(self.line_password_camera_4_edit, 2, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.group_camera_4_edit)

        self.frame_profile_edit.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.frame_profile_edit)

        self.label_profile_edit_message = QLabel(self.tab_2)
        self.label_profile_edit_message.setObjectName(u"label_profile_edit_message")
        self.label_profile_edit_message.setMinimumSize(QSize(0, 30))
        self.label_profile_edit_message.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_5.addWidget(self.label_profile_edit_message)

        self.frame_22 = QFrame(self.tab_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_save_edit_profile = QPushButton(self.frame_22)
        self.btn_save_edit_profile.setObjectName(u"btn_save_edit_profile")
        self.btn_save_edit_profile.setMinimumSize(QSize(95, 0))
        self.btn_save_edit_profile.setMaximumSize(QSize(95, 16777215))
        self.btn_save_edit_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_22.addWidget(self.btn_save_edit_profile)

        self.btn_cancel_edit_profile = QPushButton(self.frame_22)
        self.btn_cancel_edit_profile.setObjectName(u"btn_cancel_edit_profile")
        self.btn_cancel_edit_profile.setMinimumSize(QSize(95, 0))
        self.btn_cancel_edit_profile.setMaximumSize(QSize(95, 16777215))
        self.btn_cancel_edit_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancel_edit_profile.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	color:rgb(33, 33, 33);\n"
"	border: 1px solid rgb(33, 33, 33);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(217, 217, 217);\n"
"\n"
"}")

        self.horizontalLayout_22.addWidget(self.btn_cancel_edit_profile)


        self.verticalLayout_5.addWidget(self.frame_22)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_7 = QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.groupBox)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMaximumSize(QSize(16777215, 50))
        self.frame_62.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.frame_62)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 0))
        self.label_12.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_16.addWidget(self.label_12)

        self.combo_send_profile_name = QComboBox(self.frame_62)
        self.combo_send_profile_name.setObjectName(u"combo_send_profile_name")
        self.combo_send_profile_name.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_16.addWidget(self.combo_send_profile_name)


        self.verticalLayout_8.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.groupBox)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMaximumSize(QSize(16777215, 50))
        self.frame_63.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_13 = QLabel(self.frame_63)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 0))
        self.label_13.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_21.addWidget(self.label_13)

        self.combo_send_train_name = QComboBox(self.frame_63)
        self.combo_send_train_name.setObjectName(u"combo_send_train_name")
        self.combo_send_train_name.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_21.addWidget(self.combo_send_train_name)


        self.verticalLayout_8.addWidget(self.frame_63)

        self.send_config_msg = QLabel(self.groupBox)
        self.send_config_msg.setObjectName(u"send_config_msg")
        sizePolicy1.setHeightForWidth(self.send_config_msg.sizePolicy().hasHeightForWidth())
        self.send_config_msg.setSizePolicy(sizePolicy1)
        self.send_config_msg.setMaximumSize(QSize(16777215, 40))
        self.send_config_msg.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.send_config_msg)

        self.frame_14 = QFrame(self.groupBox)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 50))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btn_send_profile = QPushButton(self.frame_14)
        self.btn_send_profile.setObjectName(u"btn_send_profile")
        self.btn_send_profile.setMinimumSize(QSize(0, 30))
        self.btn_send_profile.setMaximumSize(QSize(150, 16777215))
        self.btn_send_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.btn_send_profile)


        self.verticalLayout_8.addWidget(self.frame_14)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.line_3 = QFrame(self.tab_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_3)

        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_65 = QFrame(self.groupBox_2)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMaximumSize(QSize(16777215, 50))
        self.frame_65.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_29 = QLabel(self.frame_65)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(100, 0))
        self.label_29.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_35.addWidget(self.label_29)

        self.combo_load_train_name = QComboBox(self.frame_65)
        self.combo_load_train_name.setObjectName(u"combo_load_train_name")
        self.combo_load_train_name.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_35.addWidget(self.combo_load_train_name)


        self.verticalLayout_23.addWidget(self.frame_65)

        self.frame_16 = QFrame(self.groupBox_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 40))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.label_5)

        self.line_ip_load = QLineEdit(self.frame_16)
        self.line_ip_load.setObjectName(u"line_ip_load")

        self.horizontalLayout_12.addWidget(self.line_ip_load)


        self.verticalLayout_23.addWidget(self.frame_16)

        self.load_config_msg = QLabel(self.groupBox_2)
        self.load_config_msg.setObjectName(u"load_config_msg")
        sizePolicy1.setHeightForWidth(self.load_config_msg.sizePolicy().hasHeightForWidth())
        self.load_config_msg.setSizePolicy(sizePolicy1)
        self.load_config_msg.setMaximumSize(QSize(16777215, 40))
        self.load_config_msg.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_23.addWidget(self.load_config_msg)

        self.frame_15 = QFrame(self.groupBox_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.btn_load_profile = QPushButton(self.frame_15)
        self.btn_load_profile.setObjectName(u"btn_load_profile")
        self.btn_load_profile.setMinimumSize(QSize(0, 30))
        self.btn_load_profile.setMaximumSize(QSize(150, 16777215))
        self.btn_load_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_36.addWidget(self.btn_load_profile)


        self.verticalLayout_23.addWidget(self.frame_15)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.camera_config)
        self.train_config = QWidget()
        self.train_config.setObjectName(u"train_config")
        self.verticalLayout_32 = QVBoxLayout(self.train_config)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.tabWidget_2 = QTabWidget(self.train_config)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setEnabled(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_31 = QVBoxLayout(self.tab_5)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_55 = QFrame(self.tab_5)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_56 = QLabel(self.frame_55)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(100, 0))
        self.label_56.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_52.addWidget(self.label_56)

        self.line_train_profile_name = QLineEdit(self.frame_55)
        self.line_train_profile_name.setObjectName(u"line_train_profile_name")

        self.horizontalLayout_52.addWidget(self.line_train_profile_name)


        self.verticalLayout_31.addWidget(self.frame_55)

        self.line_17 = QFrame(self.tab_5)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_17)

        self.frame_6 = QFrame(self.tab_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_53 = QLabel(self.frame_6)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(100, 0))
        self.label_53.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.label_53)

        self.line_train_profile_ip = QLineEdit(self.frame_6)
        self.line_train_profile_ip.setObjectName(u"line_train_profile_ip")

        self.horizontalLayout_6.addWidget(self.line_train_profile_ip)


        self.verticalLayout_31.addWidget(self.frame_6)

        self.line_18 = QFrame(self.tab_5)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_18)

        self.frame_8 = QFrame(self.tab_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_54 = QLabel(self.frame_8)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(100, 0))
        self.label_54.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.label_54)

        self.line_train_profile_username = QLineEdit(self.frame_8)
        self.line_train_profile_username.setObjectName(u"line_train_profile_username")

        self.horizontalLayout_7.addWidget(self.line_train_profile_username)


        self.verticalLayout_31.addWidget(self.frame_8)

        self.line_19 = QFrame(self.tab_5)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_19)

        self.frame_9 = QFrame(self.tab_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_55 = QLabel(self.frame_9)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(100, 0))
        self.label_55.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.label_55)

        self.line_train_profile_password = QLineEdit(self.frame_9)
        self.line_train_profile_password.setObjectName(u"line_train_profile_password")
        self.line_train_profile_password.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.line_train_profile_password)


        self.verticalLayout_31.addWidget(self.frame_9)

        self.line_20 = QFrame(self.tab_5)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_20)

        self.frame_54 = QFrame(self.tab_5)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_save_train = QPushButton(self.frame_54)
        self.btn_save_train.setObjectName(u"btn_save_train")
        self.btn_save_train.setEnabled(True)
        self.btn_save_train.setMaximumSize(QSize(200, 16777215))
        self.btn_save_train.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.btn_save_train)


        self.verticalLayout_31.addWidget(self.frame_54)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_4)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_16 = QVBoxLayout(self.tab_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_57 = QFrame(self.tab_6)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(16777215, 67))
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_57 = QLabel(self.frame_57)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(100, 0))
        self.label_57.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_53.addWidget(self.label_57)

        self.btn_refresh_name_config_edit = QPushButton(self.frame_57)
        self.btn_refresh_name_config_edit.setObjectName(u"btn_refresh_name_config_edit")
        self.btn_refresh_name_config_edit.setMaximumSize(QSize(20, 16777215))
        self.btn_refresh_name_config_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_refresh_name_config_edit.setStyleSheet(u"background-color: None;\n"
"border:none;")
        self.btn_refresh_name_config_edit.setIcon(icon7)
        self.btn_refresh_name_config_edit.setIconSize(QSize(20, 20))

        self.horizontalLayout_53.addWidget(self.btn_refresh_name_config_edit)

        self.combo_train_name_config = QComboBox(self.frame_57)
        self.combo_train_name_config.setObjectName(u"combo_train_name_config")

        self.horizontalLayout_53.addWidget(self.combo_train_name_config)

        self.btn_edit_config = QPushButton(self.frame_57)
        self.btn_edit_config.setObjectName(u"btn_edit_config")
        self.btn_edit_config.setEnabled(True)
        self.btn_edit_config.setMaximumSize(QSize(30, 16777215))
        self.btn_edit_config.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_edit_config.setStyleSheet(u"background-color: None;\n"
"border:none;")
        self.btn_edit_config.setIcon(icon8)
        self.btn_edit_config.setIconSize(QSize(30, 30))

        self.horizontalLayout_53.addWidget(self.btn_edit_config)

        self.btn_delete_config = QPushButton(self.frame_57)
        self.btn_delete_config.setObjectName(u"btn_delete_config")
        self.btn_delete_config.setMaximumSize(QSize(30, 16777215))
        self.btn_delete_config.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_config.setStyleSheet(u"background-color: None;\n"
"border:none;")
        self.btn_delete_config.setIcon(icon9)
        self.btn_delete_config.setIconSize(QSize(30, 30))

        self.horizontalLayout_53.addWidget(self.btn_delete_config)


        self.verticalLayout_16.addWidget(self.frame_57)

        self.frame_train_edit = QFrame(self.tab_6)
        self.frame_train_edit.setObjectName(u"frame_train_edit")
        self.frame_train_edit.setEnabled(False)
        self.frame_train_edit.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_11 = QVBoxLayout(self.frame_train_edit)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_26 = QFrame(self.frame_train_edit)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_60 = QLabel(self.frame_26)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(100, 0))
        self.label_60.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_25.addWidget(self.label_60)

        self.line_train_profile_ip_edit = QLineEdit(self.frame_26)
        self.line_train_profile_ip_edit.setObjectName(u"line_train_profile_ip_edit")

        self.horizontalLayout_25.addWidget(self.line_train_profile_ip_edit)


        self.verticalLayout_11.addWidget(self.frame_26)

        self.frame_19 = QFrame(self.frame_train_edit)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_58 = QLabel(self.frame_19)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(100, 0))
        self.label_58.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.label_58)

        self.line_train_profile_username_edit = QLineEdit(self.frame_19)
        self.line_train_profile_username_edit.setObjectName(u"line_train_profile_username_edit")

        self.horizontalLayout_10.addWidget(self.line_train_profile_username_edit)


        self.verticalLayout_11.addWidget(self.frame_19)

        self.frame_25 = QFrame(self.frame_train_edit)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_59 = QLabel(self.frame_25)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(100, 0))
        self.label_59.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_20.addWidget(self.label_59)

        self.line_train_profile_password_edit = QLineEdit(self.frame_25)
        self.line_train_profile_password_edit.setObjectName(u"line_train_profile_password_edit")

        self.horizontalLayout_20.addWidget(self.line_train_profile_password_edit)


        self.verticalLayout_11.addWidget(self.frame_25)

        self.frame_23 = QFrame(self.frame_train_edit)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.btn_save_config_edit = QPushButton(self.frame_23)
        self.btn_save_config_edit.setObjectName(u"btn_save_config_edit")
        self.btn_save_config_edit.setEnabled(False)
        self.btn_save_config_edit.setMinimumSize(QSize(200, 25))
        self.btn_save_config_edit.setMaximumSize(QSize(200, 16777215))
        self.btn_save_config_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.btn_save_config_edit)

        self.btn_cancel_config_edit = QPushButton(self.frame_23)
        self.btn_cancel_config_edit.setObjectName(u"btn_cancel_config_edit")
        self.btn_cancel_config_edit.setEnabled(False)
        self.btn_cancel_config_edit.setMinimumSize(QSize(200, 25))
        self.btn_cancel_config_edit.setMaximumSize(QSize(200, 16777215))
        self.btn_cancel_config_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.btn_cancel_config_edit)


        self.verticalLayout_11.addWidget(self.frame_23)


        self.verticalLayout_16.addWidget(self.frame_train_edit)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.verticalLayout_32.addWidget(self.tabWidget_2)

        self.stackedWidget.addWidget(self.train_config)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_9 = QVBoxLayout(self.settings)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_2 = QFrame(self.settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(109, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.btn_change_password = QPushButton(self.frame_2)
        self.btn_change_password.setObjectName(u"btn_change_password")
        self.btn_change_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btn_change_password)


        self.verticalLayout_9.addWidget(self.frame_2)

        self.line_11 = QFrame(self.settings)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_11)

        self.frame_35 = QFrame(self.settings)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_14 = QLabel(self.frame_35)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(109, 16777215))

        self.horizontalLayout_57.addWidget(self.label_14)

        self.btn_local_update = QPushButton(self.frame_35)
        self.btn_local_update.setObjectName(u"btn_local_update")
        self.btn_local_update.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_57.addWidget(self.btn_local_update)


        self.verticalLayout_9.addWidget(self.frame_35)

        self.frame_change_password = QFrame(self.settings)
        self.frame_change_password.setObjectName(u"frame_change_password")
        self.frame_change_password.setMinimumSize(QSize(0, 0))
        self.frame_change_password.setMaximumSize(QSize(16777215, 0))
        self.frame_change_password.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_21 = QVBoxLayout(self.frame_change_password)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(30, -1, 30, -1)
        self.frame_4 = QFrame(self.frame_change_password)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(195, 0))
        self.label_15.setMaximumSize(QSize(195, 16777215))

        self.horizontalLayout_18.addWidget(self.label_15)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)

        self.line_current_password = QLineEdit(self.frame_4)
        self.line_current_password.setObjectName(u"line_current_password")
        self.line_current_password.setMinimumSize(QSize(102, 27))
        self.line_current_password.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_18.addWidget(self.line_current_password)


        self.verticalLayout_21.addWidget(self.frame_4)

        self.frame_17 = QFrame(self.frame_change_password)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_16 = QLabel(self.frame_17)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(110, 0))
        self.label_16.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_19.addWidget(self.label_16)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_10)

        self.line_new_password = QLineEdit(self.frame_17)
        self.line_new_password.setObjectName(u"line_new_password")
        self.line_new_password.setMinimumSize(QSize(102, 27))
        self.line_new_password.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_19.addWidget(self.line_new_password)


        self.verticalLayout_21.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_change_password)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_22 = QLabel(self.frame_18)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(110, 0))
        self.label_22.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_26.addWidget(self.label_22)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_11)

        self.line_confirm_password = QLineEdit(self.frame_18)
        self.line_confirm_password.setObjectName(u"line_confirm_password")
        self.line_confirm_password.setMinimumSize(QSize(102, 27))
        self.line_confirm_password.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_26.addWidget(self.line_confirm_password)


        self.verticalLayout_21.addWidget(self.frame_18)

        self.btn_save_password = QPushButton(self.frame_change_password)
        self.btn_save_password.setObjectName(u"btn_save_password")
        self.btn_save_password.setMinimumSize(QSize(100, 0))
        self.btn_save_password.setMaximumSize(QSize(100, 16777215))
        self.btn_save_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_password.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.btn_save_password)


        self.verticalLayout_9.addWidget(self.frame_change_password)

        self.frame_36 = QFrame(self.settings)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_18 = QLabel(self.frame_36)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(109, 16777215))

        self.horizontalLayout_61.addWidget(self.label_18)

        self.btn_storage_manager = QPushButton(self.frame_36)
        self.btn_storage_manager.setObjectName(u"btn_storage_manager")
        self.btn_storage_manager.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_61.addWidget(self.btn_storage_manager)


        self.verticalLayout_9.addWidget(self.frame_36)

        self.frame_storage = QFrame(self.settings)
        self.frame_storage.setObjectName(u"frame_storage")
        self.frame_storage.setMinimumSize(QSize(0, 0))
        self.frame_storage.setMaximumSize(QSize(16777215, 0))
        self.frame_storage.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_15 = QVBoxLayout(self.frame_storage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_31 = QFrame(self.frame_storage)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, -1, 0, -1)
        self.frame_30 = QFrame(self.frame_31)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, -1, 0, -1)
        self.label_21 = QLabel(self.frame_30)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_28.addWidget(self.label_21)

        self.spinBox_min_allow = QSpinBox(self.frame_30)
        self.spinBox_min_allow.setObjectName(u"spinBox_min_allow")
        self.spinBox_min_allow.setMinimumSize(QSize(70, 27))

        self.horizontalLayout_28.addWidget(self.spinBox_min_allow)

        self.label_23 = QLabel(self.frame_30)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_28.addWidget(self.label_23)


        self.horizontalLayout_30.addWidget(self.frame_30)

        self.frame_29 = QFrame(self.frame_31)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, -1, 0, -1)
        self.label_20 = QLabel(self.frame_29)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_27.addWidget(self.label_20)

        self.spinBox_max_allow = QSpinBox(self.frame_29)
        self.spinBox_max_allow.setObjectName(u"spinBox_max_allow")
        self.spinBox_max_allow.setMinimumSize(QSize(70, 27))
        self.spinBox_max_allow.setValue(0)

        self.horizontalLayout_27.addWidget(self.spinBox_max_allow)

        self.label_24 = QLabel(self.frame_29)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_27.addWidget(self.label_24)


        self.horizontalLayout_30.addWidget(self.frame_29)


        self.verticalLayout_15.addWidget(self.frame_31)

        self.btn_save_storage = QPushButton(self.frame_storage)
        self.btn_save_storage.setObjectName(u"btn_save_storage")
        self.btn_save_storage.setMinimumSize(QSize(150, 0))

        self.verticalLayout_15.addWidget(self.btn_save_storage)


        self.verticalLayout_9.addWidget(self.frame_storage)

        self.frame_33 = QFrame(self.settings)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_22 = QVBoxLayout(self.frame_33)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_message_change_password = QLabel(self.frame_33)
        self.label_message_change_password.setObjectName(u"label_message_change_password")
        self.label_message_change_password.setMinimumSize(QSize(0, 14))

        self.verticalLayout_22.addWidget(self.label_message_change_password)


        self.verticalLayout_9.addWidget(self.frame_33)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)

        self.stackedWidget.addWidget(self.settings)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame_27 = QFrame(self.frame)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 50))
        self.frame_27.setMaximumSize(QSize(16777215, 50))
        self.frame_27.setStyleSheet(u"	background-color:rgb(220, 221, 180);\n"
"	border:1px solid #D7D7D9;")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(26, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_2)

        self.label_19 = QLabel(self.frame_27)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(67, 0))
        self.label_19.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_24.addWidget(self.label_19)

        self.storage_widget = QHBoxLayout()
        self.storage_widget.setObjectName(u"storage_widget")

        self.horizontalLayout_24.addLayout(self.storage_widget)


        self.verticalLayout.addWidget(self.frame_27)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.localStyleSheet)

        main.setCentralWidget(self.globalStyleSheet)
        QWidget.setTabOrder(self.line_name_camera_1, self.line_ip_camera_1)
        QWidget.setTabOrder(self.line_ip_camera_1, self.line_port_camera_1)
        QWidget.setTabOrder(self.line_port_camera_1, self.line_username_camera_1)
        QWidget.setTabOrder(self.line_username_camera_1, self.line_password_camera_1)
        QWidget.setTabOrder(self.line_password_camera_1, self.line_name_camera_2)
        QWidget.setTabOrder(self.line_name_camera_2, self.line_ip_camera_2)
        QWidget.setTabOrder(self.line_ip_camera_2, self.line_port_camera_2)
        QWidget.setTabOrder(self.line_port_camera_2, self.line_username_camera_2)
        QWidget.setTabOrder(self.line_username_camera_2, self.line_password_camera_2)
        QWidget.setTabOrder(self.line_password_camera_2, self.line_name_camera_3)
        QWidget.setTabOrder(self.line_name_camera_3, self.line_ip_camera_3)
        QWidget.setTabOrder(self.line_ip_camera_3, self.line_port_camera_3)
        QWidget.setTabOrder(self.line_port_camera_3, self.line_username_camera_3)
        QWidget.setTabOrder(self.line_username_camera_3, self.line_password_camera_3)
        QWidget.setTabOrder(self.line_password_camera_3, self.line_name_camera_4)
        QWidget.setTabOrder(self.line_name_camera_4, self.line_ip_camera_4)
        QWidget.setTabOrder(self.line_ip_camera_4, self.line_port_camera_4)
        QWidget.setTabOrder(self.line_port_camera_4, self.line_username_camera_4)
        QWidget.setTabOrder(self.line_username_camera_4, self.line_password_camera_4)
        QWidget.setTabOrder(self.line_password_camera_4, self.btn_refresh_profile_name)
        QWidget.setTabOrder(self.btn_refresh_profile_name, self.btn_found_errors)
        QWidget.setTabOrder(self.btn_found_errors, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.line_train_name)
        QWidget.setTabOrder(self.line_train_name, self.new_profile_compression)
        QWidget.setTabOrder(self.new_profile_compression, self.group_camera_2)
        QWidget.setTabOrder(self.group_camera_2, self.group_camera_4)
        QWidget.setTabOrder(self.group_camera_4, self.combo_train_name_profile)
        QWidget.setTabOrder(self.combo_train_name_profile, self.btn_edit_profile)
        QWidget.setTabOrder(self.btn_edit_profile, self.btn_delete_profile)
        QWidget.setTabOrder(self.btn_delete_profile, self.frame_profile_edit)
        QWidget.setTabOrder(self.frame_profile_edit, self.edit_profile_compression)
        QWidget.setTabOrder(self.edit_profile_compression, self.group_camera_1_edit)
        QWidget.setTabOrder(self.group_camera_1_edit, self.line_name_camera_1_edit)
        QWidget.setTabOrder(self.line_name_camera_1_edit, self.line_ip_camera_1_edit)
        QWidget.setTabOrder(self.line_ip_camera_1_edit, self.line_port_camera_1_edit)
        QWidget.setTabOrder(self.line_port_camera_1_edit, self.line_username_camera_1_edit)
        QWidget.setTabOrder(self.line_username_camera_1_edit, self.line_password_camera_1_edit)
        QWidget.setTabOrder(self.line_password_camera_1_edit, self.group_camera_2_edit)
        QWidget.setTabOrder(self.group_camera_2_edit, self.group_camera_3_edit)
        QWidget.setTabOrder(self.group_camera_3_edit, self.group_camera_4_edit)
        QWidget.setTabOrder(self.group_camera_4_edit, self.combo_send_profile_name)
        QWidget.setTabOrder(self.combo_send_profile_name, self.combo_send_train_name)
        QWidget.setTabOrder(self.combo_send_train_name, self.btn_send_profile)
        QWidget.setTabOrder(self.btn_send_profile, self.combo_load_train_name)
        QWidget.setTabOrder(self.combo_load_train_name, self.line_ip_load)
        QWidget.setTabOrder(self.line_ip_load, self.btn_load_profile)
        QWidget.setTabOrder(self.btn_load_profile, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.line_train_profile_name)
        QWidget.setTabOrder(self.line_train_profile_name, self.line_train_profile_ip)
        QWidget.setTabOrder(self.line_train_profile_ip, self.line_train_profile_username)
        QWidget.setTabOrder(self.line_train_profile_username, self.line_train_profile_password)
        QWidget.setTabOrder(self.line_train_profile_password, self.btn_save_train)
        QWidget.setTabOrder(self.btn_save_train, self.btn_refresh_name_config_edit)
        QWidget.setTabOrder(self.btn_refresh_name_config_edit, self.combo_train_name_config)
        QWidget.setTabOrder(self.combo_train_name_config, self.btn_edit_config)
        QWidget.setTabOrder(self.btn_edit_config, self.btn_delete_config)
        QWidget.setTabOrder(self.btn_delete_config, self.line_train_profile_ip_edit)
        QWidget.setTabOrder(self.line_train_profile_ip_edit, self.line_train_profile_username_edit)
        QWidget.setTabOrder(self.line_train_profile_username_edit, self.line_train_profile_password_edit)
        QWidget.setTabOrder(self.line_train_profile_password_edit, self.btn_change_password)
        QWidget.setTabOrder(self.btn_change_password, self.line_current_password)
        QWidget.setTabOrder(self.line_current_password, self.line_new_password)
        QWidget.setTabOrder(self.line_new_password, self.line_confirm_password)
        QWidget.setTabOrder(self.line_confirm_password, self.btn_save_password)
        QWidget.setTabOrder(self.btn_save_password, self.btn_local_update)
        QWidget.setTabOrder(self.btn_local_update, self.line_name_camera_2_edit)
        QWidget.setTabOrder(self.line_name_camera_2_edit, self.line_ip_camera_2_edit)
        QWidget.setTabOrder(self.line_ip_camera_2_edit, self.line_port_camera_2_edit)
        QWidget.setTabOrder(self.line_port_camera_2_edit, self.line_username_camera_2_edit)
        QWidget.setTabOrder(self.line_username_camera_2_edit, self.line_password_camera_2_edit)
        QWidget.setTabOrder(self.line_password_camera_2_edit, self.line_name_camera_3_edit)
        QWidget.setTabOrder(self.line_name_camera_3_edit, self.line_ip_camera_3_edit)
        QWidget.setTabOrder(self.line_ip_camera_3_edit, self.line_port_camera_3_edit)
        QWidget.setTabOrder(self.line_port_camera_3_edit, self.line_username_camera_3_edit)
        QWidget.setTabOrder(self.line_username_camera_3_edit, self.line_password_camera_3_edit)
        QWidget.setTabOrder(self.line_password_camera_3_edit, self.line_name_camera_4_edit)
        QWidget.setTabOrder(self.line_name_camera_4_edit, self.line_ip_camera_4_edit)
        QWidget.setTabOrder(self.line_ip_camera_4_edit, self.line_port_camera_4_edit)
        QWidget.setTabOrder(self.line_port_camera_4_edit, self.line_username_camera_4_edit)
        QWidget.setTabOrder(self.line_username_camera_4_edit, self.line_password_camera_4_edit)
        QWidget.setTabOrder(self.line_password_camera_4_edit, self.group_camera_1)
        QWidget.setTabOrder(self.group_camera_1, self.side_copy_btn)
        QWidget.setTabOrder(self.side_copy_btn, self.side_profile_btn)
        QWidget.setTabOrder(self.side_profile_btn, self.side_train_config_btn)
        QWidget.setTabOrder(self.side_train_config_btn, self.side_setting_btn)
        QWidget.setTabOrder(self.side_setting_btn, self.side_about_btn)
        QWidget.setTabOrder(self.side_about_btn, self.login_btn)
        QWidget.setTabOrder(self.login_btn, self.help_btn)
        QWidget.setTabOrder(self.help_btn, self.minimize_btn)
        QWidget.setTabOrder(self.minimize_btn, self.close_btn)
        QWidget.setTabOrder(self.close_btn, self.combo_copy_train_name)
        QWidget.setTabOrder(self.combo_copy_train_name, self.group_camera_3)

        self.retranslateUi(main)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"MainWindow", None))
        self.side_copy_btn.setText(QCoreApplication.translate("main", u"Copy", None))
        self.side_profile_btn.setText(QCoreApplication.translate("main", u"Profile Config", None))
        self.side_train_config_btn.setText(QCoreApplication.translate("main", u"Thin Clients", None))
        self.side_setting_btn.setText(QCoreApplication.translate("main", u"Settings", None))
        self.side_about_btn.setText(QCoreApplication.translate("main", u" About Us ", None))
        self.label_66.setText("")
        self.label_65.setText("")
        self.login_btn.setText(QCoreApplication.translate("main", u"Login", None))
        self.login_btn.setProperty("styleClass", QCoreApplication.translate("main", u"fillBtn", None))
        self.logined_username_lbl.setText("")
        self.help_btn.setText("")
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("main", u"Train Name :", None))
        self.label_2.setText(QCoreApplication.translate("main", u"IP Address : ", None))
        self.label_17.setText(QCoreApplication.translate("main", u"User Name :", None))
        self.timeline_groupbox.setTitle(QCoreApplication.translate("main", u"Time Line Filter", None))
        self.end_calendar_btn.setText("")
        self.end_calendar_btn.setProperty("styleClass", "")
        self.start_calendar_btn.setText("")
        self.start_calendar_btn.setProperty("styleClass", "")
        self.label_31.setText(QCoreApplication.translate("main", u":", None))
        self.label_8.setText(QCoreApplication.translate("main", u":", None))
        self.label_10.setText(QCoreApplication.translate("main", u"From", None))
        self.label_32.setText(QCoreApplication.translate("main", u"Time", None))
        self.label_30.setText(QCoreApplication.translate("main", u"End", None))
        self.label_34.setText(QCoreApplication.translate("main", u"Time", None))
        self.only_copy_new_checkbox.setText(QCoreApplication.translate("main", u"Only Copy New Files", None))
        self.time_line_msg.setText(QCoreApplication.translate("main", u"TextLabel", None))
        self.copy_button.setText(QCoreApplication.translate("main", u"Start Copy", None))
        self.copy_button.setProperty("styleClass", "")
        self.check_time_btn.setText(QCoreApplication.translate("main", u"check time sync", None))
        self.check_time_btn.setProperty("styleClass", "")
        self.btn_update_train.setText(QCoreApplication.translate("main", u"Update Train", None))
        self.btn_update_train.setProperty("styleClass", "")
        self.copy_log_lbl.setText(QCoreApplication.translate("main", u"message", None))
        self.copy_log_lbl.setProperty("styleClass", QCoreApplication.translate("main", u"msgStyle", None))
        self.btn_found_errors.setText("")
        self.lbl_ip_error.setText("")
        self.completed_copy_lbl.setText(QCoreApplication.translate("main", u"-", None))
        self.label_9.setText(QCoreApplication.translate("main", u"/", None))
        self.total_copy_lbl.setText(QCoreApplication.translate("main", u"-", None))
        self.total_copy_lbl_2.setText(QCoreApplication.translate("main", u"MB", None))
        self.copy_speed_lbl.setText(QCoreApplication.translate("main", u"Speed", None))
        self.label_4.setText(QCoreApplication.translate("main", u"Profile Name :", None))
        self.label_67.setText(QCoreApplication.translate("main", u"Compression:", None))
        self.label_89.setText(QCoreApplication.translate("main", u" Motion :", None))
        self.group_camera_1.setTitle(QCoreApplication.translate("main", u"Camera 1", None))
        self.label_33.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_39.setText(QCoreApplication.translate("main", u"Name", None))
        self.label_35.setText(QCoreApplication.translate("main", u"Port:", None))
        self.line_name_camera_1.setText("")
        self.label_40.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_41.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_2.setTitle(QCoreApplication.translate("main", u"Camera 2", None))
        self.label_43.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_44.setText(QCoreApplication.translate("main", u"Port:", None))
        self.line_name_camera_2.setText("")
        self.label_42.setText(QCoreApplication.translate("main", u"Name", None))
        self.label_45.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_46.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_3.setTitle(QCoreApplication.translate("main", u"Camera 3", None))
        self.label_48.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.line_name_camera_3.setText("")
        self.label_47.setText(QCoreApplication.translate("main", u"Name", None))
        self.label_49.setText(QCoreApplication.translate("main", u"Port:", None))
        self.label_50.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_63.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_4.setTitle(QCoreApplication.translate("main", u"Camera 4", None))
        self.line_name_camera_4.setText("")
        self.label_86.setText(QCoreApplication.translate("main", u"Port:", None))
        self.label_64.setText(QCoreApplication.translate("main", u"Name", None))
        self.label_85.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_87.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_88.setText(QCoreApplication.translate("main", u"Password :", None))
        self.label_profile_message.setText("")
        self.btn_save_profile.setText(QCoreApplication.translate("main", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main", u"Create New Profile", None))
        self.label_11.setText(QCoreApplication.translate("main", u"Profile Name :", None))
        self.btn_refresh_profile_name.setText("")
        self.btn_edit_profile.setText("")
        self.btn_delete_profile.setText("")
        self.label_111.setText(QCoreApplication.translate("main", u"train_id", None))
        self.label_68.setText(QCoreApplication.translate("main", u"Compression:", None))
        self.label_90.setText(QCoreApplication.translate("main", u"Motion :", None))
        self.group_camera_1_edit.setTitle(QCoreApplication.translate("main", u"Camera 1", None))
        self.label_70.setText(QCoreApplication.translate("main", u"Port:", None))
        self.label_69.setText(QCoreApplication.translate("main", u"Name :", None))
        self.line_name_camera_1_edit.setText("")
        self.label_51.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_71.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_72.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_2_edit.setTitle(QCoreApplication.translate("main", u"Camera 2", None))
        self.line_name_camera_2_edit.setText("")
        self.label_52.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_73.setText(QCoreApplication.translate("main", u"Name :", None))
        self.label_74.setText(QCoreApplication.translate("main", u"Port:", None))
        self.label_75.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_76.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_3_edit.setTitle(QCoreApplication.translate("main", u"Camera 3", None))
        self.line_name_camera_3_edit.setText("")
        self.label_61.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_78.setText(QCoreApplication.translate("main", u"Port:", None))
        self.label_77.setText(QCoreApplication.translate("main", u"Name :", None))
        self.label_79.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_80.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_4_edit.setTitle(QCoreApplication.translate("main", u"Camera 4", None))
        self.label_81.setText(QCoreApplication.translate("main", u"Name :", None))
        self.line_name_camera_4_edit.setText("")
        self.label_62.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_82.setText(QCoreApplication.translate("main", u"Port:", None))
        self.label_83.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_84.setText(QCoreApplication.translate("main", u"Password :", None))
        self.label_profile_edit_message.setText("")
        self.btn_save_edit_profile.setText(QCoreApplication.translate("main", u"Save", None))
        self.btn_cancel_edit_profile.setText(QCoreApplication.translate("main", u"Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("main", u"Edit / Delete", None))
        self.groupBox.setTitle(QCoreApplication.translate("main", u"Send", None))
        self.label_12.setText(QCoreApplication.translate("main", u"Profile Name :", None))
        self.label_13.setText(QCoreApplication.translate("main", u"Train Name :", None))
        self.send_config_msg.setText(QCoreApplication.translate("main", u"message", None))
        self.send_config_msg.setProperty("styleClass", QCoreApplication.translate("main", u"msgStyle", None))
        self.btn_send_profile.setText(QCoreApplication.translate("main", u"Send", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("main", u"Load", None))
        self.label_29.setText(QCoreApplication.translate("main", u"Train Name :", None))
        self.label_5.setText(QCoreApplication.translate("main", u"Ip : ", None))
        self.load_config_msg.setText(QCoreApplication.translate("main", u"message", None))
        self.load_config_msg.setProperty("styleClass", QCoreApplication.translate("main", u"msgStyle", None))
        self.btn_load_profile.setText(QCoreApplication.translate("main", u"Connect & Load", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("main", u"Load / Send", None))
        self.label_56.setText(QCoreApplication.translate("main", u"Train Name :", None))
        self.label_53.setText(QCoreApplication.translate("main", u"Ip Adrress :", None))
        self.label_54.setText(QCoreApplication.translate("main", u"UserName :", None))
        self.label_55.setText(QCoreApplication.translate("main", u"Password :", None))
        self.btn_save_train.setText(QCoreApplication.translate("main", u"Save", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("main", u"Create New Thin Client", None))
        self.label_57.setText(QCoreApplication.translate("main", u"Train Name :", None))
        self.btn_refresh_name_config_edit.setText("")
        self.btn_edit_config.setText("")
        self.btn_delete_config.setText("")
        self.label_60.setText(QCoreApplication.translate("main", u"Ip Adrress :", None))
        self.label_58.setText(QCoreApplication.translate("main", u"UserName :", None))
        self.label_59.setText(QCoreApplication.translate("main", u"Password :", None))
        self.btn_save_config_edit.setText(QCoreApplication.translate("main", u"Save", None))
        self.btn_cancel_config_edit.setText(QCoreApplication.translate("main", u"Cancel", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("main", u"Edit / Delete", None))
        self.label_3.setText(QCoreApplication.translate("main", u"Change Password :", None))
        self.btn_change_password.setText(QCoreApplication.translate("main", u"Click Here", None))
        self.label_14.setText(QCoreApplication.translate("main", u"Local Update :", None))
        self.btn_local_update.setText(QCoreApplication.translate("main", u"Click Here", None))
        self.label_15.setText(QCoreApplication.translate("main", u"Current/Mother Password :", None))
        self.label_16.setText(QCoreApplication.translate("main", u"New Password :", None))
        self.label_22.setText(QCoreApplication.translate("main", u"Confirm Password :", None))
        self.btn_save_password.setText(QCoreApplication.translate("main", u"Save", None))
        self.label_18.setText(QCoreApplication.translate("main", u"Storage Manager :", None))
        self.btn_storage_manager.setText(QCoreApplication.translate("main", u"Click Here", None))
        self.label_21.setText(QCoreApplication.translate("main", u"Minimum Allowed :", None))
        self.label_23.setText(QCoreApplication.translate("main", u"%", None))
        self.label_20.setText(QCoreApplication.translate("main", u"Maximum Allowed :", None))
        self.label_24.setText(QCoreApplication.translate("main", u"%", None))
        self.btn_save_storage.setText(QCoreApplication.translate("main", u"Save", None))
        self.label_message_change_password.setText("")
        self.label_19.setText(QCoreApplication.translate("main", u"Storage : ", None))
    # retranslateUi

