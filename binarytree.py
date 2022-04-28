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
rooty.left.left.right.right   = Node("Ü")
rooty.left.right.left.right   = Node("Ä")
rooty.right.right.right.left  = Node("Ö")
rooty.right.right.right.right = Node("x")


#fifth level of tree
rooty.left.left.left.left.left      = Node("5")
rooty.left.left.left.left.right     = Node("4")
rooty.left.left.right.right.right   = Node("2")
rooty.left.left.left.right.right    = Node("3")
rooty.left.right.left.right.left    = Node("+")
rooty.left.left.right.right.left    = Node("ð")
rooty.left.right.right.left.right   = Node("À")
rooty.left.right.right.right.right  = Node("1")
rooty.right.left.left.left.left     = Node("6")
rooty.right.left.right.left.right   = Node("")
rooty.right.right.left.left.left    = Node("7")
rooty.right.right.left.left.right   = Node("")
rooty.right.right.left.right.right  = Node("Ñ")
rooty.right.right.right.left.left   = Node("8")
rooty.right.right.right.right.left  = Node("9")
rooty.right.right.right.right.right = Node("0") 

#Sixth level of tree
rooty.left.left.right.right.left.left   = Node("?")
rooty.left.right.left.right.left.right  = Node(".")
rooty.left.right.right.left.right.left  = Node("@")
rooty.right.left.left.left.left.right   = Node("-")
rooty.right.left.right.left.right.left  = Node(";")
rooty.right.right.left.left.right.right = Node(",")
rooty.right.right.right.left.left.left  = Node(":")


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
    





def toeng(morse, rooty):
    i = 0
    j =0
    englist = []
    lenny = len(englist) -1
    reallist = []
    morselist = morse.split(" ")
    tree = rooty
    stringlist = ""
    for i in range(len(morselist)):
        for j in range(len(morselist[i])):
            
            if morselist[i][j] == ".":
                if hasattr(tree, 'left'):
                    tree= tree.left
                else:
                    print("This contains a character that is not an English letter.")
                    break
            elif morselist[i][j] == "-":
                if hasattr(tree, 'right'):
                    tree= tree.right
                else:
                    print("This contains a character that is not an English letter.")
                    break
            elif morselist[i][j] == ",":
                englist.append(" ")
                break
            else:
                print("This contains a character that is not in Morse Code.")
                break
            englist.append(tree)
        if len(englist) > 0:
            reallist.append(englist[len(englist) -1])
        tree = rooty
    
    for m in range(len(reallist)):
        for n in range(len(str(reallist[m]))):
            if str(reallist[m])[n] == "(":
                stringlist += str(reallist[m])[n+1]
                #stringlist += " "
        if str(reallist[m]) == " ":
            stringlist += " "
    return stringlist


#please install winsound and turn your volume up.
#(note: winsound and this function will only work on Windows.)
#def beep(eng):
#    import winsound

 #   beeps = tomorse(eng)
 #   beeplist = list(beeps)
 #   for elem in beeplist:
 #       for char in elem:
 #           if char == ".":
 #               winsound.Beep(440, 1000)
 #           if char == "-":
 #               winsound.Beep(440, 3000)
 #           time.sleep(1)
 #       time.sleep(6)
 #   return


