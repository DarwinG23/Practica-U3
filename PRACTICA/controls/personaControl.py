from models.persona import Persona
from controls.tda.linked.linkedList import Linked_List
import json
import os
class PersonaControl:
    
    def __init__(self):
        self.__persona = None
        self.__lista = Linked_List()

    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Persona()
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value


   #guardar en archivo json
    def save_json(self, data):
        with open("../files/persona.json", "w") as outfile:
            json.dump(data, outfile, indent=4)
    

    def read_json(self):
        if os.path.exists("../files/persona.json"): #si existe el archivo
            with open("../files/persona.json") as file: #abrir archivo
                data = json.load(file)
                return self.to_list(data)
        else:
           return self.__lista

    #pasar lista a diccionario
    def to_dict(self):
        array = self.__lista.toArray
        array_dict = []
        for i in range(0, len(array)):
            array_dict.append(array[i].__dict__)
        return array_dict
    
    #pasar diccionario a lista
    def to_list(self, array_dict):
        for i in range(0, len(array_dict)):
            persona = Persona()
            persona.__dict__ = array_dict[i]
            self.__lista.addNode(persona, self.__lista._length)
        return self.__lista
        


    @property
    def save(self):
        self.__persona._id = self.read_json()._length + 1
        self.__lista.addNode(self.__persona, self.__lista._length) 
        self.save_json(self.to_dict())
        
       
        
        
