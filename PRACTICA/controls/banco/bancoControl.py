from controls.dao.daoAdapter import DaoAdapter
from models.banco import Banco

class BancoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Banco)
        self.__banco = None

    @property
    def _banco(self):
        if self.__banco == None:
            self.__banco = Banco()
        return self.__banco

    @_banco.setter
    def _banco(self, value):
        self.__banco = value
        
    
    def _lista(self):
        return self._list()

    @property
    def save(self):
        #self._negocio._id = self.lista._length + 1
        self._save(self._banco)
        
    def merge(self, pos):
        self._merge(self._banco, pos)

    