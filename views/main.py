import sys
import copy
sys.path.append('../')
from controls.tda.queue.queue import Queue
from controls.tda.linked.linkedList import Linked_List
from models.atencion import Atencion
from models.servidorPublico import ServidorPublico
from controls.atencionDaoControl import AtencionDaoControl
from controls.servidorDaoControl import ServidorDaoControl

servidor1 = ServidorDaoControl()
servidor2 = ServidorDaoControl()
servidor3 = ServidorDaoControl()

atencionDC = AtencionDaoControl()


print("Ventanilla 1")
atencionDC._atencion._nombre = "COco"
atencionDC._atencion._tiempoDeAtencion = "30 minutos"
atencionDC._atencion._calificacion = "Excelente"
atencionDC.save

servidor1._servidor._cola.push(copy.deepcopy(atencionDC._atencion))


atencionDC._atencion._nombre = "Messi"
atencionDC._atencion._tiempoDeAtencion = "30 minutos"
atencionDC._atencion._calificacion = "Excelente"
atencionDC.save


servidor1._servidor._cola.push(copy.deepcopy(atencionDC._atencion))


atencionDC._atencion._nombre = "Pepe"
atencionDC._atencion._tiempoDeAtencion = "30 minutos"
atencionDC._atencion._calificacion = "Excelente"
atencionDC.save


servidor1._servidor._cola.push(copy.deepcopy(atencionDC._atencion))


servidor1._servidor._cola.print

servidor1._servidor._cola.pop()

servidor1._servidor._cola.print

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