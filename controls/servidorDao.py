from controls.dao.daoAdapter import DaoAdapter
from models.servidorPublico import ServidorPublico

class ServidorDao(DaoAdapter):
    def __init__(self):
        super().__init__(ServidorPublico)
        self.servidor = None

    def get_servidor(self):
        if self.servidor == None:
            self.servidor = ServidorPublico()
        return self.servidor

    def set_servidor(self, value):
        self.servidor = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._save(self.get_servidor())