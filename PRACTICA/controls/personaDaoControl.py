from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.persona import Persona

class PersonaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Persona) #sirve para llamar al constructor de la clase padre
        self.__persona = None

    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Persona()
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value


    def _lista(self):
        return self._list()

    @property
    def save(self):
        #self._persona._id = self.lista._length + 1
        self._save(self._persona)

    def merge(self, pos):
        self._merge(self._persona, pos)