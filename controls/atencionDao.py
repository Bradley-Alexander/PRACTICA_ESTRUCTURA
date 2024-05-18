from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.atencion import Atencion

class AtencionDao(DaoAdapter):
    def __init__(self):
        super().__init__(Atencion)
        self.atencion = None

    def get_atencion(self):
        if self.atencion == None:
            self.atencion = Atencion()
        return self.atencion

    def set_atencion(self, value):
        self.atencion = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._save(self.get_atencion())   