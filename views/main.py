import sys
import copy
sys.path.append('../')
from controls.tda.queue.queue import Queue
from controls.tda.linked.linkedList import Linked_List
from models.atencion import Atencion
from models.servidorPublico import ServidorPublico
from controls.atencionDaoControl import AtencionDaoControl
from controls.servidorDaoControl import ServidorDaoControl
from controls.tda.queue.queueArray import QueueArray

servidor1 = Queue(3)
servidor2 = Queue(7)
servidor3 = Queue(7)


atencionDC1 = AtencionDaoControl()
atencionDC2 = AtencionDaoControl()
atencionDC3 = AtencionDaoControl()


print("Ventanilla 1")

atencionDC1._atencion._nombre = "Juan"
atencionDC1._atencion._tiempoDeAtencion = "15 minutos"
atencionDC1._atencion._calificacion = "BUENO"


servidor1.push(copy.deepcopy(atencionDC1._atencion))


atencionDC1._atencion._nombre = "Messi"
atencionDC1._atencion._tiempoDeAtencion = "30 minutos"
atencionDC1._atencion._calificacion = "MALO"


servidor1.push(copy.deepcopy(atencionDC1._atencion))


atencionDC1._atencion._nombre = "Pepe"
atencionDC1._atencion._tiempoDeAtencion = "5 minutos"
atencionDC1._atencion._calificacion = "REGULAR"


servidor1.push(copy.deepcopy(atencionDC1._atencion))



print("-----------------------------------------------------------------------")
servidor1.print
print("-----------------------------------------------------------------------")
servidor1.pop()
servidor1.print
print("-----------------------------------------------------------------------")
servidor1.pop()
servidor1.print
print("-----------------------------------------------------------------------")

servidorArray = QueueArray(3)

atencionDC1._atencion._nombre = "Pepe"
atencionDC1._atencion._tiempoDeAtencion = "30 minutos"
atencionDC1._atencion._calificacion = "BUENO"

servidorArray.push(copy.deepcopy(atencionDC1._atencion))


atencionDC1._atencion._nombre = "Raul"
atencionDC1._atencion._tiempoDeAtencion = "25 minutos"
atencionDC1._atencion._calificacion = "REGULAR"

servidorArray.push(copy.deepcopy(atencionDC1._atencion))


atencionDC1._atencion._nombre = "Carlos"
atencionDC1._atencion._tiempoDeAtencion = "10 minutos"
atencionDC1._atencion._calificacion = "EXELENTE"

servidorArray.push(copy.deepcopy(atencionDC1._atencion))

print("000000000000000000000000000000000")

servidorArray.print
servidorArray.pop()
servidorArray.print
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