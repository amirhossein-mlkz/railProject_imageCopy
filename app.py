from PySide6 import QtWidgets, QtCore, QtGui 
import sys
import os
from datetime import datetime
import ctypes
from get_admin_privilage import run_as_admin
from utils.Trial import TrialManager


sys.path.append('UIFiles\\Assets')

BUILD_UI = True

ADMIN_ACCESS = True


if BUILD_UI:
    os.system('CMD /C pyside6-rcc uiFiles/Assets/assets.qrc -o uiFiles/Assets/assets_rc.py')#PySide
    os.system('CMD /C pyside6-uic UIFiles/mainUI.ui -o UIFiles/main_UI.py')
    os.system('CMD /C pyside6-uic UIFiles/timeSyncUI.ui -o UIFiles/timeSync_UI.py')
    os.system('CMD /C pyside6-uic UIFiles/updateUI.ui -o UIFiles/updateUI.py')

    #dialogs

from mainUI import mainUI


if __name__ == '__main__':
    trial_manager = TrialManager(trial_days=30)
    # trial_manager.reset_trial()
    if trial_manager.check_trial():
        print("The software is running in trial mode.")
    else:
        print("Trial has expired. Please purchase the software.")
        sys.exit()

    #get admin provollage if any one ret False and do that work


    # Check if we are running as an admin
    if ADMIN_ACCESS:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("Not admin. Requesting access...")
            if run_as_admin():
                # Don't exit, just let the program continue to the next steps
                print("Now running as admin! Continuing execution...")
                # sys.exit(0)

            else:
                print("Failed to obtain admin privileges. Exiting.")
                sys.exit(1)
        else:
            print("Running as administrator!")






    app = QtWidgets.QApplication(sys.argv)


    app.setStyle('windows')
    
    main_ui = mainUI()
    main_ui.show()
    # api = main_API(main_ui)
    app.exec()
    