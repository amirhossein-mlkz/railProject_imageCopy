import os

class pathConstants:

    MANIFEST_NAME = 'manifest.json'
    SELF_SHARE_NAME = 'rail_share'


    SELF_SHARE_PATH = 'C:\\rail_share'
    SELF_IMAGES_FOLDR = 'images'
    SELF_IMAGES_DIR = os.path.join(SELF_SHARE_PATH, SELF_IMAGES_FOLDR)
    UTILS_FOLDER = 'utils'
    UTILS_DIR = os.path.join(SELF_SHARE_PATH, UTILS_FOLDER)
    SELF_LOGS_SHARE_FOLDER = os.path.join(UTILS_DIR,'logs')

    OTHER_SHARE_NAME= "rail_share"
    
    OTHER_IMAGES_SHARE_FOLDER = os.path.join(OTHER_SHARE_NAME,'images')
    #-------------------------------------------------------------------
    OTHER_UTILS_SHARE_FOLDER = os.path.join(OTHER_SHARE_NAME,'utils')


    
    OTHER_LOGS_SHARE_FOLDER = os.path.join(OTHER_UTILS_SHARE_FOLDER,'logs')
    OTHER_CONFIG_SHARE_PATH = os.path.join(OTHER_UTILS_SHARE_FOLDER,'config.json')
    OTHER_CLOCK_SHARE_PATH = os.path.join(OTHER_UTILS_SHARE_FOLDER,'clock.json')
    #-------------------------------------------------------------------

    #----------------------------------------------------------------
    SELF_UPDATES_PATH = os.path.join(SELF_SHARE_PATH,'updates')
    SELF_UPDATE_IMAGEGRABBER_PATH = os.path.join(SELF_UPDATES_PATH,'imageGrabber')
    SELF_UPDATE_IMAGEGRABBER_MANIFEST_PATH = os.path.join(SELF_UPDATE_IMAGEGRABBER_PATH,MANIFEST_NAME)
    TEMP_UPDATE_DIR = 'update'#directory of extracted of update
    #----------------------------------------------------------------
    OTHER_UPDATES_PATH = os.path.join(OTHER_SHARE_NAME,'updates')
    OTHER_UPDATE_IMAGEGRABBER_PATH = os.path.join(OTHER_UPDATES_PATH,'imageGrabber')
    OTHER_UPDATE_IMAGEGRABBER_MANIFEST_PATH = os.path.join(OTHER_UPDATE_IMAGEGRABBER_PATH,MANIFEST_NAME)

