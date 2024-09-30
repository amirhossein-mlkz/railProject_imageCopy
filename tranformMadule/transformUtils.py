from persiantools.jdatetime import JalaliDateTime, timedelta

class transormUtils:

    @staticmethod
    def extract_file_name_info(name:str) -> tuple[JalaliDateTime, str, str]:
        date, clock, train_id, camera_name = name.split('_')
        dc_str = date + '_' + clock
        dt = JalaliDateTime.strptime(dc_str,'%Y-%m-%d_%H-%M-%S-%f')
        return dt, train_id, camera_name

    @staticmethod
    def last_day_of_month(year, month):
        if month == 12:
            next_month = JalaliDateTime(year+1, 1, 1)
        else:
            next_month = JalaliDateTime(year, month+1, 1)
        last_day_of_month:JalaliDateTime = next_month - timedelta(days=1)
        return last_day_of_month.day
