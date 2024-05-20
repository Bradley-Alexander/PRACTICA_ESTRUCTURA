import sys
import copy
import psutil
import os
sys.path.append('../')
from controls.tda.queue.queue import Queue
from models.atencion import Atencion
from controls.atencionDaoControl import AtencionDaoControl
from controls.tda.queue.queueArray import QueueArray
from memory_profiler import profile
from time import time

#inicioList = time()

atencionDC1 = AtencionDaoControl()
atencionDC2 = AtencionDaoControl()
atencionDC3 = AtencionDaoControl()

servidor1 = Queue(3)


#inicioArray = time()

atencionDC2 = AtencionDaoControl()
servidorArray = QueueArray(3)

atencionDC2._atencion._nombre = "Francisco"
atencionDC2._atencion._tiempoDeAtencion = "30 minutos"
atencionDC2._atencion._calificacion = "BUENO"

servidorArray.push(atencionDC2._atencion)


atencionDC2._atencion._nombre = "Francisco"
atencionDC2._atencion._tiempoDeAtencion = "30 minutos"
atencionDC2._atencion._calificacion = "BUENO"

servidorArray.push(atencionDC2._atencion)


atencionDC2._atencion._nombre = "Francisco"
atencionDC2._atencion._tiempoDeAtencion = "30 minutos"
atencionDC2._atencion._calificacion = "BUENO"

servidorArray.push(atencionDC2._atencion)

print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("Array")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
servidorArray.print
servidorArray.pop()
servidorArray.print
servidorArray.pop()
servidorArray.print

print("-------------------------------------------------------")
print("-------------------------------------------------------")
process = psutil.Process(os.getpid())
memory_usage = process.memory_info().rss 
print(f"La memoria utilizada por el programa es: {memory_usage} MB")
#finArray = time()
print("-------------------------------------------------------")
print("-------------------------------------------------------")



#tiempo_total_list = finList - inicioList

#tiempo_total_array = finArray - inicioArray

#print("Tiempo de ejecucion con lista: ", tiempo_total_list)
#print("Tiempo de ejecucion con array: ", tiempo_total_array)



def get_size(obj):
    return sys.getsizeof(obj)

vector_queue = QueueArray(1000)

linked_list_queue = Queue(1000) 

for i in range(1000):
    vector_queue.push(i)
    linked_list_queue.push(i)

# Medir el uso de memoria
vector_queue_size = get_size(vector_queue)
linked_list_queue_size = get_size(linked_list_queue)

print(f"Memoria usada por la cola con vector: {vector_queue_size} bytes")
print(f"Memoria usada por la cola con lista enlazada: {linked_list_queue_size} bytes")











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