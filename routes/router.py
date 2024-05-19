from flask import Blueprint, jsonify, abort, request, render_template, redirect 
from controls.atencionDaoControl import AtencionDaoControl
from controls.tda.queue.queue import Queue
from flask_cors import CORS
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