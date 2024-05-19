from controls.tda.queue.queueOperations import QueueOperation
from models.categoriaCalificacion import CategoriaCalificacion

class Atencion:
    def _init_(self):
        self.__id = 0
        self.__nombre = ''
        self.__tiempoDeAtencion = ''
        self.__calificacion = CategoriaCalificacion

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _tiempoDeAtencion(self):
        return self.__tiempoDeAtencion

    @_tiempoDeAtencion.setter
    def _tiempoDeAtencion(self, value):
        self.__tiempoDeAtencion = value

    @property
    def _calificacion(self):
        return self.__calificacion

    @_calificacion.setter
    def _calificacion(self, value):
        self.__calificacion = value


    @property
    def serealizable(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "tiempoDeAtencion": self.__tiempoDeAtencion,
            "calificacion": self.__calificacion,
            

        }
    
    def deserealize(data):
        atencion = Atencion()
        atencion.__id = data["id"]
        atencion.__nombre = data["nombre"]
        atencion.__tiempoDeAtencion = data["tiempoDeAtencion"]
        atencion.__calificacion = data["calificacion"]

        return atencion

    def __str__(self):
        return f"\nNombre: {self.__nombre}, Tiempo de atencion: {self.__tiempoDeAtencion}, Calificacion: {self.__calificacion}"