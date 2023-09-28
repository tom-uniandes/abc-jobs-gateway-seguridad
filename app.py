from flask import Flask
from flask_cors import CORS

from gateway import (
    Sesion, 
    Oferta
)

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

cors = CORS(app)

@app.route('/login', methods=['POST'])
def post_login_user():
    return Sesion.login_user(Sesion, "/autenticacion")

@app.route('/create-project', methods=['POST'])
def post_autorization():
    return Oferta.create_project(Oferta, "/oferta")
    

if __name__ == '__main__':
    app.run(port=5005)

