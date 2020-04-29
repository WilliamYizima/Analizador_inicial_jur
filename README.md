# Estruturador de Inicial

## O projeto

Passo a passo da lógica:

- Olha para cada 'título'
- Deste título, usa um regex para saber se aquela seção é importante(no caso seção pedidos)
- Corta desta seção até o final quebrando por linha
- Junta e configura um 'estrofe' com certas características

- Características atuais de um título


- Características atuais para quebra de um parágrafo

## Como rodar

- git clone
- crie um ambiente virtual:
    ```bash
        virtualenv -p python3 env
    ```
- rode o ambiente virtual:
    ```bash
        source env/bin/activate
    ```

- instale as libs
    ```bash
       pip install -r requirements.txt
    ```

- rode o FASTAPI

    ```bash
       uvicorn app:app
    ```

- rode EM DEV FASTAPI

    ```bash
       uvicorn app:app --reload
    ```

