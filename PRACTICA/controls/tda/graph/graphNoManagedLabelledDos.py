from controls.tda.graph.graphNoManeged import  GraphNoManaged
from controls.exception.arrayPositionException import ArrayPositionException
from math import nan


class GraphNoManagedLabelledDos(GraphNoManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        self.__labels = []
        self.__labelsVertex={}
        for i in range(0, self.num_vertex):
            self.__labels.append(None)
            
    @property
    def getListAdjacent(self):
        return self.__listAdjacent
        
    def getVertex(self, label):
        try:
            return self.__labelsVertex[str(label)]
        except Exception as error:
            return -1    
    
    def label_vertex(self, v, label):
        self.__labels[v] = label
        self.__labelsVertex[str(label)] = v
        
    def getLabel(self, v):
        return self.__labels[v]
    
    def exist_edge_E(self, label1, label2):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            return self.exist_edges(v1, v2)
        else:
            return False
        
    def insert_edges_weight_E(self, label1, label2, weight): #sirve para insertar aristas con peso
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            self.insert_edges_weight(v1, v2, weight)
        else:
            raise ArrayPositionException("Vertex not found") 
        
    def insert_edges_E(self, label1, label2): #sirve para insertar aristas
        self.insert_edges_weight_E(label1, label2, nan)
    
    def weight_edges_E(self, label1, label2): #sirve para obtener el peso de las aristas
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            return self.weight_edges(v1, v2)
        else:
            raise ArrayPositionException("Vertex not found") 
        
    def adjacent_E(self, label1): #sirve para obtener los vertices adyacentes
        v1 = self.getVertex(label1)
        if v1 != -1:
            return self.adjacent(v1)
        else:
            raise ArrayPositionException("Vertex not found")
        
    
    @property
    def serializar(self):
        adyacencias = []
        for i in range(0, len(self.__labels)):  
            for j in range(0, self.adjacent_E(self.__labels[i])._length):
                dic = {}
                dic["from"] = i+1
                dic["to"] = self.adjacent(i).getNode(j)._destination + 1
                adyacencias.append(dic)
                
        return {
            "vertices": self.num_vertex,
            "aristas": self.num_edges,
            "etiquetas": self.__labels,
            "etiquetasVertice": self.__labelsVertex,
            "adyacencias": adyacencias
        }
       
    @classmethod 
    def deserializar(self, dic):
        graph = GraphNoManagedLabelledDos(int(dic["vertices"]))
        graph.__labelsVertex = dic["etiquetasVertice"]
        graph.__labels = dic["etiquetas"]
        graph.__listAdjacent = dic["adyacencias"]
        graph.__numEdg = dic["aristas"]
        return graph