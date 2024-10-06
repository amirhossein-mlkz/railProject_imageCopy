from PySide6 import QtWidgets, QtCore, QtGui 
import sys
import os
BUILD_UI = True
if BUILD_UI:
    sys.path.append('UIFiles\\Assets')
    os.system('CMD /C pyside6-rcc uiFiles/Assets/assets.qrc -o uiFiles/Assets/assets_rc.py')#PySide
    os.system('CMD /C pyside6-uic UIFiles/mainUI.ui -o UIFiles/main_UI.py')
    #dialogs

from mainUI import mainUI


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    main_ui = mainUI()
    main_ui.show()
    # api = main_API(main_ui)
    app.exec()
    