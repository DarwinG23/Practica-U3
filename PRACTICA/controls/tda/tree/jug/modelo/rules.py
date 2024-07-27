from controls.tda.linked.linkedList import Linked_List
from controls.tda.tree.jug.modelo.node import Node

class Rules():
    
    
    def rules(self, jb, jl):
        x = jb._current_capacity
        y = jl._current_capacity
        rules = Linked_List()
        
        print("#######################")
        print("jb: ", jb)
        print("jl: ", jl)
        print("x: ", x)
        print("y: ", y)
        print("jb: ", jb._capacity)
        print("jl: ", jl._capacity)
        
        #R1: Llenar la jarra de 4 litros completamente (Para ellos debe tener algo de liquido)
        if x < jb._capacity:
            print("Aplico regla 1")
            node = Node()
            node.set_current_capacity(jb._capacity, y)
            print("node: ", node)
            rules.addNode(node)
            
        if y < jl._capacity:
            print("Aplico regla 2")
            node = Node()
            node.set_current_capacity(x, jl._capacity)
            print("node: ", node)
            rules.addNode(node)
        
        #Vaciar jarra grande
        if x > 0:
            print("Aplico regla 3")
            node = Node()
            node.set_current_capacity(0, y)
            rules.addNode(node)
        
        #Vaciar jarra peque
        if y > 0:
            print("Aplico regla 4")
            node = Node()
            node.set_current_capacity(x, 0)
            rules.addNode(node)
            
        
        #Llenar la jarra grande con la pequeña
        if (x+y) >= jb._capacity and (x < jb._capacity and y >0):
            print("Aplico regla 5")
            node = Node()
            node.set_current_capacity(jb._capacity, y-(jb._capacity-x))
            rules.addNode(node)
        
        #Llenar la jarra pequeña con la grande
        if (x+y) >= jl._capacity and (y < jl._capacity and x >0):
            print("Aplico regla 6")
            node = Node()
            node.set_current_capacity(x-(jl._capacity-y), jl._capacity)
            rules.addNode(node)
            
        #Vaciar jarra grande en la pequeña
        if (x+y) >= jl._capacity and  x > 0:
            print("Aplico regla 7")
            node = Node()
            node.set_current_capacity(0, (x+y))
            rules.addNode(node)
        
        #Vaciar jarra pequeña en la grande
        if (x+y) >= jb._capacity and y > 0:
            print("Aplico regla 8")
            node = Node()
            node.set_current_capacity((x+y), 0)
            rules.addNode(node)
            
        return rules
            