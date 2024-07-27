from controls.tda.graph.graphNoManeged import GraphNoManaged
from controls.exception.arrayPositionException import ArrayPositionException

class GraphNoManegedLabelled(GraphNoManaged):
    
    def __init__(self, directed=False):
        super().__init__(directed)
        self._lebelled = [None] * self.num_vertex
        
    @property
    def _lebelled(self):
        return self.__lebelled

    @_lebelled.setter
    def _lebelled(self, value):
        self.__lebelled = value

    def getLabel(self, v):
        if v <= self.num_vertex:
            return self.__lebelled[v]
        else:
            raise ArrayPositionException("Delimite out - 2")
        
    def getId(self, label):
        if label in self.__lebelled:
            return self.__lebelled.index(label)
        else:
            raise ArrayPositionException("El label no existe")
   
    def addLabel(self, v, objeto):
        if v <= self.num_vertex:
            self.__lebelled[v] = objeto
        else:
            raise ArrayPositionException("Delimite out - 1")
        
    def add_edge_label(self, objUno, objDos, wieght):
        v1 = self.getId(objUno)
        v2 = self.getId(objDos)
        self.insert_edges_weight(v1, v2, wieght)

   