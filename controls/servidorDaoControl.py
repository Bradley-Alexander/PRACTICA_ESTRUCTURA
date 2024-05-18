from controls.dao.daoAdapter import DaoAdapter
from models.servidorPublico import ServidorPublico

class ServidorDaoControl:
    def __init__(self):
        self.__servidor = None

    @property
    def _servidor(self):
        if self.__servidor is None:
            self.__servidor = ServidorPublico()
        return self.__servidor

    @_servidor.setter
    def _servidor(self, value):
        self.__servidor = value
    
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._save(self._servidor)