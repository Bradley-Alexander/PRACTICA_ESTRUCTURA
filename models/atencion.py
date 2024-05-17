from controls.tda.queue.queueOperations import QueueOperation

class Atencion:
    def __init__(self,):
        self.__nombre = ''
        self.__tiempoDeAtencion = ''
        self.__calificacion = ''

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

    def __str__ (self):
        return f'\nNombre:{self.__nombre}, Tiempo Despacho:{self.__tiempoDeAtencion}, Calificacion:{self.__calificacion}'