class ServidorPublico:
    def __init__(self):
        self.__velocidad = 0.0
        self.__cantidadUsuarios = 0
        self.__calificacion = "malo", "bueno", "regular", "muy bueno", "excelente" 
        self.__dia = "lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"

    def __str__(self):
        return f"Velocidad: {self.__velocidad}, Cantidad de Usuarios: {self.__cantidadUsuarios}, Calificacion: {self.__calificacion}, Dia: {self.__dia}"