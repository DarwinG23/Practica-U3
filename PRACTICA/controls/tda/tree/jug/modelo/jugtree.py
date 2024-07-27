from controls.tda.tree.jug.modelo.node import Node
from controls.tda.linked.linkedList import Linked_List
from controls.tda.tree.jug.modelo.rules import Rules

class Jugtree():
    def __init__(self, first, last) -> None:
        self.__state_first = first
        self.__state_final = last  
        self.__nodes = Linked_List()
        self.__list_nodes = Linked_List()
        
    
    def isNodeSearch(self, na, ns):
        # print("##################################3")
        # print(na._jb._current_capacity)
        # print(ns._jb._current_capacity)
        # print(na._jl._current_capacity)
        # print(ns._jl._current_capacity)
        return (na._jb._current_capacity == ns._jb._current_capacity) and (na._jl._current_capacity == ns._jl._current_capacity)
        
    
    
    #Busqueda en anchura    
    def search(self):
        try:   
            if self.isNodeSearch(self.__state_first, self.__state_final):
                self.__nodes.addNode(self.__state_final, self.__nodes._length)
            else:
                self.__nodes = Linked_List()
                self.__list_nodes = Linked_List()
                self.__list_nodes.addNode(self.__state_first, self.__nodes._length)
                while self.__list_nodes._length > 0:
                    current = self.__list_nodes.delete()
                    print("current: ", current)
                    if self.isNodeSearch(current, self.__state_final):
                        return current
                    else:
                        print("current jb: ", current._jb)
                        print("current jl: ", current._jl)
                        print("current jb capacity : ", current._jb._capacity)
                        print("current jl capacity : ", current._jl._capacity)
                        ar = Rules()
                        rules  = ar.rules(current._jb, current._jl)
                        current.addSuccesor(rules)
                        print("#######################")
                        print("rules: ", rules._length) 
                        for i in range(0, rules._length):
                            auxR = rules.getNode(i)
                            print("i: ", i)
                            print("auxR: ",auxR)
                            print("state__first: ", self.__state_first) 
                            print("state_final: ", self.__state_final)
                            self.__list_nodes.addNode(auxR, self.__list_nodes._length)
                            self.__nodes.addNode(auxR, self.__list_nodes._length)
                            
                            if self.isNodeSearch(auxR, self.__state_final):
                                print("entro")
                                print(type(auxR))
                                return auxR
                            
        except Exception as error:
            print("errores")
            print(error) 
        return None
    
    
    def deleteRules(self, rules):
        list = Linked_List()
        if not rules.isEmpty and not self.__nodes.isEmpty:
            rulesA = rules.toArray
            nodesA = self.__nodes.toArray
            for i in range(0, len(rulesA)):
                nad = True
                for j in range(0, len(nodesA)):
                    if self.isNodeSearch(rulesA[i], nodesA[j]):
                        nad = False
                        break
                if nad:
                    list.add(rulesA[i])
        return list
            
        
    
    def route(self, node):
        routes = Linked_List()
        while node != None:
            routes.add(node, routes._length)
            node = node._father
        
        return routes
        