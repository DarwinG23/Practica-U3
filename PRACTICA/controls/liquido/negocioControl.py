from controls.dao.daoAdapter import DaoAdapter
from models.liquido.negocio import Negocio

class NegocioControl(DaoAdapter):
    def __init__(self):
        super().__init__(Negocio)
        self.__negocio = None

    @property
    def _negocio(self):
        if self.__negocio == None:
            self.__negocio = Negocio()
        return self.__negocio

    @_negocio.setter
    def _negocio(self, value):
        self.__negocio = value

    def _lista(self):
        return self._list()

    @property
    def save(self):
        #self._negocio._id = self.lista._length + 1
        self._save(self._negocio)
        
    def merge(self, pos):
        self._merge(self._negocio, pos)