from flask import Blueprint, jsonify, abort, request, render_template, redirect 
from controls.atencionDaoControl import AtencionDaoControl
from controls.tda.queue.queue import Queue
from flask_cors import CORS
import random
router = Blueprint('router', __name__)


#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion
#
@router.route('/')
def home():
    return render_template("template.html")
 

@router.route('/atenciones')
def lista_atenciones():
    ad = AtencionDaoControl()
    return render_template("nene/cola.html", lista=ad.to_dict())


@router.route('/atencion/ver')
def ver_guardar():
    return render_template("nene/guardarCola.html")


#guardar personas
@router.route('/atenciones/guardar', methods=["POST"])
def guardar_personas():
    ad = AtencionDaoControl()
    servidor1 = Queue(7)
    data = request.form
    
    if not "nombre" in data.keys():
        abort(400)
        
    #TODO ...Validar
    ad._atencion._nombre = data["nombre"]
    ad._atencion._tiempoDeAtencion = data["tiempoDeAtencion"]
    ad._atencion._calificacion = data["calificacion"]
    ad.save
    servidor1.push(ad._atencion)
    return redirect("/atenciones", code=302)

@router.route('/atenciones/eliminar', methods=["POST"])
def eliminar_atencion():
    ad = AtencionDaoControl()
    try:
        ad.delete()
        return redirect("/atenciones", code=302)
    except IndexError as e:
        return jsonify({"message": str(e)}), 400

@router.route('/atenciones/editar/<pos>')
def ver_editar(pos):
    ad = AtencionDaoControl()
    nene = ad._list().get(int(pos) -1)
    print(nene)
    return render_template("nene/editarCola.html", data = nene )

 

@router.route('/atenciones/modificar', methods=["POST"])
def modificar_atenciones():
    ad = AtencionDaoControl()
    data = request.form
    pos = data["id"]
    nene = ad._list().get(int(data["id"]))
    if not "nombre" in data.keys():
        abort(400)
        
    #TODO ...Validar
    ad._atencion = nene
    ad._atencion._nombre = data["nombre"]
    ad._atencion._tiempoDeAtencion = data["tiempoDeAtencion"]
    ad._atencion._calificacion = data["calificacion"]
    ad.merge(int(pos) -1)
    return redirect("/atenciones", code=302)


@router.route('/atenciones/agregarACola/<pos>')
def agregar_a_cola(pos):
    ad = AtencionDaoControl()
    cola = Queue(7)
    nene = ad._list().get(int(pos))
    ad._atencion = nene
    cola.push(ad)
    return redirect("/atenciones", code=302)


@router.route('/cola')
def cola():
    lista = [
        {'nombre': 'Juan', 'calificacion': 'Bueno', 'tiempoDeAtencion': 15},
        {'nombre': 'Bradley', 'calificacion': 'Malo', 'tiempoDeAtencion': 10},
        {'nombre': 'Alexander', 'calificacion': 'Regular', 'tiempoDeAtencion': 35},
        {'nombre': 'Maria', 'calificacion': 'Muy Bueno', 'tiempoDeAtencion': 20},
        {'nombre': 'Raul', 'calificacion': 'Exelente', 'tiempoDeAtencion': 15},
        {'nombre': 'Nelson', 'calificacion': 'Malo', 'tiempoDeAtencion': 15},
        {'nombre': 'Santiago', 'calificacion': 'Regular', 'tiempoDeAtencion': 65},
        {'nombre': 'Jared', 'calificacion': 'Bueno', 'tiempoDeAtencion': 5},
        {'nombre': 'Santiago', 'calificacion': 'Muy Bueno', 'tiempoDeAtencion': 15},
        {'nombre': 'Jair', 'calificacion': 'Exelente', 'tiempoDeAtencion': 45},
        {'nombre': 'Elizabeth', 'calificacion': 'Malo', 'tiempoDeAtencion': 20},
        {'nombre': 'Carlos', 'calificacion': 'Bueno', 'tiempoDeAtencion': 30}
        # Agrega más elementos según sea necesario
    ]

    # Selecciona 5 elementos aleatorios (o menos si hay menos de 5 elementos en la lista)
    num_items = min(5, len(lista))
    lista_aleatoria = random.sample(lista, num_items)

    return render_template('cola.html', lista=lista_aleatoria)