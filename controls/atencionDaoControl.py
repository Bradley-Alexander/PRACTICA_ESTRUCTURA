from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.atencion import Atencion
from controls.dao.arrayDaoAdapter import ArrayDaoAdapter

class AtencionDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Atencion)
        self.__id_counter = 0
        self.__atencion = None

    @property
    def _atencion(self):
        if self.__atencion is None:
            self.__atencion = Atencion()
        return self.__atencion

    @_atencion.setter
    def _atencion(self, value):
        self.__atencion = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._atencion._id = self._lista._lenght + 1
        self._save(self._atencion)

    def merge(self, pos):
        self._merge(self._atencion, pos)

    def delete(self, pos):
        self._delete(pos)

    def delete(self):
        self._list()
        if self.lista._lenght > 0:
            self._delete(0)
        else:
            raise IndexError("The queue is empty")