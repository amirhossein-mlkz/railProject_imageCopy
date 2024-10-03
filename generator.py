import os,cv2,random

from persiantools.jdatetime import JalaliDateTime

encode_param = [int(cv2.IMWRITE_JPEG_LUMA_QUALITY), 80]


MODE = 1
main_path = f'test_data{MODE}'


if MODE==1:
    os.mkdir(main_path)
    for train in ['11BGD1',]:
        path0 = os.path.join(main_path, train)
        os.mkdir(path0)
        for cam in ['cam1', 'cam2']:
            path1 = os.path.join(path0, str(cam))
            os.mkdir(path1)
            for year in range(1401,1403):
                path2 = os.path.join(path1, str(year))
                os.mkdir(path2)
                for month in range(1,8):
                    path3 = os.path.join(path2, str(month))
                    os.mkdir(path3)
                    for day in range(10,15):
                        path4 = os.path.join(path3, str(day))
                        os.mkdir(path4)
                        for hour in range(8,12):
                            path5 = os.path.join(path4, str(hour))
                            os.mkdir(path5)
                            for minute in range(3,55, 10):
                                path6 = os.path.join(path5, str(minute))
                                os.mkdir(path6)

                                date = JalaliDateTime(year, month, day, hour, minute)
                                date_str = date.strftime('%Y-%m-%d_%H-%M-%S-%f')
                                file_name = f'{date_str}_{train}_{cam}.mp4'

                                file_path = os.path.join(path6, file_name)
                                with open(file_path, 'wt') as f:
                                    f.write('salam')

                            


if MODE==2:
    os.mkdir(main_path)
    for train in ['11BGD1',]:
        path0 = os.path.join(main_path, train)
        os.mkdir(path0)
        for cam in ['cam1', 'cam2']:
            path1 = os.path.join(path0, str(cam))
            os.mkdir(path1)
            for year in range(1401,1403):
                for month in range(1,8):
                    for day in range(10,15):
                        for hour in range(8,12):
                            for minute in range(3,55, 10):

                                date = JalaliDateTime(year, month, day, hour, minute)
                                date_str = date.strftime('%Y-%m-%d_%H-%M-%S-%f')
                                file_name = f'{date_str}_{train}_{cam}.mp4'

                                file_path = os.path.join(path1, file_name)
                                with open(file_path, 'wt') as f:
                                    f.write('salam')