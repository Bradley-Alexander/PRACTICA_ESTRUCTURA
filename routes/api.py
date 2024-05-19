from flask import Blueprint, jsonify, make_response, request
from controls.atencionDaoControl import AtencionDaoControl
from flask_cors import CORS
api = Blueprint('api', __name__)


#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion
#
@api.route('/')
def home():
    return make_response(
        jsonify({"msg":"OK", "code": 200}),
        200
    )

@api.route('/atenciones', methods=['GET'])
def get_atenciones():
    atenciones = AtencionDaoControl().to_dict()
    return jsonify(atenciones), 200


#lista personas
@api.route('/api/atenciones')
def lista_atenciones():
    ad = AtencionDaoControl()
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": ad.to_dict()}),
        200
    )
#guardar personas
@api.route('/api/atenciones/guardar', methods=["POST"])
def guardar_atencion():
    ad = AtencionDaoControl()
    data = request.json
    print(type(data))
    if not "apellido" in data.keys():
        return make_response(
            jsonify({"msg":"Faltan datos", "code": 400, "data": []}), 
            400
        )
        
    #TODO ...Validar
    ad._atencion.__nombre = data["nombre"]
    ad._atencion.__tiempoDeAtencion = data["tiempoDeAtencion"]
    ad._atencion.__calificacion = data["calificacion"]
    ad.save
    return make_response(
        jsonify({"msg":"OK, se ha registrado correctamente", "code": 200, "data": []}),
        200
    )

