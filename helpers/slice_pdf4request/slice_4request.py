from helpers.pre_process.pre_process import clean_signature,remove_footer
from helpers.help.helpers import date_today_hour
import pandas as pd
import numpy as np


def dataset_request(response_app,dataset,name_excel):
    name_excel_file = f'pedido_{date_today_hour()}_{name_excel}'
    if ('id' in response_app):
        begin = response_app['id']
        end = response_app['id_anterior']
        dataset_request = dataset.iloc[begin:end]
        dataset_request_clean01=dataset_request.copy()
        # TO DO melhorar este pré processamento
        # dataset_request_clean01 = clean_signature(dataset_request) 

        # dataset_request_clean01 = remove_footer(dataset_request)
        
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

def slice_sentence(dataframe,indice:list)->list:
    # dataframe = dataframe.set_index('id')
    sentence=[]
    dataframe = dataframe.reset_index()
    for i in range(len(indice['indices'])-1):
        lista = indice['indices']
        print(len(indice['indices']))
        print(i)
        begin = lista[i]
        print(begin)
        texto = ''
        if(i==0):
            texto = dataframe.loc[:begin]['text'].values
        if(i==len(indice['indices'])-2):
            end = lista[i+1]
            texto01 = dataframe.loc[begin:end-1]['text'].values
            begin = lista[-1]
            sentence.append(' '.join(texto01))
            texto02 = dataframe.loc[begin:]['text'].values
            sentence.append(' '.join(texto02))
            print('ultimo')
        else:
            end = lista[i+1]
            print(end)
            texto = dataframe.loc[begin:end-1]['text'].values
        sentence.append(' '.join(texto))
    return sentence