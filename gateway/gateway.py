from flask import request, json
import requests

urlBaseSesion = 'http://localhost:5003'
urlBaseOferta = 'http://localhost:5002'

class Sesion:
    def login_user(self, endpoint):
        body = request.get_json()
        endpoint = urlBaseSesion + endpoint

        response = requests.request(
            method = request.method,
            url = endpoint,
            headers = request.headers,
            data = request.get_data(),
            json = body,
        )

        return json.loads(response.content), response.status_code
    
    def verify_autorization(self):
        body = request.get_json()
        endpoint = urlBaseSesion + "/autoriza/oferta"

        response = requests.request(
            method = "get",
            url = endpoint,
            headers = request.headers,
            data = request.get_data(),
            json = body,
        )
        return response

class Oferta:
    def create_project(self, endpoint):
        response = Sesion.verify_autorization(Sesion)
        if response.status_code == 200:
            body = request.get_json()
            endpoint = urlBaseOferta + endpoint
            response = requests.request(
                method = request.method,
                url = endpoint,
                headers = request.headers,
                data = request.get_data(),
                json = body,
            )
            return json.loads(response.content), response.status_code
        else:
            return {"mensaje": "Usuario no autorizado para crear proyectos"}, 401
