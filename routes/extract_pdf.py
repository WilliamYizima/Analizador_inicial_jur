from flask import Blueprint, request, jsonify
from controllers.controller_extract_requests import create_structe_excel
extract_pdf = Blueprint('extract_pdf', __name__)
import os

regex_titulos_pedidos = ['Dos Pedidos','PEDIDOS','Pleiteia','PEDIDO','REQUERIMENTOS']

@extract_pdf.route('/extract_pdf/pdf_struct', methods=['POST'])
def run():
    try:
        body = request.get_json()
        name_excel = body['name_excel']
        name_pdf = body['name_pdf']
        path_pdf = f'./download/upload/{name_pdf}'
        print(path_pdf)
        print(name_excel)
        retorno = create_structe_excel(path_pdf,name_excel,regex_titulos_pedidos)
        return jsonify(
            code=200,
            message='successfully executed',
            content=f'{retorno}'
        )
    except:
        return jsonify(
            code=500,
            message='something happend',
            content=''
        )


@extract_pdf.route('/extract_pdf/create', methods=['POST'])
def create():
    try:
        if 'file_pdf' not in request.files:
            return jsonify(
                code=400,
                message='request file is empty!',
                content=''
            )
        file_received = request.files['file_pdf']
        # upload_path = app.config['UPLOAD_PATH']
        file_received.save(f'./download/upload/{file_received.filename}')
        return jsonify(
            code=200,
            message=f'PDF received ',
            content=''
        )

    except:
        return jsonify(
            code=500,
            message='Dawn! Retry this Proccess',
            content=''
        )

@extract_pdf.route('/extract_pdf/create_zip', methods=['POST'])
def create_zip():
    try:
        if 'file_zip' not in request.files:
            return jsonify(
                code=400,
                message='request file is empty!',
                content=''
            )
        file_received = request.files['file_zip']
        # upload_path = app.config['UPLOAD_PATH']
        file_received.save(f'./download/upload/{file_received.filename}')
        return jsonify(
            code=200,
            message=f'ZIP received ',
            content=''
        )

    except:
        return jsonify(
            code=500,
            message='Dawn! Retry this Proccess',
            content=''
        )
