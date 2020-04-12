from helpers.help.helpers import treatament_file_name
from helpers.filter_apply.token_senteces import filter_tokenizer,last_terms


def reponse(path_pdf:str,dataset_request,dataset_full,list_regex_end_page):
    obj_reponse = {
        'file_name':'',
        'text_requests':'',
        'sentences':[],
        'last_page':{}
    }
    obj_reponse['sentences'] = filter_tokenizer(dataset_request)


    analyze_list = []
    sentence = {'num':0,'text':'','layout_analyze':''}
    obj_reponse['file_name'] = treatament_file_name(path_pdf)
    text_requests = [texto for texto in dataset_request['text'].values]
    obj_reponse['text_requests'] = ' '.join(text_requests)

    for index,texto in dataset_request.iterrows():
        analyze = {'num':index,'text':'','font_size':0,'font':'','sent_length':''}
        analyze['sent_length'] = len(texto)
        analyze['text'] = texto['text']
        analyze['font_size'] = texto['size']
        analyze['font'] = texto['font']
        analyze_list.append(analyze)
    obj_reponse['last_page'] = reponse_last_page(path_pdf,dataset_full,list_regex_end_page)
    
    return obj_reponse

def reponse_last_page(path_pdf,dataset,list_regex):
    obj_reponse = {
        'file_name':'',
        'end_petition':'',
        'term_regex':'',
        'sentences_last_page':[],
        'status':''
    }
    obj_last_terms = last_terms(dataset,list_regex)
    obj_reponse['file_name'] = treatament_file_name(path_pdf)
    obj_reponse['end_petition'] = obj_last_terms['sent']
    obj_reponse['term_regex'] = obj_last_terms['termo']
    obj_reponse['sentences_last_page'] = obj_last_terms['sentences']
    
    return obj_reponse
