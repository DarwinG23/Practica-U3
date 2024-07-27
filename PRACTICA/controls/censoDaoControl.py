from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.censo import Censo

class CensoDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Censo)
        self.__censo = None

    @property
    def _censo(self):
        if self.__censo == None:
            self.__censo = Censo()
        return self.__censo

    @_censo.setter
    def _censo(self, value):
        self.__censo = value


    def _lista(self):
        return self._lista()

    @property
    def save(self):
        #self._censo._id = self.lista._length + 1
        
        self._save(self._censo)


   

    

    

