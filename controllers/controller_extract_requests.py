from helpers.structure_pdf.read_pdf import structure_pdf
from helpers.structure_pdf.structure_table import structure_table
from helpers.filter_apply.filter_apply import filter_process,find_response
from helpers.slice_pdf4request.slice_4request import dataset_request
from helpers.response_app.reponse import reponse

def create_structe_excel(path_pdf:str,name_excel:str,regex_titulos_pedidos:list):
    structure_4excel = structure_pdf(path_pdf)
    dataset = structure_table(structure_4excel,name_excel)
    response_filter = filter_process(dataset,regex_titulos_pedidos)
    response_app = find_response(response_filter)
    dataset_pedidos = dataset_request(response_app,dataset,name_excel)
    response_app = reponse(path_pdf,dataset_pedidos)
    return response_app