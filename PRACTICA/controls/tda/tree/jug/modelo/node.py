from controls.tda.tree.jug.modelo.jug import Jug
from controls.tda.linked.linkedList import Linked_List

class Node():
    def __init__(self) -> None:
        self.__jb = Jug()
        self.__jl = Jug()
        self.__father = None
        self.__succesors = Linked_List()
        self.__jb._capacity = 4
        self.__jb._current_capacity = 0
        self.__jl._capacity = 3
        self.__jl._current_capacity = 0
        

    @property
    def _jb(self):
        return self.__jb

    @_jb.setter
    def _jb(self, value):
        self.__jb = value

    @property
    def _jl(self):
        return self.__jl

    @_jl.setter
    def _jl(self, value):
        self.__jl = value

    @property
    def _father(self):
        return self.__father

    @_father.setter
    def _father(self, value):
        self.__father = value

    @property
    def _succesors(self):
        return self.__succesors

    @_succesors.setter
    def _succesors(self, value):
        self.__succesors = value

        
    def set_current_capacity(self, ccjb, ccjl):
        self.__jb._current_capacity = ccjb
        self.__jl._current_capacity = ccjl
        

       
    def addSuccesor(self, rules):
        self.__succesors = Linked_List()
        for i in range(0, rules._length):
           aux = rules.getNode(i)
           aux._father = self
           self.__succesors.addNode(aux, self.__succesors._length)
       
        
        
    
    def __str__(self) -> str:
        return str(self._jb) + " : " + str(self._jl) 