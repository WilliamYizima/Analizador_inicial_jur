from flask import Flask
from routes import extract_pdf

app = Flask(__name__)
app.secret_key = "secret key"
app.register_blueprint(extract_pdf.extract_pdf)



@app.route("/")
def root():
    return "Extração de Pedidos PDF"


if __name__ == '__main__':
    port = 5000
    # serve(app, host=host, port=port)
    app.run(port=port, debug=True)
