from datetime import date,datetime
import zipfile
import glob





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

def unzip_files(dir_input:str,zip_file_name:str):
    """The function unzip files in dir_input and create a folder whith a zip_file_name
    :param dir_input: str the source of you need unzip file ; 
           file_name: str the name of you rename the folder in source of dir_input
    :return the source of unzip file
    :raises Nothing raises
    """
    file_upload = zipfile.ZipFile(f'.\\{dir_input}\\{zip_file_name}')
    file_upload.extractall(f'.\\{dir_input}\\unzip_{zip_file_name}')
    file_upload.close()

    dir_file = f'{dir_input}/unzip_{zip_file_name}'
    return dir_file

def read_files_folder(dir_input:str) -> str:
    """This function return all files PDF in folder
    
    Arguments:
        dir_input {str} -- path of folder
    
    Returns:
        str -- files in folder
    """    

    list_files_read = glob.glob(f'{dir_input}/*.pdf')
    files_treat_read = [files.replace('\\','/').split('/')[-1] for files in list_files_read]
    return files_treat_read