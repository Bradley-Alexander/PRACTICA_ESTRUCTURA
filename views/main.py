import sys
sys.path.append('../')
from controls.tda.queue.queue import Queue
from controls.tda.linked.linkedList import Linked_List
from models.atencion import Atencion
from models.servidorPublico import ServidorPublico

servidor1 = ServidorPublico()
servidor2 = ServidorPublico()
servidor3 = ServidorPublico()

servidor1.__nombre = "Juan"
servidor1.__ventanilla = 1
servidor1.__cola = Queue(3)

atencion1 = Atencion()

atencion1._tiempoDeAtencion = "30 minutos"
atencion1._calificacion = "Excelente"
atencion1._nombre = "Estalin"

servidor1.__cola.push(atencion1)

atencion2 = Atencion()

atencion2._tiempoDeAtencion = "10 minutos"
atencion2._calificacion = "Malo"
atencion2._nombre = "Pepito"

servidor1.__cola.push(atencion2)


atencion3 = Atencion()

atencion3._tiempoDeAtencion = "10 minutos"
atencion3._calificacion = "Malo"
atencion3._nombre = "Pepito"

servidor1.__cola.push(atencion3)

servidor1.__cola.print

#comentame el codigo siguiente

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