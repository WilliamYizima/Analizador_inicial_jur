import pandas as pd

def regex_validando(regex:str,frase:str):
    import re
    regex_tratado = regex.lower()
    frase_tratado = frase.lower()
    regex_compile = re.compile(regex_tratado)
    captura = regex_compile.search(frase_tratado)
    resposta_regex = 'não encontrado'
    if captura:
        resposta_regex = str(captura.group())
    return resposta_regex

def regex_validando_lista(lista_regex:list,frase:str):
    resposta_lista_regex = 'não encontrado'
    for regex in lista_regex:
        resposta_regex = regex_validando(regex,frase)
        if (resposta_regex!='não encontrado'):
            resposta_lista_regex = resposta_regex
            break
    return resposta_lista_regex


def read_dataframe_find_regex(dados,regex_titulos_pedidos,tipo_filtro,ultimo_index):
    obj_regex = {'id':'','regex':'','id_anterior':'','tipo_validador':'','nivel_validacao':''}
    if(tipo_filtro==1):
        obj_regex['tipo_validador']='Negrito + Upper + Espaç anterior + Espaç posterior'
        obj_regex['nivel_validacao']='Muito bom'
    if(tipo_filtro==2):
        obj_regex['tipo_validador']='Negrito + Espaç anterior + Espaç posterior'
        obj_regex['nivel_validacao']='Bom'
    if(tipo_filtro==3):
        obj_regex['tipo_validador']='Negrito + Upper + Espaç posterior'
        obj_regex['nivel_validacao']='Bom'
    if(tipo_filtro==4):
        obj_regex['tipo_validador']='Negrito + Upper + Espaç anterior'
        obj_regex['nivel_validacao']='Bom'
    if(tipo_filtro==5):
        obj_regex['tipo_validador']='Negrito + Espaç anterior'
        obj_regex['nivel_validacao']='Ponto Atencao'
    if(tipo_filtro==6):
        obj_regex['tipo_validador']='Negrito + Espaç posterior'
        obj_regex['nivel_validacao']='Ponto Atencao'
    dados = dados.sort_values(['id'])
    index_controle=[]
    text_controle=[]
    for index, dado in dados.iterrows():
        index_controle.append(index)
        text_controle.append(dado['text'])
        resposta_regex = regex_validando_lista(regex_titulos_pedidos,dado['text'])
        if(obj_regex['id'] !=''):
            obj_regex['id_anterior'] = index_controle[-1]
            break
        if(resposta_regex!='não encontrado' and obj_regex['id'] ==''):
            obj_regex['id'] = index
            obj_regex['regex'] = resposta_regex
    # validações
    
    if  (obj_regex['id_anterior'] == ''):
        obj_regex['id_anterior'] = ultimo_index
    else:
        tamanho_pedido = int(obj_regex['id']) - int(obj_regex['id_anterior'])
        if(tamanho_pedido<20):
            obj_regex['id_anterior'] = ultimo_index
    return obj_regex

def filter01(negrito_anterior,lista_negrito,negrito_posterior,lista_upper,dataset,regex_titulos_pedidos):
    ultimo_index = dataset.shape[0]#Gambis para não dar pau no id_ultimo
    intersection_negrito_anterior_negrito = negrito_anterior.intersection(lista_negrito)
    intersection_negrito_posterior_negrito_anterior_negrito = intersection_negrito_anterior_negrito.intersection(negrito_posterior)
    intersection_upper_negrito_posterior_negrito_anterior_negrito = intersection_negrito_posterior_negrito_anterior_negrito.intersection(lista_upper)
    dados0 = dataset.iloc[list(intersection_upper_negrito_posterior_negrito_anterior_negrito)]
    filtro_01 = read_dataframe_find_regex(dados0,regex_titulos_pedidos,1,ultimo_index)

    return filtro_01

def filter02(negrito_anterior,lista_negrito,negrito_posterior,dataset,regex_titulos_pedidos):
    ultimo_index = dataset.shape[0]#Gambis para não dar pau no id_ultimo
    intersection_negrito_espaco_anterior = lista_negrito.intersection(negrito_anterior)
    intersection_negrito_espaco_anterior_espaco_superior = intersection_negrito_espaco_anterior.intersection(negrito_posterior)
    dados02 = dataset.iloc[list(intersection_negrito_espaco_anterior_espaco_superior)]
    filtro_02 = read_dataframe_find_regex(dados02,regex_titulos_pedidos,2,ultimo_index)
    return filtro_02

def filter03(lista_upper,lista_negrito,negrito_posterior,dataset,regex_titulos_pedidos):
    ultimo_index = dataset.shape[0]#Gambis para não dar pau no id_ultimo
    intersection_negrito_upper = lista_negrito.intersection(lista_upper)
    intersection_negrito_upper_espaco_posterior = intersection_negrito_upper.intersection(negrito_posterior)
    dados03 = dataset.iloc[list(intersection_negrito_upper_espaco_posterior)]
    filtro_03 = read_dataframe_find_regex(dados03,regex_titulos_pedidos,3,ultimo_index)
    return filtro_03

def filter04(lista_upper,lista_negrito,negrito_anterior,dataset,regex_titulos_pedidos):
    ultimo_index = dataset.shape[0]#Gambis para não dar pau no id_ultimo
    intersection_negrito_upper = lista_negrito.intersection(lista_upper)
    intersection_negrito_upper_espaco_anterior = intersection_negrito_upper.intersection(negrito_anterior)
    dados04 = dataset.iloc[list(intersection_negrito_upper_espaco_anterior)]
    filtro_04 = read_dataframe_find_regex(dados04,regex_titulos_pedidos,4,ultimo_index)
    
    return filtro_04

def filter05(lista_negrito,vazio_anterior_set,dataset,regex_titulos_pedidos): 
    ultimo_index = dataset.shape[0]#Gambis para não dar pau no id_ultimo
    intersection_negrito_espaco_anterior = lista_negrito.intersection(vazio_anterior_set)
    dados05 = dataset.iloc[list(intersection_negrito_espaco_anterior)]
    filtro_05 = read_dataframe_find_regex(dados05,regex_titulos_pedidos,5,ultimo_index)
    return filtro_05

def filter06(lista_negrito,vazio_posterior_set,dataset,regex_titulos_pedidos): 
    ultimo_index = dataset.shape[0]#Gambis para não dar pau no id_ultimo
    intersection_negrito_espaco_posterior = lista_negrito.intersection(vazio_posterior_set)
    dados06 = dataset.iloc[list(intersection_negrito_espaco_posterior)]
    filtro_06 =read_dataframe_find_regex(dados06,regex_titulos_pedidos,6,ultimo_index)
    return filtro_06
