import pandas as pd

def clean_signature(dataframe):
    """ OBS - Com o estudo feito, todas as iniciais protocoladas tem uma frase sobre 'assinatura eletronica' 
    que tem como font Helvetica
        INPUT- 
            dataframeF = dataframe a ser tratado
    RETORNA UM DATAFRAME E SALVA UM EXCEL"""   
    helvetica = dataframe.query('font.str.contains("Helvetica") & size<9')
    index_helvetica = helvetica.index
    data_frame_filtrado = dataframe.copy()
    data_frame_filtrado.drop(index_helvetica , inplace=True)
    return data_frame_filtrado

def remove_footer(dataframe):
    """ OBS - Com o estudo feito, todas as iniciais protocoladas tem uma frase sobre 'assinatura eletronica' 
    que tem como font Helvetica
        INPUT- 
            dataframeF = dataframe a ser tratado
    RETORNA UM DATAFRAME E SALVA UM EXCEL"""   
    dataset_teste = dataframe.query('size>=9.97 and not font.str.contains("Helvetica")')
    data_frame_filtrado = dataset_teste.copy()

    return data_frame_filtrado