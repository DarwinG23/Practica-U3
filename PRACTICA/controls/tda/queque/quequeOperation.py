from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedEmpty import LinkedEmpty

class QuequeOperation(Linked_List):
    def __init__(self, top):
        super().__init__()
        self.__top = top

    @property
    def _top(self):
        return self.__top

    @_top.setter
    def _top(self, value):
        self.__top = value

    @property
    def verifyTop(self):
        return self._length < self.__top
    
    def queque(self, data):
        if self.verifyTop:
            self.addNode(data, self._length)
        else:
            raise LinkedEmpty("QueQue is Full")
        
    @property
    def dequeque(self):
        if self.isEmpty:
            raise LinkedEmpty("Queque is Empty")
        else:
            return self.delete(0)
        
    def extraer_min(self):
        if self.isEmpty:
            raise LinkedEmpty("Queque is Empty")
        else:
            #encuentra el minimo de la cola 
            min = self._head._data
            pos = 0
            for i in range(1, self._length):
                if min > self.getNode(i):
                    min = self.getNode(i)
                    pos = i
            return self.delete(pos)
        
    
