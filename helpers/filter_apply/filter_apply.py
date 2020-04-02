import re
from helpers.filter_apply.filters import *
import pandas as pd


def find_response(respostas_filtro):
    response_return={}
    for respostas in respostas_filtro:
        if(respostas['id']!=''):
            response_return = respostas
            break
    return response_return

def filter_process(dataset,regex_titulos_pedidos):
    list_responses = []
    negrito = dataset.query('font.str.contains("Bold")')
    lista_negrito = {index_negrito for index_negrito in negrito['id']}

    upper = dataset.query('text.str.isupper()')
    lista_upper = {index_upper for index_upper in upper.id}

    vazio = dataset.query('text == " "')
    lista_vazio = {index_vazio for index_vazio in vazio.id}

    vazio_anterior_lista_utilizar = list(lista_vazio)
    vazio_anterior_lista = [negrito+1 for negrito in vazio_anterior_lista_utilizar]
    vazio_posterior_lista_utilizar = list(lista_vazio)
    vazio_posterior_lista = [negrito-1 for negrito in vazio_posterior_lista_utilizar]
    
    vazio_anterior_set = set([index_negrito for index_negrito in vazio_anterior_lista])
    vazio_posterior_set = set([index_negrito for index_negrito in vazio_posterior_lista])
    
    response_filter01 = filter01(vazio_anterior_set,lista_negrito,vazio_posterior_set,lista_upper,dataset,regex_titulos_pedidos)
    response_filter02 = filter02(vazio_anterior_set,lista_negrito,vazio_posterior_set,dataset,regex_titulos_pedidos)
    response_filter03 = filter03(lista_upper,lista_negrito,vazio_posterior_set,dataset,regex_titulos_pedidos)
    response_filter04 = filter04(lista_upper,lista_negrito,vazio_anterior_set,dataset,regex_titulos_pedidos)
    response_filter05 = filter05(lista_negrito,vazio_anterior_set,dataset,regex_titulos_pedidos)
    response_filter06 = filter06(lista_negrito,vazio_posterior_set,dataset,regex_titulos_pedidos)
    list_responses = [response_filter01,response_filter02,response_filter03,response_filter04,response_filter05,response_filter06]
    return list_responses