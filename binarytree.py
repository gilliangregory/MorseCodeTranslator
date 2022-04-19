#please type "pip install binarytree" into the command line to install
#binarytree package from python
from binarytree import Node
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

rooty = Node("START")

#first level of tree
rooty.left  = Node("E")
rooty.right = Node("T")

#second level of tree
rooty.left.left   = Node("I")
rooty.left.right  = Node("A")
rooty.right.left  = Node("N")
rooty.right.right = Node("M")

#third level of tree
rooty.left.left.left    = Node("S")
rooty.left.left.right   = Node("U")
rooty.left.right.left   = Node("R")
rooty.left.right.right  = Node("W")
rooty.right.left.left   = Node("D")
rooty.right.left.right  = Node("K")
rooty.right.right.left  = Node("G")
rooty.right.right.right = Node("O")

#fourth level of tree
rooty.left.left.left.left    = Node("H")
rooty.left.left.left.right   = Node("V")
rooty.left.left.right.left   = Node("F")
rooty.left.right.left.left   = Node("L")
rooty.left.right.right.left  = Node("P")
rooty.left.right.right.right = Node("J")
rooty.right.left.left.left   = Node("B")
rooty.right.left.left.right  = Node("X")
rooty.right.left.right.left  = Node("C")
rooty.right.left.right.right = Node("Y")
rooty.right.right.left.left  = Node("Z")
rooty.right.right.left.right = Node("Q")

def preorder(rooty):
    if rooty:
        print(rooty.val), #prints data of node
        preorder(rooty.left) 
        preorder(rooty.right)

def inorder(rooty):
    if rooty:
        inorder(rooty.left)
        print(rooty.val),
        inorder(rooty.right)


