from fastapi import FastAPI,Body
from pydantic import BaseModel
import os
from controllers.controller_extract_requests import create_structe_excel,analyze_mass


app = FastAPI()

regex_titulos_pedidos = ['Dos Pedidos','PEDIDOS','Pleiteia','PEDIDO','REQUERIMENTOS']
regex_fim_petição = ['Pede deferimento','Deferimento','Deferimento.']

@app.post("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

class Extract(BaseModel):
    name_excel: str
    name_pdf: str


class ResponseExtract(BaseModel):
    code:int
    content:str

@app.post('/extract_pdf/pdf_struct',
            response_model=ResponseExtract,
            responses ={
                200 :  {
            "content": {
                "application/json": {
                    "example": {
  "code": 200,
  "content": {
    "file_name": "Peticao_BK-3.pdf",
    "last_page": {
      "end_petition": "Pede deferimento. ",
      "file_name": "Peticao_BK-3.pdf",
      "sentences_last_page": [
        "que após a juntada de defesa e documentos, terá o autor melhores condições ",
        "para apuração por estimativa dos pedidos formulados. ",
        " ",
        "Nestes termos, ",
        "Pede deferimento. ",
        " ",
      ],
      "status": "salvo",
      "term_regex": "pede deferimento"
    },
    "sentences": [
      "79.   Requer os benefícios da justiça gratuita, por  ser pessoa pobre na acepção legal do termo, além de no momento não auferir  nenhum tipo de renda, e quando recebia o valor era inferior a 40% do teto da  previdência. ",
      "80.   Requer, ainda, seja determinada a exibição  pela Reclamada dos seguintes documentos, cartões de ponto, demonstrativos  de pagamento, ficha de registro, contrato de trabalho, extrato de fundo de  garantia e extrato de recolhimento do INSS, planilha ou balanço da empresa  para apuração dos valores de vendas a fim de comprovar o referido  Assinado eletronicamente. A Certificação Digital pertence a: CRISTOPHER TOMIELLO SOLDAINI http://pje.trt2.jus.br/primeirograu/Processo/ConsultaDocumento/listView.seam?nd=19031020285432600000132238168 Número do documento: 19031020285432600000132238168 Num. 444e655 - Pág. 28                                                                                                                                            T OMIELLO E  S OLDAINI  |   A DVOCACIA   29  R UA  J OSÉ  G OMES DE  A BREU ,   Nº  26,   CJ   141   –   N OVA  P ETRÓPOLIS  –   S ÃO  B ERNARDO DO  C AMPO  –   SP  TEL",
      ".   (55   11)   98221-1228   |  ADVOCACIA",
      ". TOMIELLOSOLDAINI @ GMAIL",
      ". COM       pagamento de participação nos lucros PPR semestral e remuneração variável,  nota fiscal de compra de EPI e EPC, certificados de aprovação respectivos,  comprovantes de entrega a reclamante, fiscalização do uso de EPI, bem como  ficha de registro e evolução salarial do paradigma. (todas as exibições nos  termos do art. 396 e sob as penas do art. 400 do Novo Código de Processo  Civil).  ",
      
    ],
    "text_requests": "XX- Dos requerimentos    79.   Requer os benefícios da justiça gratuita, por  ser pessoa pobre na acepção legal do termo, além de no momento não auferir  nenhum tipo de renda, e quando recebia o valor era inferior a 40% do teto da  previdência.  80.   Requer, ainda, seja determinada a exibição  pela Reclamada dos seguintes documentos, cartões de ponto, demonstrativos  de pagamento, ficha de registro, contrato de trabalho, extrato de fundo de  garantia e extrato de recolhimento do INSS, planilha ou balanço da empresa  para apuração dos valores de vendas a fim de comprovar o referido  Assinado eletronicamente. A Certificação Digital pertence a: CRISTOPHER TOMIELLO SOLDAINI http://pje.trt2.jus.br/primeirograu/Processo/ConsultaDocumento/listView.seam?nd=19031020285432600000132238168 Número do documento: 19031020285432600000132238168 Num. 444e655 - Pág. 28                                                                                                                                            T OMIELLO E  S OLDAINI  |   A DVOCACIA   29  R UA  J OSÉ  G OMES DE  A BREU ,   Nº  26,   CJ   141   –   N OVA  P ETRÓPOLIS  –   S ÃO  B ERNARDO DO  C AMPO  –   SP  TEL .   (55   11)   98221-1228   |  ADVOCACIA . TOMIELLOSOLDAINI @ GMAIL . COM       pagamento de participação nos lucros PPR semestral e remuneração variável,  nota fiscal de compra de EPI e EPC, certificados de aprovação respectivos,  comprovantes de entrega a reclamante, fiscalização do uso de EPI, bem como  ficha de registro e evolução salarial do paradigma. (todas as exibições nos  termos do art. 396 e sob as penas do art. 400 do Novo Código de Processo  Civil).   81.   Esclarece-se, desde já, que os documentos  ora solicitados são imprescindíveis ao correto e fidedigno deslinde do feito.  82.   Requer  a  procedência  da  reclamação  trabalhista, para condenar a reclamada ao pagamento das verbas pleiteadas,  com correção monetária, juros de mora, custas e despesas processuais.  83.   Requer a notificação da reclamada para  contestar a reclamação trabalhista, sob pena de sofrer os efeitos da revelia.  84.   Requer provar o alegado por todos os meios  de prova em direito admitidos, especialmente pelo depoimento pessoal da  reclamada, sob pena de confissão, oitiva de testemunhas, perícias e outros se  necessários.    XXI- Do valor da causa    85.   Da à causa para efeito de custas e alçada o  valor líquido de R$ 605.198,55 (seiscentos e cinco mil cento e noventa e oito  reais e cinquenta e cinco centavos).  86.   Consignamos que o valor ora arbitrado, é  realizado por mera estimativa não servindo, em nenhuma hipótese, como  fundamento para limitação do valor do  “quantum, debeatur”,  o qual será  fixado, oportunamente em regular execução de sentença. Entretanto, caso não  seja o entendimento deste Douto Juízo, requer o autor que antes de proferida  a decisão de mérito, seja o mesmo notificado a fim de, se for o caso, adequar o  valor da causa com uma estimativa mais próxima dos pedidos formulados, eis  Assinado eletronicamente. A Certificação Digital pertence a: CRISTOPHER TOMIELLO SOLDAINI http://pje.trt2.jus.br/primeirograu/Processo/ConsultaDocumento/listView.seam?nd=19031020285432600000132238168 Número do documento: 19031020285432600000132238168 Num. 444e655 - Pág. 29                                                                                                                                            T OMIELLO E  S OLDAINI  |   A DVOCACIA   30  R UA  J OSÉ  G OMES DE  A BREU ,   Nº  26,   CJ   141   –   N OVA  P ETRÓPOLIS  –   S ÃO  B ERNARDO DO  C AMPO  –   SP  TEL .   (55   11)   98221-1228   |  ADVOCACIA . TOMIELLOSOLDAINI @ GMAIL . COM       que após a juntada de defesa e documentos, terá o autor melhores condições  para apuração por estimativa dos pedidos formulados.    Nestes termos,  Pede deferimento.    São Paulo, 10 de março de 2019.    Cristopher Tomiello Soldaini  OAB/SP sob o nº 336.068  Assinado eletronicamente. A Certificação Digital pertence a: CRISTOPHER TOMIELLO SOLDAINI http://pje.trt2.jus.br/primeirograu/Processo/ConsultaDocumento/listView.seam?nd=19031020285432600000132238168 Número do documento: 19031020285432600000132238168 Num. 444e655 - Pág. 30",
    "title": [
      "BARRA FUNDA - SP.",
      "MICHAEL DOS SANTOS CORREA",
      "RECLAMAÇÃO TRABALHISTA",
      "BK BRASIL OPERAÇÃO E ASSESSORIA A RESTAURANTES S.A",
      "Notificações e Intimações",
      "I- Do contrato de trabalho",
      "II- Rescisão indireta do Contrato de Trabalho",
      "(II)",
      "(III)",
      "(IV)",
      "(VI)",
      "(VII)",
    ]
  },
  "message": "successfully executed"
}
                }
            },
        } 
        }
)

async def run(
                extract:Extract = Body(
                    ...,
                    example={
	                    "name_excel":"Peticao_BK-3.pdf",
	                    "name_pdf":"Peticao_BK-3.pdf"
                        },
                )
            ):
    """teste
    """
    name_excel = extract.name_excel
    name_pdf = extract.name_pdf
    path_pdf = f'./download/upload/{name_pdf}'
    retorno = create_structe_excel(path_pdf,name_excel,regex_titulos_pedidos,regex_fim_petição)
    return {'message' : retorno},200

# @app.post("/items/")
# async def create_item(item: Item):
#     return item