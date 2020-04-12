from helpers.help.helpers import treatament_file_name
from helpers.filter_apply.token_senteces import filter_tokenizer


def reponse(path_pdf:str,dataset_request):
    obj_reponse = {
        'file_name':'',
        'text_requests':'',
        'sentences':[]
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

    
    return obj_reponse

