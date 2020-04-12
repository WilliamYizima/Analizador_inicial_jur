from helpers.structure_pdf.read_pdf import structure_pdf
from helpers.structure_pdf.structure_table import structure_table
from helpers.filter_apply.filter_apply import filter_process,find_response
from helpers.slice_pdf4request.slice_4request import dataset_request
from helpers.response_app.reponse import reponse
from helpers.help.helpers import unzip_files,read_files_folder



#TO DO -> JOGAR PRO DOTENV
generate_folder_excel = './download/generate'
read_folder_zip = './download/upload'


def create_structe_excel(path_pdf:str,name_excel:str,regex_titulos_pedidos:list,list_regex_end_page:list):
    structure_4excel = structure_pdf(path_pdf)
    dataset = structure_table(structure_4excel,name_excel)
    response_filter = filter_process(dataset,regex_titulos_pedidos)
    response_app = find_response(response_filter)
    dataset_pedidos = dataset_request(response_app,dataset,name_excel)
    response_app = reponse(path_pdf,dataset_pedidos,dataset,list_regex_end_page)
    return response_app

def analyze_mass(file_zip_name:str,regex_titulos_pedidos:list,regex_fim_petição:list) ->list:
    dir_zip_files = unzip_files(read_folder_zip,file_zip_name)
    files_folder = read_files_folder(dir_zip_files)
    path_pdf = f'./download/upload/unzip_{file_zip_name}'
    response_mass =[]
    for files in files_folder:
        obj_files = {'name':files,'status':''}
        try:
            create_structe_excel(f'{path_pdf}/{files}',files,regex_titulos_pedidos,regex_fim_petição)
            obj_files['status']='Processado'
            response_mass.append(obj_files)
        except:
            obj_files['status']='Não foi possível Processar'
            response_mass.append(obj_files)

    return response_mass
