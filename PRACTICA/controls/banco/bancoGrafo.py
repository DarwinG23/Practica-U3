from controls.banco.bancoControl import BancoControl
from controls.tda.graph.graphNoManagedLabelledDos import GraphNoManagedLabelledDos
import os, re, json
from controls.tda.graph.adjacent import Adjacent
from controls.banco.distancia import Distancia
from controls.tda.linked.linkedList import Linked_List
from controls.tda.queque.queque import QueQue

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
                    origenAdy = self.__ndao._list().binary_search_models_id(dic["from"], "_id")
                    destinoAdy = self.__ndao._list().binary_search_models_id(dic["to"], "_id")
        
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
        
    def BFS(self):
        visitados = Linked_List()
        for i in range(0, len(self.__ndao.to_dic())): 
            visitados.addNode(False)
        Inicio = 0
        

        lista = Linked_List()
        lista.addNode(Inicio)
        visitados.get(Inicio)._data = True
        i = 0

        while i < lista._length:
            nodoActual = lista.get(i)._data
            listaAdy = self.__grafo.adjacent(nodoActual)
            for j in range(0, listaAdy._length):
                destinoId = listaAdy.getNode(j)._destination
                if not visitados.get(destinoId)._data:
                    visitados.get(destinoId)._data = True
                    lista.addLast(destinoId)
            i += 1

        for i in range(0, visitados._length):
            if not visitados.get(i)._data:
                print("No se ha visitado el nodo: ", i)
                return False
        
        return True 
        
    def crearMatrices(self):
        if self.__grafo is not None:
            arrayElementos = self.__ndao.to_dic()
            
            matrizDistancias = Linked_List()
            matrizRecorridos = Linked_List()

            for i in range(len(arrayElementos)):
                filaDistancias = Linked_List()
                filaRecorridos = Linked_List()
                for j in range(len(arrayElementos)):
                    filaDistancias.addNode("INF")
                    filaRecorridos.addNode("-----")
                matrizDistancias.addNode(filaDistancias)
                matrizRecorridos.addNode(filaRecorridos)
                
            
            for i in range(len(arrayElementos)):
                for j in range(len(arrayElementos)):
                    if i == j:
                        matrizDistancias.getNode(i).get(j)._data = 0
                        matrizRecorridos.getNode(i).get(j)._data = "-----"
                    else:
                        matrizRecorridos.getNode(i).get(j)._data = arrayElementos[j]["nombre"]
                    if self.__grafo.exist_edge_E(arrayElementos[i]["nombre"], arrayElementos[j]["nombre"]):
                        matrizDistancias.getNode(i).get(j)._data = self.__grafo.weight_edges_E(arrayElementos[i]["nombre"], arrayElementos[j]["nombre"])
                        
            
            self.__matrizDistancias = matrizDistancias
            self.__matrizRecorridos = matrizRecorridos
            
    
    def floyd(self, origen, destino):
        self.crearMatrices()
        dicElementos = self.__ndao.to_dic()
              
        for k in range(len(dicElementos)):
            for i in range(len(dicElementos)):
                for j in range(len(dicElementos)):
                    if float(self.__matrizDistancias.getNode(i).get(j)._data) > float(self.__matrizDistancias.getNode(i).get(k)._data) + float(self.__matrizDistancias.getNode(k).get(j)._data):
                        self.__matrizDistancias.getNode(i).get(j)._data = round(float(self.__matrizDistancias.getNode(i).get(k)._data + self.__matrizDistancias.getNode(k).get(j)._data),3)
                        self.__matrizRecorridos.getNode(i).get(j)._data = self.__matrizRecorridos.getNode(i).get(k)._data
                        
        
        camino = "La ruta mas corta es: "
        origenid = int(origen)-1
        destinoid = int(destino)-1
        elementoDestino = dicElementos[destinoid]["nombre"] 
        elemento = dicElementos[origenid]["nombre"]
        camino = camino + str(elemento) + " --> "
        while elemento != elementoDestino:
            
            elemento = self.__matrizRecorridos.getNode(origenid).get(destinoid)._data
            
            if elemento == elementoDestino:
                camino += str(elemento)
            else:
               camino += str(elemento) + " --> "
               
            origenid = self.__grafo.getVertex(elemento)   
         
        return "".join(camino) + "  |Con una distancia de: " + str(self.__matrizDistancias.getNode(int(origen)-1).get(int(destino)-1)._data) 
    
    
    def dijkstra(self, origen, destino):
        distancias = Linked_List()
        no_visitados = Linked_List()
        predecesores = Linked_List()
        destinoId = int(destino)-1
        destinoEtiqueta = self.__ndao.to_dic()[int(destino)-1]["nombre"]
        origenEtiqueta = self.__ndao.to_dic()[int(origen)-1]["nombre"]    
        
        #Inicializar listas
        for i in range(0, len(self.__ndao.to_dic())):
            distancias.addLast(float("inf"))
            no_visitados.addLast(self.__ndao.to_dic()[i]["nombre"])
            predecesores.addLast(None)
        
        distancias.get(int(origen)-1)._data = 0
        

        origen = int(origen)-1
        while no_visitados._length > 0:
            etiquetaActual = self.__grafo.getLabel(int(origen))
            adyacentes = self.__grafo.adjacent_E(etiquetaActual)
            
            for i in range(0, no_visitados._length):
                if etiquetaActual == no_visitados.get(i)._data:
                    for i in range(0, adyacentes._length):
                        vecino = adyacentes.getNode(i)._destination
                        etiquetaVecino = self.__grafo.getLabel(vecino)
                        existe = False
                        for j in range(0, no_visitados._length):
                            if no_visitados.get(j)._data == etiquetaVecino:
                                existe = True
                                break
                        
                        if existe:
                            origen_id = int(origen) 
                            vecino_id = int(vecino)
                            nueva_distancia = distancias.get(origen_id)._data + adyacentes.getNode(i)._weight

                            if distancias.get(vecino_id)._data > nueva_distancia:
                                distancias.get(vecino_id)._data = nueva_distancia
                                predecesores.get(vecino_id)._data = etiquetaActual
                    else:
                        continue
    
            

            origen = self.__grafo.getVertex(etiquetaActual)
            no_visitados.print
            
            for i in range (0, no_visitados._length):
                if etiquetaActual == no_visitados.get(i)._data:
                    no_visitados.delete(i)
                    break

                

            next_nodo_dist_min = None
            min = float("inf")
            for i in range(0, no_visitados._length):
                nodoEtiqueta = no_visitados.get(i)._data
                nodo = self.__grafo.getVertex(nodoEtiqueta)
                dist = distancias.get(nodo)._data
                if dist < min:
                    min = dist
                    next_nodo_dist_min = nodo
                    etiquetaMin = no_visitados.get(i)._data
                    
                    


            origen = next_nodo_dist_min

            
        



        listaCamino = Linked_List()
        listaCamino.addFirst(destinoEtiqueta)
        predecesores.print
        while destinoEtiqueta != origenEtiqueta:
            id = self.__grafo.getVertex(destinoEtiqueta)
            destinoEtiqueta = predecesores.get(id)._data
            listaCamino.addFirst(destinoEtiqueta)
            
        camino = "La ruta mas corta es: "
        for i in range(0, listaCamino._length):
            camino += listaCamino.getNode(i)
            if i < listaCamino._length - 1:
                camino += " --> "
            
        
                
        return "".join(camino) + "  |Con una distancia de: " + str(round(float(distancias.get(int(destinoId))._data),3))
       
  
            
        