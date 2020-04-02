from helpers.clean_signature.clean_signature import clean_signature
from helpers.help.helpers import date_today_hour
import pandas as pd


def dataset_request(response_app,dataset,name_excel):
    name_excel_file = f'pedido_{date_today_hour()}_{name_excel}'
    if ('id' in response_app):
        begin = response_app['id']
        end = response_app['id_anterior']
        dataset_request = dataset.iloc[begin:end]
        dataset_request_clean01 = clean_signature(dataset_request)

        writer = pd.ExcelWriter (f'./download/generate/{name_excel_file}.xlsx', engine = 'xlsxwriter')
        dataset_request_clean01.to_excel(writer, sheet_name='Sheet1',index=False)
        writer.save()
        # return dataset_request_clean01
        return dataset_request_clean01
    else:
        return 'não consegui processar, valide o dicionário: \n\
                routes\extract_pdf.py    \n \
                ou veja se o corte atende aos filters atuais:\n\
                helpers\\filter_apply\\filters.py'