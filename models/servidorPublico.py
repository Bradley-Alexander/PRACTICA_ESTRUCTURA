from controls.tda.queue.queue import Queue

class ServidorPublico:
    def __init__(self):
        self.__ventanilla = 0
        self.__nombre = ''
        self.__cola = None

    @property
    def _ventanilla(self):
        return self.__ventanilla

    @_ventanilla.setter
    def _ventanilla(self, value):
        self.__ventanilla = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _cola(self):
        if self.__cola is None:
            self.__cola = Queue(3)
        return self.__cola

    @_cola.setter
    def _cola(self, value):
        self.__cola = value

    @property
    def serealizable(self):
        return {
            "ventanilla": self.__ventanilla,
            "nombre": self.__nombre,
            "cola": self.__cola
        }
    
    def deserealize(self, data):
        servidor = ServidorPublico()
        servidor.__ventanilla = data["ventanilla"]
        servidor.__nombre = data["nombre"]
        servidor.__cola = data["cola"]

        return servidor