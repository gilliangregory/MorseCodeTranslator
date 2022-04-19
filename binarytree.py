class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

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
rooty.left.left.left.left     = Node("H")
rooty.left.left.left.right    = Node("V")
rooty.left.left.right.left    = Node("F")
rooty.left.right.left.left    = Node("L")
rooty.left.right.right.left   = Node("P")
rooty.left.right.right.right  = Node("J")
rooty.right.left.left.left    = Node("B")
rooty.right.left.left.right   = Node("X")
rooty.right.left.right.left   = Node("C")
rooty.right.left.right.right  = Node("Y")
rooty.right.right.left.left   = Node("Z")
rooty.right.right.left.right  = Node("Q")


def preorder(rooty):
    if rooty:
        print(rooty.val), #prints data of node
        preorder(rooty.left) 
        preorder(rooty.right)

def tomorse(rooty, char, dotty):
    if rooty == None:
        return False
    elif rooty.val == char:
        return True
    else:
        if tomorse(rooty.left, char, dotty)==True:
            dotty.insert(0,".")
            return True
        elif tomorse(rooty.right, char, dotty)==True:
            dotty.insert(0,"-")
            return True

# Code copied from function drawtree obtained from https://gist.github.com/Liwink/b81e726ad89df8b0754a3a1d0c40d0b4
def drawtree(rooty):
    def height(rooty):
        return 1 + max(height(rooty.left), height(rooty.right)) if rooty else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(rooty)
    jumpto(0,20*h)
    draw(rooty, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()

if __name__ == '__main__':
    drawtree(rooty)


