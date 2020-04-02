from datetime import date,datetime

def date_today_hour():
    """The function return the day today and the hour
    :param  Nothing parameter
    :returns str day-month-year
    :raises Nothing raises
    """
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_Hour_%H_%M_%S")
    return dt_string

def treatament_file_name(path_file:str):
    path_file = path_file.replace('\\','/')
    path_file = path_file.split('/')
    return path_file[-1]