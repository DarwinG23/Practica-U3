
from controls.tda.graph.graphNoManagedLabelledDos import GraphNoManagedLabelledDos
from controls.liquido.negocioControl import NegocioControl
from controls.liquido.distancia import Distancia
import os, re, json
from controls.tda.graph.adjacent import Adjacent

class NegocioGrafo():
    def __init__(self):
        self.__grafo = None
        self.__ndao = NegocioControl()
        self.__json_folder = "data/grafo.json"
        
    

    @property
    def _grafo(self):
        if self.__grafo == None:
            self.create_graph()
        return self.__grafo

    @_grafo.setter
    def _grafo(self, value):
        self.__grafo = value

       
    def create_graph(self,origen = None, destino = None, reiniciar = False):
        if os.path.exists(self.__json_folder) and not reiniciar:
            list = self.__ndao._list()
            if list._length > 0:
                
                self.__grafo = GraphNoManagedLabelledDos(list._length)
                arr = list.toArray
                for i in range(0, len(arr)):
                    self.__grafo.label_vertex(i, arr[i]._nombre)
                    
                self.__grafo = self.loadGraph
                
                adyacencias = self.__grafo.getListAdjacent
        
                for i in range(0, len(adyacencias)):
                    dic = adyacencias[i]
                    ady = Adjacent()
                    origenAdy = self.__ndao._list().binary_search_models(dic["from"], "_id")
                    destinoAdy = self.__ndao._list().binary_search_models(dic["to"], "_id")
        
                    peso = Distancia().calcularDistancia(origenAdy._longitud, origenAdy._latitud, destinoAdy._longitud, destinoAdy._latitud)
                    self.__grafo.__listAdjacent = []
                    self.__grafo.insert_edges_weight_E(origenAdy._nombre, destinoAdy._nombre, round(float(peso),3))
                    
        
                            
                if origen != None and destino != None:
                    peso = Distancia().calcularDistancia(origen._longitud, origen._latitud, destino._longitud, destino._latitud)           
                    self.__grafo.insert_edges_weight_E(origen._nombre, destino._nombre, round(float(peso),3))
                
                
                self.__grafo.paint_graph()
                
                self.saveGraph
                                
        else:
            list = self.__ndao._list()
            if list._length > 0:
                self.__grafo = GraphNoManagedLabelledDos(list._length)
                arr = list.toArray
                for i in range(0, len(arr)):
                    self.__grafo.label_vertex(i, arr[i]._nombre)
                self.__grafo.paint_graph()
                self.saveGraph
          
    @property      
    def saveGraph(self):
        if self.__grafo is not None:
            json_folder = "data"
            json_file = os.path.join(json_folder, "grafo.json")
            grafo_serializado = self.__grafo.serializar
            
            if os.path.exists(json_file):
                os.remove(json_file)
                
            with open(json_file, 'w') as file:
                json.dump(grafo_serializado, file, indent=4)
            return True
        else:
            return False
        
    @property
    def loadGraph(self):
        json_folder = "data"
        json_file = os.path.join(json_folder, "grafo.json")
        if os.path.exists(json_file):
            with open(json_file, 'r') as file:
                data = json.load(file)
                return GraphNoManagedLabelledDos.deserializar(data)
        else:
            print(f"El archivo {json_file} no existe.")
            return None
        
        
        
    
    