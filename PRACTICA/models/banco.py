class Banco:
    
    def __init__(self) -> None:
        self.__id = 0
        self.__nombre = ""
        self.__direccion = ""
        self.__horario = "s/n"
        self.__telefono = "s/n"
        self.__latitud = "0.0"
        self.__longitud = "0.0"

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _horario(self):
        return self.__horario

    @_horario.setter
    def _horario(self, value):
        self.__horario = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    @property
    def _latitud(self):
        return self.__latitud

    @_latitud.setter
    def _latitud(self, value):
        self.__latitud = value

    @property
    def _longitud(self):
        return self.__longitud

    @_longitud.setter
    def _longitud(self, value):
        self.__longitud = value
        
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "direccion": self.__direccion,
            "horario": self.__horario,
            "telefono": self.__telefono,
            "latitud": self.__latitud,
            "longitud": self.__longitud
        }
        
    
    def deserializar(data):
        banco = Banco()
        banco._id = data["id"]
        banco._nombre = data["nombre"]
        banco._direccion = data["direccion"]
        banco._horario = data["horario"]
        banco._telefono = data["telefono"]
        banco._latitud = data["latitud"]
        banco._longitud = data["longitud"]
        return banco
    
    def __str__(self) -> str:
        return f"{self.__id} {self.__nombre}  {self.__latitud} {self.__longitud}"

        

  