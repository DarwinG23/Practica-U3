import sys
sys.path.append('../')
from controls.calculos import calculos
from controls.tdaArray import TDAArray
from controls.tda.linked.linkedList import Linked_List
from controls.tda.linked.node import Node
from controls.personaDaoControl import PersonaDaoControl
from controls.censoDaoControl import CensoDaoControl
from controls.tda.stack.stack import Stack
from controls.tda.queque.queque import QueQue
import random
from controls.tda.graph.graphManaged import GraphManaged
from controls.tda.graph.graphNoManeged import GraphNoManaged
from controls.tda.graph.graphManagedLabelled import GraphManagedLebelled
from controls.tda.graph.graphNoManegedLabelled import GraphNoManegedLabelled
from controls.tda.graph.graphManagedLabelledDos import GraphManagedLabelledDos
from controls.tda.graph.graphNoManagedLabelledDos import GraphNoManagedLabelledDos
from controls.tda.tree.treeNumber import TreeNumber
from controls.tda.tree.jug.modelo.node import Node as JugNode
from controls.tda.tree.jug.modelo.rules import Rules

from controls.tda.tree.jug.modelo.jugtree import Jugtree
from controls.tda.tree.jug.modelo.node import Node


pc = PersonaDaoControl()
cd = CensoDaoControl()
stack = Stack(4)
queque = QueQue(6)

# try:
#     #graphD = GraphManaged(15)
#     #graphD = GraphNoManaged(15)
#     #graphD = GraphManagedLebelled(5)
#     #graphD = GraphNoManegedLabelled(5)
#     #graphD = graphManagedLabelledDos(5)
#     # listaPersonas = pc._list()
#     # graphL = GraphNoManagedLabelledDos(5)
#     aux = "100,70,130,50,50,80,110,150,45,60,75,85,105,115,145,155, 20"
#     nodesData = aux.split(",")
#     tree = TreeNumber()
#     for data in nodesData:
#         tree.insert(int(data))
    
#     print(tree.getNroNodes)
#     print(tree.getHeight)
    
    
    
# except Exception as error:
    # print("Errores")
    # print(error)
    
node = JugNode()
node.set_current_capacity(0, 0)


nodeF = JugNode()
nodeF.set_current_capacity(4, 3)

JugTree = Jugtree(node, nodeF)
result = JugTree.search()   

if result != None:
    print(JugTree.route(result))    
    print("Lo logre " + str(result))

else:
    print("No hay nada")    


    

