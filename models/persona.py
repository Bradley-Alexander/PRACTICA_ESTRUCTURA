import random as r

class Persona:
    def __init__(self):
        self.__apellidos = ''
        self.__nombres = ''

    @property
    def _apellidos(self):
        return self.__apellidos

    @_apellidos.setter
    def _apellidos(self, value):
        self.__apellidos = value

    @property
    def _nombres(self):
        return self.__nombres

    @_nombres.setter
    def _nombres(self, value):
        self.__nombres = value


    # def to_dict(self):
    #     return {
    #         'id': self.__id,
    #         'apellidos': self.__apellidos,
    #         'nombres': self.__nombres,
    #         'dni': self.__dni,
    #         'direccion': self.__direccion,
    #         'telefono': self.__telefono,
    #         'tipo_identificacion': self.__tipo_identificacion.value
    #     }
    
    @property
    def serializable(self):
        return {
            "apellidos": self.__apellidos,
            "nombres": self.__nombres,   
        }
    
    def deserializar(data):
        persona = Persona()
        persona._apellidos = data["apellidos"]
        persona._nombres = data["nombres"]
        return persona
        
    def __str__(self) -> str:
        return self.__apellidos + "" + self.__nombres