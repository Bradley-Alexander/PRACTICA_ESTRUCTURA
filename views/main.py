import sys
import copy
sys.path.append('../')
from controls.tda.queue.queue import Queue
from controls.tda.linked.linkedList import Linked_List
from models.atencion import Atencion
from models.servidorPublico import ServidorPublico

servidor1 = ServidorPublico()
servidor2 = ServidorPublico()
servidor3 = ServidorPublico()

atencion = Atencion()

print("Ventanilla 1")
atencion._nombre = "Estalin"
atencion._tiempoDeAtencion = "30 minutos"
atencion._calificacion = "Excelente"
servidor1._cola.push(copy.deepcopy(atencion))

atencion._nombre = "Pepito"
atencion._tiempoDeAtencion = "10 minutos"
atencion._calificacion = "Malo"
servidor1._cola.push(copy.deepcopy(atencion))

atencion._nombre = "Santi"
atencion._tiempoDeAtencion = "19 minutos"
atencion._calificacion = "Regular"
servidor1._cola.push(copy.deepcopy(atencion))

servidor1._cola.print



print("Ventanilla 2")
atencion._nombre = "Estalin"
atencion._tiempoDeAtencion = "30 minutos"
atencion._calificacion = "Excelente"
servidor2._cola.push(copy.deepcopy(atencion))

atencion._nombre = "Pepito"
atencion._tiempoDeAtencion = "10 minutos"
atencion._calificacion = "Malo"
servidor2._cola.push(copy.deepcopy(atencion))

atencion._nombre = "Santi"
atencion._tiempoDeAtencion = "19 minutos"
atencion._calificacion = "Regular"
servidor2._cola.push(copy.deepcopy(atencion))

servidor2._cola.print



print("Ventanilla 3")
atencion._nombre = "Bradley"
atencion._tiempoDeAtencion = "40 minutos"
atencion._calificacion = "Excelente"
servidor3._cola.push(copy.deepcopy(atencion))

atencion._nombre = "Messi"
atencion._tiempoDeAtencion = "10 minutos"
atencion._calificacion = "Bueno"
servidor3._cola.push(copy.deepcopy(atencion))

atencion._nombre = "Rafael"
atencion._tiempoDeAtencion = "19 minutos"
atencion._calificacion = "Bueno"
servidor3._cola.push(copy.deepcopy(atencion))

servidor3._cola.print


#atencion = Atencion()

#ventanilla1 = Queue(5)
#ventanilla2 = Queue(5)
#ventanilla3 = Queue(5)

#ventanilla1.push(1)
#ventanilla1.push(2)
#ventanilla1.push(3)
#ventanilla1.push(4)
#ventanilla1.push(5)

#print(ventanilla1.print)
#ventanilla1.pop()
#print(ventanilla1.print)
#ventanilla1.pop()
#print(ventanilla1.print)


#-----------------------------------------------------