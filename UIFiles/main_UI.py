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
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)

from uiUtils.GUIComponents import timeSpinBox
import assets_rc

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.setEnabled(True)
        main.resize(617, 710)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        main.setMinimumSize(QSize(0, 0))
        main.setMaximumSize(QSize(617, 16777215))
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
"	background-color:#FF6500;\n"
"}\n"
"\n"
"*[styleSheet=\"LsideFrameStyle\"]  .QPushButton{\n"
"	border: 0px;\n"
"	color: white;\n"
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
"	background-color:#FF6500;\n"
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
"*[styleSheet=\"LpagesFrameStyle\"] .QWidg"
                        "et\n"
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
"}\n"
""
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
"	bor"
                        "der:none;\n"
"}\n"
"\n"
"\n"
"QPushButton[styleSheet=\"calendar\"]{\n"
"background:transparent;\n"
"icon:url(:/asstets/icons/calendar.png);\n"
"border:none;\n"
"icon-size:25px;\n"
"width:25px;\n"
"height:25px;\n"
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
"    image: url(:/asstets/icons/down_icon_black.png); /* Adjust the path to you"
                        "r arrow icon */\n"
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
"QGroupBox {"
                        "\n"
"    background-color: #F7F8FA;  /* Background color inside the group box */\n"
"    border: 1px solid #D7D7D9;  /* Border around the group box */\n"
"    border-radius: 5px;         /* Slight rounded corners */\n"
"    margin-top: 20px;           /* Space between title and top edge */\n"
"    padding: 10px;              /* Padding inside the group box */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;  /* Position title over the border */\n"
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
"    border: 1px soli"
                        "d #D7D7D9;  /* Same border when disabled */\n"
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
        self.leftSideFrame.setMinimumSize(QSize(0, 0))
        self.leftSideFrame.setMaximumSize(QSize(120, 16777211))
        self.leftSideFrame.setStyleSheet(u"LsideFrameStyle")
        self.leftSideFrame.setFrameShape(QFrame.StyledPanel)
        self.leftSideFrame.setFrameShadow(QFrame.Plain)
        self.leftSideFrame.setLineWidth(1)
        self.verticalLayout_67 = QVBoxLayout(self.leftSideFrame)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.leftSideFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 87))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dorsa_lbl = QLabel(self.frame_3)
        self.dorsa_lbl.setObjectName(u"dorsa_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dorsa_lbl.sizePolicy().hasHeightForWidth())
        self.dorsa_lbl.setSizePolicy(sizePolicy2)
        self.dorsa_lbl.setMinimumSize(QSize(90, 45))
        self.dorsa_lbl.setMaximumSize(QSize(75, 65))
        self.dorsa_lbl.setPixmap(QPixmap(u":/asstets/icons/2.png"))
        self.dorsa_lbl.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.dorsa_lbl)


        self.verticalLayout_67.addWidget(self.frame_3)

        self.verticalSpacer_6 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_67.addItem(self.verticalSpacer_6)

        self.line_5 = QFrame(self.leftSideFrame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_5)

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
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_4)

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

        self.line_6 = QFrame(self.leftSideFrame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_6)

        self.side_train_config_btn = QPushButton(self.leftSideFrame)
        self.side_train_config_btn.setObjectName(u"side_train_config_btn")
        sizePolicy3.setHeightForWidth(self.side_train_config_btn.sizePolicy().hasHeightForWidth())
        self.side_train_config_btn.setSizePolicy(sizePolicy3)
        self.side_train_config_btn.setMinimumSize(QSize(0, 50))
        self.side_train_config_btn.setMaximumSize(QSize(16777215, 50))
        self.side_train_config_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_train_config_btn.setIcon(icon1)
        self.side_train_config_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_67.addWidget(self.side_train_config_btn)

        self.line_7 = QFrame(self.leftSideFrame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_7)

        self.side_setting_btn = QPushButton(self.leftSideFrame)
        self.side_setting_btn.setObjectName(u"side_setting_btn")
        sizePolicy3.setHeightForWidth(self.side_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_setting_btn.setSizePolicy(sizePolicy3)
        self.side_setting_btn.setMinimumSize(QSize(0, 50))
        self.side_setting_btn.setMaximumSize(QSize(16777215, 50))
        self.side_setting_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_setting_btn.setIcon(icon1)
        self.side_setting_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_67.addWidget(self.side_setting_btn)

        self.line_2 = QFrame(self.leftSideFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_2)

        self.side_about_btn = QPushButton(self.leftSideFrame)
        self.side_about_btn.setObjectName(u"side_about_btn")
        self.side_about_btn.setEnabled(False)
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

        self.line_8 = QFrame(self.leftSideFrame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_67.addWidget(self.line_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_67.addItem(self.verticalSpacer_2)

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

        self.verticalLayout_67.setStretch(5, 10)
        self.verticalLayout_67.setStretch(11, 10)

        self.horizontalLayout_2.addWidget(self.leftSideFrame)

        self.frame = QFrame(self.localStyleSheet)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
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
        icon4 = QIcon()
        icon4.addFile(u"assets/icons/help_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.help_btn.setIcon(icon4)
        self.help_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout_14.addWidget(self.help_btn)

        self.minimize_btn = QPushButton(self.topFrame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy3.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy3)
        self.minimize_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/asstets/icons/minus_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon5)
        self.minimize_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.topFrame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy3.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy3)
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
        self.frame_56 = QFrame(self.copy)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
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


        self.verticalLayout_2.addWidget(self.frame_56)

        self.line_9 = QFrame(self.copy)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_9)

        self.frame_58 = QFrame(self.copy)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setEnabled(False)
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_58)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(34, 0, 42, 0)
        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
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

        self.ip_address_msg = QLabel(self.frame_60)
        self.ip_address_msg.setObjectName(u"ip_address_msg")

        self.verticalLayout_33.addWidget(self.ip_address_msg)


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

        self.username_msg = QLabel(self.frame_61)
        self.username_msg.setObjectName(u"username_msg")

        self.verticalLayout_34.addWidget(self.username_msg)


        self.verticalLayout_35.addWidget(self.frame_61)

        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        sizePolicy4.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy4)
        self.frame_59.setMinimumSize(QSize(0, 0))
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_17 = QVBoxLayout(self.frame_59)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, -1, -1, -1)
        self.label_21 = QLabel(self.frame_59)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_56.addWidget(self.label_21)

        self.password_input = QLineEdit(self.frame_59)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setReadOnly(True)

        self.horizontalLayout_56.addWidget(self.password_input)


        self.verticalLayout_17.addLayout(self.horizontalLayout_56)

        self.password_msg = QLabel(self.frame_59)
        self.password_msg.setObjectName(u"password_msg")

        self.verticalLayout_17.addWidget(self.password_msg)


        self.verticalLayout_35.addWidget(self.frame_59)


        self.verticalLayout_2.addWidget(self.frame_58)

        self.line_10 = QFrame(self.copy)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_10)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.timeline_groupbox = QGroupBox(self.copy)
        self.timeline_groupbox.setObjectName(u"timeline_groupbox")
        self.timeline_groupbox.setMinimumSize(QSize(0, 160))
        self.timeline_groupbox.setCheckable(True)
        self.verticalLayout_19 = QVBoxLayout(self.timeline_groupbox)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, -1, 0, -1)
        self.frame_7 = QFrame(self.timeline_groupbox)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 120))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_20 = QVBoxLayout(self.frame_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, -1, 0, -1)
        self.frame_date_2 = QFrame(self.frame_7)
        self.frame_date_2.setObjectName(u"frame_date_2")
        self.frame_date_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_date_2.setFrameShape(QFrame.NoFrame)
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

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.horizontalSpacer_7 = QSpacerItem(38, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

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

        self.horizontalSpacer_8 = QSpacerItem(38, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

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

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.verticalLayout_2.addWidget(self.copy_button, 0, Qt.AlignHCenter)

        self.line_21 = QFrame(self.copy)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_21)

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

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        self.frame_21 = QFrame(self.tab)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 509))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_13 = QVBoxLayout(self.frame_21)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.group_camera_1 = QGroupBox(self.frame_21)
        self.group_camera_1.setObjectName(u"group_camera_1")
        self.group_camera_1.setMaximumSize(QSize(16777215, 156))
        self.group_camera_1.setCheckable(True)
        self.group_camera_1.setChecked(False)
        self.verticalLayout_10 = QVBoxLayout(self.group_camera_1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.group_camera_1)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_22)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_22.addWidget(self.label_33)

        self.line_name_camera_1 = QLineEdit(self.frame_22)
        self.line_name_camera_1.setObjectName(u"line_name_camera_1")
        self.line_name_camera_1.setMaximumSize(QSize(174, 16777215))

        self.horizontalLayout_22.addWidget(self.line_name_camera_1)

        self.label_18 = QLabel(self.frame_22)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_22.addWidget(self.label_18)

        self.line_ip_camera_1 = QLineEdit(self.frame_22)
        self.line_ip_camera_1.setObjectName(u"line_ip_camera_1")

        self.horizontalLayout_22.addWidget(self.line_ip_camera_1)


        self.verticalLayout_10.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.group_camera_1)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_23)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_23.addWidget(self.label_19)

        self.line_username_camera_1 = QLineEdit(self.frame_23)
        self.line_username_camera_1.setObjectName(u"line_username_camera_1")

        self.horizontalLayout_23.addWidget(self.line_username_camera_1)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_24)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_24.addWidget(self.label_20)

        self.line_password_camera_1 = QLineEdit(self.frame_24)
        self.line_password_camera_1.setObjectName(u"line_password_camera_1")

        self.horizontalLayout_24.addWidget(self.line_password_camera_1)


        self.horizontalLayout_23.addWidget(self.frame_24)


        self.verticalLayout_10.addWidget(self.frame_23)


        self.verticalLayout_13.addWidget(self.group_camera_1)

        self.line_12 = QFrame(self.frame_21)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_12)

        self.group_camera_2 = QGroupBox(self.frame_21)
        self.group_camera_2.setObjectName(u"group_camera_2")
        self.group_camera_2.setEnabled(True)
        self.group_camera_2.setCheckable(True)
        self.group_camera_2.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.group_camera_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.group_camera_2)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_27)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_27.addWidget(self.label_35)

        self.line_name_camera_2 = QLineEdit(self.frame_27)
        self.line_name_camera_2.setObjectName(u"line_name_camera_2")
        self.line_name_camera_2.setMaximumSize(QSize(174, 16777215))

        self.horizontalLayout_27.addWidget(self.line_name_camera_2)

        self.label_23 = QLabel(self.frame_27)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_27.addWidget(self.label_23)

        self.line_ip_camera_2 = QLineEdit(self.frame_27)
        self.line_ip_camera_2.setObjectName(u"line_ip_camera_2")

        self.horizontalLayout_27.addWidget(self.line_ip_camera_2)


        self.verticalLayout_12.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.group_camera_2)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_28)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_28.addWidget(self.label_24)

        self.line_username_camera_2 = QLineEdit(self.frame_28)
        self.line_username_camera_2.setObjectName(u"line_username_camera_2")

        self.horizontalLayout_28.addWidget(self.line_username_camera_2)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_29)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_29.addWidget(self.label_25)

        self.line_password_camera_2 = QLineEdit(self.frame_29)
        self.line_password_camera_2.setObjectName(u"line_password_camera_2")

        self.horizontalLayout_29.addWidget(self.line_password_camera_2)


        self.horizontalLayout_28.addWidget(self.frame_29)


        self.verticalLayout_12.addWidget(self.frame_28)


        self.verticalLayout_13.addWidget(self.group_camera_2)

        self.line_13 = QFrame(self.frame_21)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_13)

        self.group_camera_3 = QGroupBox(self.frame_21)
        self.group_camera_3.setObjectName(u"group_camera_3")
        self.group_camera_3.setEnabled(True)
        self.group_camera_3.setCheckable(True)
        self.group_camera_3.setChecked(False)
        self.verticalLayout_15 = QVBoxLayout(self.group_camera_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.group_camera_3)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.frame_30)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_30.addWidget(self.label_63)

        self.line_name_camera_3 = QLineEdit(self.frame_30)
        self.line_name_camera_3.setObjectName(u"line_name_camera_3")
        self.line_name_camera_3.setMaximumSize(QSize(174, 16777215))

        self.horizontalLayout_30.addWidget(self.line_name_camera_3)

        self.label_26 = QLabel(self.frame_30)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_30.addWidget(self.label_26)

        self.line_ip_camera_3 = QLineEdit(self.frame_30)
        self.line_ip_camera_3.setObjectName(u"line_ip_camera_3")

        self.horizontalLayout_30.addWidget(self.line_ip_camera_3)


        self.verticalLayout_15.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.group_camera_3)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_31)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_31.addWidget(self.label_27)

        self.line_username_camera_3 = QLineEdit(self.frame_31)
        self.line_username_camera_3.setObjectName(u"line_username_camera_3")

        self.horizontalLayout_31.addWidget(self.line_username_camera_3)

        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_32)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_32.addWidget(self.label_28)

        self.line_password_camera_3 = QLineEdit(self.frame_32)
        self.line_password_camera_3.setObjectName(u"line_password_camera_3")

        self.horizontalLayout_32.addWidget(self.line_password_camera_3)


        self.horizontalLayout_31.addWidget(self.frame_32)


        self.verticalLayout_15.addWidget(self.frame_31)


        self.verticalLayout_13.addWidget(self.group_camera_3)

        self.line_14 = QFrame(self.frame_21)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_14)

        self.group_camera_4 = QGroupBox(self.frame_21)
        self.group_camera_4.setObjectName(u"group_camera_4")
        self.group_camera_4.setEnabled(True)
        self.group_camera_4.setCheckable(True)
        self.group_camera_4.setChecked(False)
        self.verticalLayout_24 = QVBoxLayout(self.group_camera_4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.group_camera_4)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.frame_38)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_37.addWidget(self.label_64)

        self.line_name_camera_4 = QLineEdit(self.frame_38)
        self.line_name_camera_4.setObjectName(u"line_name_camera_4")
        self.line_name_camera_4.setMaximumSize(QSize(174, 16777215))

        self.horizontalLayout_37.addWidget(self.line_name_camera_4)

        self.label_36 = QLabel(self.frame_38)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_37.addWidget(self.label_36)

        self.line_ip_camera_4 = QLineEdit(self.frame_38)
        self.line_ip_camera_4.setObjectName(u"line_ip_camera_4")

        self.horizontalLayout_37.addWidget(self.line_ip_camera_4)


        self.verticalLayout_24.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.group_camera_4)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_39)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_38.addWidget(self.label_37)

        self.line_username_camera_4 = QLineEdit(self.frame_39)
        self.line_username_camera_4.setObjectName(u"line_username_camera_4")

        self.horizontalLayout_38.addWidget(self.line_username_camera_4)

        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_40)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_39.addWidget(self.label_38)

        self.line_password_camera_4 = QLineEdit(self.frame_40)
        self.line_password_camera_4.setObjectName(u"line_password_camera_4")

        self.horizontalLayout_39.addWidget(self.line_password_camera_4)


        self.horizontalLayout_38.addWidget(self.frame_40)


        self.verticalLayout_24.addWidget(self.frame_39)


        self.verticalLayout_13.addWidget(self.group_camera_4)

        self.line_15 = QFrame(self.frame_21)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_15)

        self.frame_10 = QFrame(self.frame_21)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 30))
        self.frame_10.setMaximumSize(QSize(16777215, 30))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
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


        self.verticalLayout_13.addWidget(self.frame_10)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_9)

        self.line_16 = QFrame(self.frame_21)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_16)


        self.verticalLayout_14.addWidget(self.frame_21)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.label_profile_message = QLabel(self.tab)
        self.label_profile_message.setObjectName(u"label_profile_message")
        self.label_profile_message.setMaximumSize(QSize(16777215, 23))

        self.verticalLayout_14.addWidget(self.label_profile_message)

        self.frame_34 = QFrame(self.tab)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_10)

        self.btn_save_profile = QPushButton(self.frame_34)
        self.btn_save_profile.setObjectName(u"btn_save_profile")
        self.btn_save_profile.setMinimumSize(QSize(95, 0))
        self.btn_save_profile.setMaximumSize(QSize(95, 16777215))
        self.btn_save_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_profile.setIconSize(QSize(29, 23))

        self.horizontalLayout_33.addWidget(self.btn_save_profile)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_11)


        self.verticalLayout_14.addWidget(self.frame_34)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_12 = QFrame(self.tab_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 30))
        self.frame_12.setMaximumSize(QSize(16777215, 30))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Plain)
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

        self.frame_profile_edit = QFrame(self.tab_2)
        self.frame_profile_edit.setObjectName(u"frame_profile_edit")
        self.frame_profile_edit.setMaximumSize(QSize(16777215, 490))
        self.frame_profile_edit.setFrameShape(QFrame.StyledPanel)
        self.frame_profile_edit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_profile_edit)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.group_camera_1_edit = QGroupBox(self.frame_profile_edit)
        self.group_camera_1_edit.setObjectName(u"group_camera_1_edit")
        self.group_camera_1_edit.setEnabled(True)
        self.group_camera_1_edit.setMaximumSize(QSize(16777215, 145))
        self.group_camera_1_edit.setCheckable(True)
        self.group_camera_1_edit.setChecked(False)
        self.verticalLayout_25 = QVBoxLayout(self.group_camera_1_edit)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.group_camera_1_edit)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.frame_41)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_40.addWidget(self.label_51)

        self.line_name_camera_1_edit = QLineEdit(self.frame_41)
        self.line_name_camera_1_edit.setObjectName(u"line_name_camera_1_edit")
        self.line_name_camera_1_edit.setMinimumSize(QSize(102, 27))
        self.line_name_camera_1_edit.setMaximumSize(QSize(177, 16777215))

        self.horizontalLayout_40.addWidget(self.line_name_camera_1_edit)

        self.label_39 = QLabel(self.frame_41)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_40.addWidget(self.label_39)

        self.line_ip_camera_1_edit = QLineEdit(self.frame_41)
        self.line_ip_camera_1_edit.setObjectName(u"line_ip_camera_1_edit")

        self.horizontalLayout_40.addWidget(self.line_ip_camera_1_edit)


        self.verticalLayout_25.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.group_camera_1_edit)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_42)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_41.addWidget(self.label_40)

        self.line_username_camera_1_edit = QLineEdit(self.frame_42)
        self.line_username_camera_1_edit.setObjectName(u"line_username_camera_1_edit")

        self.horizontalLayout_41.addWidget(self.line_username_camera_1_edit)

        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_43)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_42.addWidget(self.label_41)

        self.line_password_camera_1_edit = QLineEdit(self.frame_43)
        self.line_password_camera_1_edit.setObjectName(u"line_password_camera_1_edit")

        self.horizontalLayout_42.addWidget(self.line_password_camera_1_edit)


        self.horizontalLayout_41.addWidget(self.frame_43)


        self.verticalLayout_25.addWidget(self.frame_42)


        self.verticalLayout_6.addWidget(self.group_camera_1_edit)

        self.group_camera_2_edit = QGroupBox(self.frame_profile_edit)
        self.group_camera_2_edit.setObjectName(u"group_camera_2_edit")
        self.group_camera_2_edit.setEnabled(True)
        self.group_camera_2_edit.setCheckable(True)
        self.group_camera_2_edit.setChecked(False)
        self.verticalLayout_26 = QVBoxLayout(self.group_camera_2_edit)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.group_camera_2_edit)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_44)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_43.addWidget(self.label_52)

        self.line_name_camera_2_edit = QLineEdit(self.frame_44)
        self.line_name_camera_2_edit.setObjectName(u"line_name_camera_2_edit")
        self.line_name_camera_2_edit.setMaximumSize(QSize(177, 16777215))

        self.horizontalLayout_43.addWidget(self.line_name_camera_2_edit)

        self.label_42 = QLabel(self.frame_44)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_43.addWidget(self.label_42)

        self.line_ip_camera_2_edit = QLineEdit(self.frame_44)
        self.line_ip_camera_2_edit.setObjectName(u"line_ip_camera_2_edit")

        self.horizontalLayout_43.addWidget(self.line_ip_camera_2_edit)


        self.verticalLayout_26.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.group_camera_2_edit)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_45)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_44.addWidget(self.label_43)

        self.line_username_camera_2_edit = QLineEdit(self.frame_45)
        self.line_username_camera_2_edit.setObjectName(u"line_username_camera_2_edit")

        self.horizontalLayout_44.addWidget(self.line_username_camera_2_edit)

        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_46)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_45.addWidget(self.label_44)

        self.line_password_camera_2_edit = QLineEdit(self.frame_46)
        self.line_password_camera_2_edit.setObjectName(u"line_password_camera_2_edit")

        self.horizontalLayout_45.addWidget(self.line_password_camera_2_edit)


        self.horizontalLayout_44.addWidget(self.frame_46)


        self.verticalLayout_26.addWidget(self.frame_45)


        self.verticalLayout_6.addWidget(self.group_camera_2_edit)

        self.group_camera_3_edit = QGroupBox(self.frame_profile_edit)
        self.group_camera_3_edit.setObjectName(u"group_camera_3_edit")
        self.group_camera_3_edit.setEnabled(True)
        self.group_camera_3_edit.setCheckable(True)
        self.group_camera_3_edit.setChecked(False)
        self.verticalLayout_27 = QVBoxLayout(self.group_camera_3_edit)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.group_camera_3_edit)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.frame_47)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_46.addWidget(self.label_61)

        self.line_name_camera_3_edit = QLineEdit(self.frame_47)
        self.line_name_camera_3_edit.setObjectName(u"line_name_camera_3_edit")
        self.line_name_camera_3_edit.setMaximumSize(QSize(177, 16777215))

        self.horizontalLayout_46.addWidget(self.line_name_camera_3_edit)

        self.label_45 = QLabel(self.frame_47)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_46.addWidget(self.label_45)

        self.line_ip_camera_3_edit = QLineEdit(self.frame_47)
        self.line_ip_camera_3_edit.setObjectName(u"line_ip_camera_3_edit")

        self.horizontalLayout_46.addWidget(self.line_ip_camera_3_edit)


        self.verticalLayout_27.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.group_camera_3_edit)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_48)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_47.addWidget(self.label_46)

        self.line_username_camera_3_edit = QLineEdit(self.frame_48)
        self.line_username_camera_3_edit.setObjectName(u"line_username_camera_3_edit")

        self.horizontalLayout_47.addWidget(self.line_username_camera_3_edit)

        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_49)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_48.addWidget(self.label_47)

        self.line_password_camera_3_edit = QLineEdit(self.frame_49)
        self.line_password_camera_3_edit.setObjectName(u"line_password_camera_3_edit")

        self.horizontalLayout_48.addWidget(self.line_password_camera_3_edit)


        self.horizontalLayout_47.addWidget(self.frame_49)


        self.verticalLayout_27.addWidget(self.frame_48)


        self.verticalLayout_6.addWidget(self.group_camera_3_edit)

        self.group_camera_4_edit = QGroupBox(self.frame_profile_edit)
        self.group_camera_4_edit.setObjectName(u"group_camera_4_edit")
        self.group_camera_4_edit.setEnabled(True)
        self.group_camera_4_edit.setCheckable(True)
        self.group_camera_4_edit.setChecked(False)
        self.verticalLayout_28 = QVBoxLayout(self.group_camera_4_edit)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.group_camera_4_edit)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.frame_50)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_49.addWidget(self.label_62)

        self.line_name_camera_4_edit = QLineEdit(self.frame_50)
        self.line_name_camera_4_edit.setObjectName(u"line_name_camera_4_edit")
        self.line_name_camera_4_edit.setMaximumSize(QSize(177, 16777215))

        self.horizontalLayout_49.addWidget(self.line_name_camera_4_edit)

        self.label_48 = QLabel(self.frame_50)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_49.addWidget(self.label_48)

        self.line_ip_camera_4_edit = QLineEdit(self.frame_50)
        self.line_ip_camera_4_edit.setObjectName(u"line_ip_camera_4_edit")

        self.horizontalLayout_49.addWidget(self.line_ip_camera_4_edit)


        self.verticalLayout_28.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.group_camera_4_edit)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_51)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_50.addWidget(self.label_49)

        self.line_username_camera_4_edit = QLineEdit(self.frame_51)
        self.line_username_camera_4_edit.setObjectName(u"line_username_camera_4_edit")

        self.horizontalLayout_50.addWidget(self.line_username_camera_4_edit)

        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_52)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_51.addWidget(self.label_50)

        self.line_password_camera_4_edit = QLineEdit(self.frame_52)
        self.line_password_camera_4_edit.setObjectName(u"line_password_camera_4_edit")

        self.horizontalLayout_51.addWidget(self.line_password_camera_4_edit)


        self.horizontalLayout_50.addWidget(self.frame_52)


        self.verticalLayout_28.addWidget(self.frame_51)


        self.verticalLayout_6.addWidget(self.group_camera_4_edit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.btn_save_edit_profile = QPushButton(self.frame_profile_edit)
        self.btn_save_edit_profile.setObjectName(u"btn_save_edit_profile")
        self.btn_save_edit_profile.setMinimumSize(QSize(95, 0))
        self.btn_save_edit_profile.setMaximumSize(QSize(95, 16777215))
        self.btn_save_edit_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btn_save_edit_profile, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_profile_edit)

        self.frame_13 = QFrame(self.tab_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_profile_edit_message = QLabel(self.frame_13)
        self.label_profile_edit_message.setObjectName(u"label_profile_edit_message")
        self.label_profile_edit_message.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_15.addWidget(self.label_profile_edit_message)


        self.verticalLayout_5.addWidget(self.frame_13)

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
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
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
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
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

        self.frame_14 = QFrame(self.groupBox)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 50))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btn_send_profile = QPushButton(self.frame_14)
        self.btn_send_profile.setObjectName(u"btn_send_profile")
        self.btn_send_profile.setMaximumSize(QSize(95, 16777215))
        self.btn_send_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.btn_send_profile)


        self.verticalLayout_8.addWidget(self.frame_14)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.line_3 = QFrame(self.tab_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
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
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
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
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
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

        self.frame_15 = QFrame(self.groupBox_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.btn_load_profile = QPushButton(self.frame_15)
        self.btn_load_profile.setObjectName(u"btn_load_profile")
        self.btn_load_profile.setMaximumSize(QSize(120, 16777215))
        self.btn_load_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_36.addWidget(self.btn_load_profile)


        self.verticalLayout_23.addWidget(self.frame_15)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

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
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
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
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_17)

        self.frame_6 = QFrame(self.tab_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
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
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_18)

        self.frame_8 = QFrame(self.tab_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
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
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_19)

        self.frame_9 = QFrame(self.tab_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
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
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_20)

        self.frame_54 = QFrame(self.tab_5)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_check_connection = QPushButton(self.frame_54)
        self.btn_check_connection.setObjectName(u"btn_check_connection")
        self.btn_check_connection.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.btn_check_connection)

        self.btn_save_train = QPushButton(self.frame_54)
        self.btn_save_train.setObjectName(u"btn_save_train")
        self.btn_save_train.setEnabled(True)
        self.btn_save_train.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.btn_save_train)


        self.verticalLayout_31.addWidget(self.frame_54)

        self.plainTextEdit_check_connection = QPlainTextEdit(self.tab_5)
        self.plainTextEdit_check_connection.setObjectName(u"plainTextEdit_check_connection")
        self.plainTextEdit_check_connection.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_31.addWidget(self.plainTextEdit_check_connection)

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
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
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
        self.frame_train_edit.setFrameShape(QFrame.StyledPanel)
        self.frame_train_edit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_train_edit)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_26 = QFrame(self.frame_train_edit)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
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
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
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
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
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

        self.btn_save_config_edit = QPushButton(self.frame_train_edit)
        self.btn_save_config_edit.setObjectName(u"btn_save_config_edit")
        self.btn_save_config_edit.setEnabled(False)
        self.btn_save_config_edit.setMaximumSize(QSize(16777215, 16777215))
        self.btn_save_config_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.btn_save_config_edit)


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
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
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
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_11)

        self.frame_change_password = QFrame(self.settings)
        self.frame_change_password.setObjectName(u"frame_change_password")
        self.frame_change_password.setMinimumSize(QSize(0, 180))
        self.frame_change_password.setMaximumSize(QSize(16777215, 180))
        self.frame_change_password.setFrameShape(QFrame.StyledPanel)
        self.frame_change_password.setFrameShadow(QFrame.Plain)
        self.verticalLayout_21 = QVBoxLayout(self.frame_change_password)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(30, -1, 30, -1)
        self.frame_4 = QFrame(self.frame_change_password)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(195, 0))
        self.label_15.setMaximumSize(QSize(195, 16777215))

        self.horizontalLayout_18.addWidget(self.label_15)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.line_current_password = QLineEdit(self.frame_4)
        self.line_current_password.setObjectName(u"line_current_password")
        self.line_current_password.setMinimumSize(QSize(102, 27))
        self.line_current_password.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_18.addWidget(self.line_current_password)


        self.verticalLayout_21.addWidget(self.frame_4)

        self.frame_17 = QFrame(self.frame_change_password)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_16 = QLabel(self.frame_17)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(110, 0))
        self.label_16.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_19.addWidget(self.label_16)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)

        self.line_new_password = QLineEdit(self.frame_17)
        self.line_new_password.setObjectName(u"line_new_password")
        self.line_new_password.setMinimumSize(QSize(102, 27))
        self.line_new_password.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_19.addWidget(self.line_new_password)


        self.verticalLayout_21.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_change_password)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_22 = QLabel(self.frame_18)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(110, 0))
        self.label_22.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_26.addWidget(self.label_22)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_9)

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

        self.verticalLayout_21.addWidget(self.btn_save_password, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_change_password)

        self.frame_33 = QFrame(self.settings)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_33)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_message_change_password = QLabel(self.frame_33)
        self.label_message_change_password.setObjectName(u"label_message_change_password")
        self.label_message_change_password.setMinimumSize(QSize(0, 14))

        self.verticalLayout_22.addWidget(self.label_message_change_password, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_33)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)

        self.stackedWidget.addWidget(self.settings)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.localStyleSheet)

        main.setCentralWidget(self.globalStyleSheet)

        self.retranslateUi(main)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"MainWindow", None))
        self.dorsa_lbl.setText("")
        self.side_copy_btn.setText(QCoreApplication.translate("main", u"Copy", None))
        self.side_profile_btn.setText(QCoreApplication.translate("main", u"Profile Config", None))
        self.side_train_config_btn.setText(QCoreApplication.translate("main", u"Train Config", None))
        self.side_setting_btn.setText(QCoreApplication.translate("main", u"Settings", None))
        self.side_about_btn.setText(QCoreApplication.translate("main", u" About Us ", None))
        self.login_btn.setText(QCoreApplication.translate("main", u"Login", None))
        self.login_btn.setProperty("styleClass", QCoreApplication.translate("main", u"fillBtn", None))
        self.logined_username_lbl.setText("")
        self.help_btn.setText("")
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("main", u"Train Name :", None))
        self.label_2.setText(QCoreApplication.translate("main", u"IP Address : ", None))
        self.ip_address_msg.setText(QCoreApplication.translate("main", u"message", None))
        self.ip_address_msg.setProperty("styleClass", QCoreApplication.translate("main", u"msgStyle", None))
        self.label_17.setText(QCoreApplication.translate("main", u"User Name :", None))
        self.username_msg.setText(QCoreApplication.translate("main", u"message", None))
        self.username_msg.setProperty("styleClass", QCoreApplication.translate("main", u"msgStyle", None))
        self.label_21.setText(QCoreApplication.translate("main", u"Password   :", None))
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
        self.group_camera_1.setTitle(QCoreApplication.translate("main", u"Camera 1 - Right", None))
        self.label_33.setText(QCoreApplication.translate("main", u"Name :", None))
        self.line_name_camera_1.setText(QCoreApplication.translate("main", u"Right", None))
        self.label_18.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_19.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_20.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_2.setTitle(QCoreApplication.translate("main", u"Camera 2 - Left", None))
        self.label_35.setText(QCoreApplication.translate("main", u"Username :", None))
        self.line_name_camera_2.setText(QCoreApplication.translate("main", u"Left", None))
        self.label_23.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_24.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_25.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_3.setTitle(QCoreApplication.translate("main", u"Camera 3", None))
        self.label_63.setText(QCoreApplication.translate("main", u"Name :", None))
        self.line_name_camera_3.setText(QCoreApplication.translate("main", u"Spare 3", None))
        self.label_26.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_27.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_28.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_4.setTitle(QCoreApplication.translate("main", u"Camera 4", None))
        self.label_64.setText(QCoreApplication.translate("main", u"Name :", None))
        self.line_name_camera_4.setText(QCoreApplication.translate("main", u"Spare 4", None))
        self.label_36.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_37.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_38.setText(QCoreApplication.translate("main", u"Password :", None))
        self.label_4.setText(QCoreApplication.translate("main", u"Profile Name :", None))
        self.label_profile_message.setText("")
        self.btn_save_profile.setText(QCoreApplication.translate("main", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main", u"Create New Profile", None))
        self.label_11.setText(QCoreApplication.translate("main", u"Profile Name :", None))
        self.btn_refresh_profile_name.setText("")
        self.btn_edit_profile.setText("")
        self.btn_delete_profile.setText("")
        self.group_camera_1_edit.setTitle(QCoreApplication.translate("main", u"Camera 1 - Right", None))
        self.label_51.setText(QCoreApplication.translate("main", u"Name :", None))
        self.line_name_camera_1_edit.setText("")
        self.label_39.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_40.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_41.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_2_edit.setTitle(QCoreApplication.translate("main", u"Camera 2 - Left", None))
        self.label_52.setText(QCoreApplication.translate("main", u"Name :", None))
        self.line_name_camera_2_edit.setText("")
        self.label_42.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_43.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_44.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_3_edit.setTitle(QCoreApplication.translate("main", u"Camera 3", None))
        self.label_61.setText(QCoreApplication.translate("main", u"Name :", None))
        self.line_name_camera_3_edit.setText("")
        self.label_45.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_46.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_47.setText(QCoreApplication.translate("main", u"Password :", None))
        self.group_camera_4_edit.setTitle(QCoreApplication.translate("main", u"Camera 4", None))
        self.label_62.setText(QCoreApplication.translate("main", u"Name :", None))
        self.line_name_camera_4_edit.setText("")
        self.label_48.setText(QCoreApplication.translate("main", u"Ip :", None))
        self.label_49.setText(QCoreApplication.translate("main", u"Username :", None))
        self.label_50.setText(QCoreApplication.translate("main", u"Password :", None))
        self.btn_save_edit_profile.setText(QCoreApplication.translate("main", u"Save", None))
        self.label_profile_edit_message.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("main", u"Edit / Delete", None))
        self.groupBox.setTitle(QCoreApplication.translate("main", u"Send", None))
        self.label_12.setText(QCoreApplication.translate("main", u"Profile Name :", None))
        self.label_13.setText(QCoreApplication.translate("main", u"Train Name :", None))
        self.btn_send_profile.setText(QCoreApplication.translate("main", u"Send", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("main", u"Load", None))
        self.label_29.setText(QCoreApplication.translate("main", u"Train Name :", None))
        self.label_5.setText(QCoreApplication.translate("main", u"Ip : ", None))
        self.btn_load_profile.setText(QCoreApplication.translate("main", u"Connect & Load", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("main", u"Load / Send", None))
        self.label_56.setText(QCoreApplication.translate("main", u"Train Name :", None))
        self.label_53.setText(QCoreApplication.translate("main", u"Ip Adrress :", None))
        self.label_54.setText(QCoreApplication.translate("main", u"UserName :", None))
        self.label_55.setText(QCoreApplication.translate("main", u"Password :", None))
        self.btn_check_connection.setText(QCoreApplication.translate("main", u"Check Connection", None))
        self.btn_save_train.setText(QCoreApplication.translate("main", u"Save", None))
        self.plainTextEdit_check_connection.setPlainText(QCoreApplication.translate("main", u"Check Ping ....", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("main", u"Create New Train Config", None))
        self.label_57.setText(QCoreApplication.translate("main", u"Train Name :", None))
        self.btn_refresh_name_config_edit.setText("")
        self.btn_edit_config.setText("")
        self.btn_delete_config.setText("")
        self.label_60.setText(QCoreApplication.translate("main", u"Ip Adrress :", None))
        self.label_58.setText(QCoreApplication.translate("main", u"UserName :", None))
        self.label_59.setText(QCoreApplication.translate("main", u"Password :", None))
        self.btn_save_config_edit.setText(QCoreApplication.translate("main", u"Save", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("main", u"Edit / Delete", None))
        self.label_3.setText(QCoreApplication.translate("main", u"Change Password :", None))
        self.btn_change_password.setText(QCoreApplication.translate("main", u"Click Here", None))
        self.label_15.setText(QCoreApplication.translate("main", u"Current Password/Mother Password :", None))
        self.label_16.setText(QCoreApplication.translate("main", u"New Password :", None))
        self.label_22.setText(QCoreApplication.translate("main", u"Confirm Password :", None))
        self.btn_save_password.setText(QCoreApplication.translate("main", u"Save", None))
        self.label_message_change_password.setText("")
    # retranslateUi

