import enum
class CategoriaCalificacion(enum.Enum):
    MALO = 1
    REGULAR = 2
    BUENO = 3
    MUY_BUENO = 4
    EXCELENTE = 5

    def getInstance(self):
        if self.instance == None:
            self.instance = CategoriaCalificacion()
        return self.instance
