from PySide6 import QtWidgets, QtCore, QtGui 
import sys
import os
from datetime import datetime

sys.path.append('UIFiles\\Assets')

BUILD_UI = False
if BUILD_UI:
    os.system('CMD /C pyside6-rcc uiFiles/Assets/assets.qrc -o uiFiles/Assets/assets_rc.py')#PySide
    os.system('CMD /C pyside6-uic UIFiles/mainUI.ui -o UIFiles/main_UI.py')
    os.system('CMD /C pyside6-uic UIFiles/timeSyncUI.ui -o UIFiles/timeSync_UI.py')

    #dialogs

from mainUI import mainUI


if __name__ == '__main__':




    # Get the current year
    current_year = datetime.now().year

    # Check if the year is 2025
    if current_year == 2025:
        sys.exit()  # Stops the program






    app = QtWidgets.QApplication(sys.argv)
    
    main_ui = mainUI()
    main_ui.show()
    # api = main_API(main_ui)
    app.exec()
    