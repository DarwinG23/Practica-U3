
from models.mru import mru

class calculos:
    def __init__(self):
       self.__mru =  mru()

    @property
    def _mru(self):
        return self.__mru

    @_mru.setter
    def _mru(self, value):
        self.__mru = value


    #TODO
    #x = v*t
    def calcularVelocidad(self):
        self.__mru._velocidad = self.__mru._distancia / self.__mru._tiempo
        return self.__mru._velocidad