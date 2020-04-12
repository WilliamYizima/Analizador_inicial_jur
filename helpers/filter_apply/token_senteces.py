
import re
from helpers.slice_pdf4request.slice_4request import slice_sentence,token_last_page
from helpers.filter_apply.filters import regex_validando_lista

def filter_tokenizer(dataframe):
    token_sentence=''
    dataframe = dataframe.reset_index()
    most_rec_filter,max_rec = count_bulltes(dataframe)
    if(max_rec>1):
        index_filter = []
        if(most_rec_filter == 'mapping_regex_letter_dot'):index_filter = mapping_regex_letter_dot(dataframe)
        if(most_rec_filter == 'mapping_regex_letter_paran'):index_filter = mapping_regex_letter_paran(dataframe)
        if(most_rec_filter == 'mapping_regex_numb_dot'):index_filter = mapping_regex_numb_dot(dataframe)
        if(most_rec_filter == 'mapping_regex_numb_paran'):index_filter = mapping_regex_numb_paran(dataframe)
        if(most_rec_filter == 'mapping_regex_bullet'):index_filter = mapping_regex_numb_paran(dataframe)

        token_sentence = slice_sentence(dataframe,index_filter)
        
    # else:
    #     ...
    return token_sentence
        
def mapping_regex_bullet(dataframe,msg:str='bullet circle')->dict:
    letter_paren = re.compile(r'^•',re.IGNORECASE)
    linhas = []
    indices = []
    obj_response = {'indices':[],'confianca':msg}
    for index, row in dataframe.iterrows():
        result = letter_paren.findall(row['text']) 
        if result:
            obj_response['indices'].append(index)
            linhas.append(row['text'])
    return obj_response

def mapping_regex_white_space(dataframe,msg:str='WHITE SPACE')->dict:
    letter_paren = re.compile(r'(^^\s{0,}$)',re.IGNORECASE)
    linhas = []
    indices = []
    obj_response = {'indices':[],'confianca':msg}
    for index, row in dataframe.iterrows():
        result = letter_paren.findall(row['text']) 
        if result:
            obj_response['indices'].append(index)
            linhas.append(row['text'])
    return obj_response

def mapping_regex_letter_dot(dataframe,msg:str='a.')->dict:
    letter_paren = re.compile(r'[^a-z][a-z]\.|^[a-z]\s{0,}?\.',re.IGNORECASE)
    linhas = []
    indices = []
    obj_response = {'indices':[],'confianca':msg}
    for index, row in dataframe.iterrows():
        result = letter_paren.findall(row['text']) 
        if result:
            obj_response['indices'].append(index)
            linhas.append(row['text'])
    return obj_response

def mapping_regex_numb_dot(dataframe,msg:str='1.')->dict:
    letter_paren = re.compile(r'^\d{0,3}\s{0,}?\.',re.IGNORECASE)
    linhas = []
    indices = []
    obj_response = {'indices':[],'confianca':msg}
    
    for index, row in dataframe.iterrows():
        result = letter_paren.findall(row['text']) 
        if result:
            obj_response['indices'].append(index)
            linhas.append(row['text'])
    return obj_response

def mapping_regex_letter_paran(dataframe,msg:str='a)')->dict:
    letter_paren = re.compile(r'([^a-z][a-z]\)|^[a-z]\s{0,}?\.)',re.IGNORECASE)
    linhas = []
    indices = []
    obj_response = {'indices':[],'confianca':msg}
    for index, row in dataframe.iterrows():
        result = letter_paren.findall(row['text']) 
        if result:
            obj_response['indices'].append(index)
            linhas.append(row['text'])
    return obj_response

def mapping_regex_numb_paran(dataframe,msg:str='1)')->dict:
    letter_paren = re.compile(r'([^a-z]\d\)|^\d\s{0,}?\))',re.IGNORECASE)
    linhas = []
    indices = []
    obj_response = {'indices':[],'confianca':msg}
    for index, row in dataframe.iterrows():
        result = letter_paren.findall(row['text']) 
        if result:
            obj_response['indices'].append(index)
            linhas.append(row['text'])
    return obj_response

def count_bulltes(dataframe)->str:
    """
    Deverá retornar o bullet mais recorrente
    """
    count_letter_dot= len(mapping_regex_letter_dot(dataframe)['indices'])
    count_letter_paran= len(mapping_regex_letter_paran(dataframe)['indices'])
    count_numb_dot= len(mapping_regex_numb_dot(dataframe)['indices'])
    count_numb_paran= len(mapping_regex_numb_paran(dataframe)['indices'])
    count_bullet = len(mapping_regex_bullet(dataframe)['indices'])

    filters_list = ['mapping_regex_letter_dot','mapping_regex_letter_paran','mapping_regex_numb_dot','mapping_regex_numb_paran','count_bullet']
    most_rec = [count_letter_dot,count_letter_paran,count_numb_dot,count_numb_paran,count_bullet]
 
    index_resp = most_rec.index(max(most_rec))
    response = filters_list[index_resp]

    return response,max(most_rec)

def last_terms(dataframe,list_regex)->dict:
    dataset_last_page = token_last_page(dataframe)
    dataset_last_page = dataset_last_page.reset_index()
    obj_find = {'index':0,'termo':'','sent':'','sentences':[]}
    for index,row in dataset_last_page.iterrows():
        obj_find['sentences'].append(row['text'])
        search_regex = regex_validando_lista(list_regex,row['text'])
        if (search_regex!='não encontrado'):
            obj_find['index'] = index
            obj_find['termo'] = search_regex
            obj_find['sent'] = row['text']
    return obj_find


"""POSSÍVEIS REGRAS:

==========Validadores fracos==============

- a) 

- a.

==========Validadores fortes=============

- espaços entre validadores fracos


=====Caso não encontre nenhuma regra, vá por este caminho===

quebra por espaços em branco

"""
