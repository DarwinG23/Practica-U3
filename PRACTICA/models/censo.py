from models.persona import Persona

class Censo:
    def __init__(self):
        self.__id = 0
        self.__fecha = ""
        self.__nene = 0
        self.__peso = 0.0
        self.__estatura = 0.0
        self.__censador = ""

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _nene(self):
        return self.__nene

    @_nene.setter
    def _nene(self, value):
        self.__nene = value

    @property
    def _peso(self):
        return self.__peso

    @_peso.setter
    def _peso(self, value):
        self.__peso = value

    @property
    def _estatura(self):
        return self.__estatura

    @_estatura.setter
    def _estatura(self, value):
        self.__estatura = value

    @property
    def _censador(self):
        return self.__censador

    @_censador.setter
    def _censador(self, value):
        self.__censador = value
    
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "fecha": self.__fecha,
            "nene":  self.__nene,    #Persona().serializable if self.__nene == None else self.__nene.serializable,
            "peso": self.__peso,
            "estatura": self.__estatura,
            "censador": self.__censador
        }
    
    def deserializar(data):
        censo = Censo()
        censo._id = data["id"]
        censo._fecha = data["fecha"]
        censo._nene = data["nene"]   #Persona.deserializar(data["nene"])
        censo._peso = data["peso"]
        censo._estatura = data["estatura"]
        censo._censador = data["censador"]
        return censo
