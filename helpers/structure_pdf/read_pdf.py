import fitz

def structure_pdf(nome_pdf:str):
    """Lê PDF e Estrutura para gerar o Excel
    Arguments:
        nome_pdf {str} -- caminho do arquivo com a extensão para ler o arquivo.
        EX: 'dataset_arquivos_pd_validar/Peticao_BK-3.pdf'
    
    Returns:
        [dict] -- Retorna um dicionário para criar o dataframe
    """
    estrutura_documento_02 = []
    doc_teste = fitz.open(nome_pdf)
    quantidade_pagina_arquivo = doc_teste.pageCount
    # lendo pagina
    for pagina in range(quantidade_pagina_arquivo):
        page = doc_teste.loadPage(pagina)
        obj_structure = page.getText('dict')
        estrutura_documento_02.append(obj_structure)
    paginas_conteudo = []
    conta_pagina01=0
    # lendo 'blocks'
    for paginas in estrutura_documento_02:
        paginas_conteudo.append(paginas['blocks'])
    linhas_atributos = []
    pagina_numeracao = []
    # lendo 'conteudo'
    for i in range(len(paginas_conteudo)):
        conteudo = paginas_conteudo[i]
        for j in range(len(conteudo)):
            if('lines' in conteudo[j]):
                obj_atributo = {'linha_atributo':[],'pagina':''}
                obj_atributo['linha_atributo']=conteudo[j]['lines']
                obj_atributo['pagina'] = i+1
                linhas_atributos.append(obj_atributo) 
    text = []
    size = []
    font = []
    count = 0
    id = []
    page = []
    # lendo 'linhas'
    for linhas01 in linhas_atributos:
        minha_pagina = linhas01['pagina']
        for linhas02 in linhas01['linha_atributo']:
            for linha_atributos in linhas02['spans']:
                text.append(linha_atributos['text'])
                size.append(linha_atributos['size'])
                font.append(linha_atributos['font'])
                page.append(minha_pagina)
                id.append(count)
                count = count+1

    data_4excel = {'id':id,'page':page,'font':font,'size':size,'text':text}
    return data_4excel