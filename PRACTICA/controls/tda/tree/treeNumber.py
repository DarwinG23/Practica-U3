from controls.tda.linked.linkedList import Linked_List
from controls.tda.tree.node import Node
class TreeNumber():
    def __init__(self) -> None:
        self.__root = None 
        self.__height = 0
        self.__nro_nodes = 0
        self.__levels = Linked_List()
        self.__orders = Linked_List()
    
    @property    
    def getNroNodes(self):
        return self.__nro_nodes
    
    @property    
    def getHeight(self):
        return self.__height
        
    
    def __calcHeight(self, tree):
        if tree == None:
            return 0
        else:
            left = self.__calcHeight(tree._left)
            right = self.__calcHeight(tree._right)
            if left > right:
                left += 1
                return left 
            else:
                right += 1
                return right 
            
    def __calclevels(self, tree, level):
        if tree != None:
            self.__levels.getNode(level).addNode(tree._data)   #OJO
            level += 1
            self.__calclevels(tree._left, level)   
            self.__calclevels(tree._right, level)
        else:
            self.__levels.getNode(level).addNode(tree._data)   #OJO
            level += 1
            self.__calclevels(None, level)   
            self.__calclevels(None, level)
    
    def levels(self):
        self.__levels = Linked_List()
        #TODO
        #calc levels
        self.__height = self.__calcHeight(self.__root)
        for i in range(0, self.__height):
            self.__levels.addNode(Linked_List())
        #OJO
        # self.__calclevels(self.__root, 0)
        # self.__levels.delete(self.__levels._length-1)
    
    
    def insert(self, data):
        if self.__root == None:
            self.__root = Node(data)
            self.__nro_nodes += 1
            self.levels()
            return True
        else:
            new = Node(data)
            recent = self.__root
            father = None
            while(True):
                father = recent
                if data == recent._data:
                    return False
                elif data < recent._data:
                    recent = recent._left
                    if recent == None:
                        new._father = father
                        father._left = new
                        self.__nro_nodes += 1
                        self.levels()
                        return True
                else:
                    recent = recent._right
                    if recent == None:
                        new._father = father
                        father._right = new
                        self.__nro_nodes += 1
                        self.levels()
                        return True
    
    def __pre_order(self, tree):
        if tree != None:
            self.__orders.addNode(tree, self.__ordeners._length)
            self._pre_order(tree._left)
            self._pre_order(tree._right)
            
    def pre_order(self):
        self.__ordeners = Linked_List()
        self.__pre_order(self.__root)
        return self.__orders
    
    
    def __post_order(self, tree):
        if tree != None:
            self._pre_order(tree._left)
            self._pre_order(tree._right)
            self.__orders.addNode(tree, self.__ordeners._length)
            
    def post_order(self):
        self.__ordeners = Linked_List()
        self.__post_order(self.__root)
        return self.__orders
   
    #izq raiz der
    def __in_order(self, tree):
        if tree != None:
            self._pre_order(tree._left)
            self.__orders.addNode(tree, self.__ordeners._length)
            self._pre_order(tree._right)
    
    def in_order(self):
        self.__ordeners = Linked_List()
        self.__in_order(self.__root)
        return self.__orders
    
    
              