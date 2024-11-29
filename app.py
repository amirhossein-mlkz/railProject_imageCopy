from PySide6 import QtWidgets, QtCore, QtGui 
import sys
import os
from datetime import datetime
import ctypes
from get_admin_privilage import run_as_admin


sys.path.append('UIFiles\\Assets')

BUILD_UI = True

ADMIN_ACCESS = False


if BUILD_UI:
    os.system('CMD /C pyside6-rcc uiFiles/Assets/assets.qrc -o uiFiles/Assets/assets_rc.py')#PySide
    os.system('CMD /C pyside6-uic UIFiles/mainUI.ui -o UIFiles/main_UI.py')
    os.system('CMD /C pyside6-uic UIFiles/timeSyncUI.ui -o UIFiles/timeSync_UI.py')
    os.system('CMD /C pyside6-uic UIFiles/updateUI.ui -o UIFiles/updateUI.py')

    #dialogs

from mainUI import mainUI


if __name__ == '__main__':




    # Get the current year
    current_year = datetime.now().year

    # Check if the year is 2025
    if current_year == 2025:
        sys.exit()  # Stops the program


    fiewall_status = False

    folder_share_status = False
    


    #check_firewall_disable


    #check_folder_share



    #get admin provollage if any one ret False and do that work


    # Check if we are running as an admin
    if ADMIN_ACCESS:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("Not admin. Requesting access...")
            if run_as_admin():
                # Don't exit, just let the program continue to the next steps
                print("Now running as admin! Continuing execution...")
                sys.exit(0)

            else:
                print("Failed to obtain admin privileges. Exiting.")
                sys.exit(1)
        else:
            print("Running as administrator!")






    app = QtWidgets.QApplication(sys.argv)


    # app.setStyle('windows')
    
    main_ui = mainUI()
    main_ui.show()
    # api = main_API(main_ui)
    app.exec()
    