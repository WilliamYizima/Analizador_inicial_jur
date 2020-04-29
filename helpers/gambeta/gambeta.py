import pandas as pd

path_dict_end_petition = 'download/generate/termino_inicial/'

def bd_excel(obj_response):
    try:
        titulos = ','.join(obj_response['title'])
        path_file = f'{path_dict_end_petition}Termos_Excel.xlsx'
        dataset = pd.read_excel(path_file)
        obj_data = {'NOME_PDF':obj_response['file_name'],
                    'TERMO_REGEX':obj_response['last_page']['term_regex'],
                    'FRASE':obj_response['last_page']['end_petition'],
                    'POSSIVEIS_TITULOS':titulos}
        dataset = dataset.append(obj_data, ignore_index=True)
        dataset.to_excel(path_file,index=False)
        retorno = 'salvo'
    except:
        retorno = 'não salvo'
    return retorno
