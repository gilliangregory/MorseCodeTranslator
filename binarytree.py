
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

tree = Node("START")

#first level of tree
tree.left  = Node("E")
tree.right = Node("T")

#second level of tree
tree.left.left   = Node("I")
tree.left.right  = Node("A")
tree.right.left  = Node("N")
tree.right.right = Node("M")

#third level of tree
tree.left.left.left    = Node("S")
tree.left.left.right   = Node("U")
tree.left.right.left   = Node("R")
tree.left.right.right  = Node("W")
tree.right.left.left   = Node("D")
tree.right.left.right  = Node("K")
tree.right.right.left  = Node("G")
tree.right.right.right = Node("O")

#fourth level of tree
tree.left.left.left.left    = Node("H")
tree.left.left.left.right   = Node("V")
tree.left.left.right.left   = Node("F")
tree.left.right.left.left   = Node("L")
tree.left.right.right.left  = Node("P")
tree.left.right.right.right = Node("J")
tree.right.left.left.left   = Node("B")
tree.right.left.left.right  = Node("X")
tree.right.left.right.left  = Node("C")
tree.right.left.right.right = Node("Y")
tree.right.right.left.left  = Node("Z")
tree.right.right.left.right = Node("Q")

def preorder(tree):
    if tree:
        print(tree.val), #prints data of node
        preorder(tree.left) 
        preorder(tree.right)

def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.val),
        inorder(tree.right)
        

