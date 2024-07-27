from models.enumTipoIdentificacion import EnumTipoIdentificacion
class Persona:
    def __init__(self):
        self.__id = 0  
        self.__nombres = ""
        self.__apellidos = ""
        self.__dni = ""
        self.__direccion = ""
        self.__telefono = ""
        self.__tipoIdentificacion = EnumTipoIdentificacion.CEDULA

    @property
    def _tipoIdentificacion(self):
        return self.__tipoIdentificacion

    @_tipoIdentificacion.setter
    def _tipoIdentificacion(self, value):
        self.__tipoIdentificacion = value


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombres(self):
        return self.__nombres

    @_nombres.setter
    def _nombres(self, value):
        self.__nombres = value

    @property
    def _apellidos(self):
        return self.__apellidos

    @_apellidos.setter
    def _apellidos(self, value):
        self.__apellidos = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value
    
    @property
    def serializable(self):
        
        #print(self._tipoIdentificacion.getValue)
        
        #print(type(self._tipoIdentificacion.getValue))
        
        return {
            "id": self.__id,
            "apellidos": self.__apellidos,
            "nombres": self.__nombres,
            "direccion": self.__direccion,
            "dni": self.__dni,
            "telefono": self.__telefono,
            "tipo": self.__tipoIdentificacion
        }
    

    def deserializar(data):
        persona = Persona()
        persona._id = data["id"]
        persona._apellidos = data["apellidos"]
        persona._nombres = data["nombres"]
        persona._direccion = data["direccion"]
        persona._dni = data["dni"]
        persona._telefono = data["telefono"]
        persona._tipoIdentificacion = data["tipo"] 

        return persona



    def __str__(self) -> str:
        return "{" + str(self.__id) + ": " + self.__apellidos + " " + self.__nombres + "}"
 
    

