import pandas as pd
from helpers.help.helpers import date_today_hour
import xlsxwriter

def structure_table(data_4excel:dict,name_excel_file:str):
    name_excel_file = f'{date_today_hour()}_{name_excel_file}'
    dados_capturados = pd.DataFrame(data=data_4excel)

    writer = pd.ExcelWriter (f'./download/generate/{name_excel_file}.xlsx', engine = 'xlsxwriter')
    dados_capturados.to_excel(writer, sheet_name='Sheet1',index=False)
    writer.save()
    return dados_capturados