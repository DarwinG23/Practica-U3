from controls.banco.bancoControl import BancoControl
from controls.tda.graph.graphNoManagedLabelledDos import GraphNoManagedLabelledDos
import os, re, json
from controls.tda.graph.adjacent import Adjacent
from controls.banco.distancia import Distancia

class BancoGrafo():
    def __init__(self):
        self.__grafo = None
        self.__ndao = BancoControl()
        self.__json_folder = "data/grafo.json"
        self.__matrizDistancias = []
        self.__matrizRecorridos = []
        
    

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
                    
                
                grafoCargado = self.loadGraph
                
                adyacencias = grafoCargado.getListAdjacent
                
        
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
        
    def crearMatrices(self):
        if self.__grafo is not None:
            arrayBancos = self.__ndao.to_dic()
            
            matrizDistancias = []
            matrizRecorridos = []

            for i in range(len(arrayBancos)):
                filaDistancias = ["INF"] * len(arrayBancos)
                filaRecorridos = ["-----"] * len(arrayBancos)
                matrizDistancias.append(filaDistancias)
                matrizRecorridos.append(filaRecorridos)
            
            for i in range(len(arrayBancos)):
                for j in range(len(arrayBancos)):
                    if i == j:
                        matrizDistancias[i][j] = 0
                        matrizRecorridos[i][j] = "-----"
                    else:
                        matrizRecorridos[i][j] = arrayBancos[j]["nombre"]
                    if self.__grafo.exist_edge_E(arrayBancos[i]["nombre"], arrayBancos[j]["nombre"]):
                        matrizDistancias[i][j] = self.__grafo.weight_edges_E(arrayBancos[i]["nombre"], arrayBancos[j]["nombre"])
                        
            
            self.__matrizDistancias = matrizDistancias
            self.__matrizRecorridos = matrizRecorridos
        
    def BFS(self):
        visitados = [False] * len(self.__ndao.to_dic())
        Inicio = 0
        lista = []
        lista.append(Inicio)
        visitados[Inicio] = True
        i = 0
        while i < len(lista):
            nodoActual = lista[i]
            listaAdy = self.__grafo.adjacent(nodoActual)
            listaAdy = listaAdy.toArray
            for j in range(0, len(listaAdy)):
                destinoId = listaAdy[j]._destination
                if not visitados[destinoId]:
                    visitados[destinoId] = True
                    lista.append(destinoId)
            i += 1
        
        for i in range(0, len(visitados)):
            if not visitados[i]:
                print("No se ha visitado el nodo: ", i)
                return False
        
        return True 
    
    
 
    
    
    def Floyd(self, origen, destino):
        self.crearMatrices()
        arrayBancos = self.__ndao.to_dic()
              
        for k in range(len(arrayBancos)):
            for i in range(len(arrayBancos)):
                for j in range(len(arrayBancos)):
                    if float(self.__matrizDistancias[i][j]) > float(self.__matrizDistancias[i][k]) + float(self.__matrizDistancias[k][j]):
                        self.__matrizDistancias[i][j] = round(float(self.__matrizDistancias[i][k] + self.__matrizDistancias[k][j]),3)
                        self.__matrizRecorridos[i][j] = self.__matrizRecorridos[i][k]
                        
        #encontrar camino
        camino = []
        origenid = int(origen)-1
        destinoid = int(destino)-1
        bancoDestino = arrayBancos[destinoid]["nombre"] 
        banco = arrayBancos[origenid]["nombre"]
        camino.append(str(banco) + " --> ")
        
        while banco != bancoDestino:
            banco = self.__matrizRecorridos[origenid][destinoid]
            
            if banco == bancoDestino:
                camino.append(str(banco))
            else:
               camino.append(str(banco) + " --> ")
               
            origenid = self.__grafo.getVertex(banco)   
    
        
        return "".join(camino)
       
            
        