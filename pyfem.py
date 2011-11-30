from time import sleep

class Node:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
    
    def __str__(self):
        return "%s: (%s, %s)" % str(self.num), str(self.x), str(self.y)

class Element:
    def __init__(self, num, p1, p2, p3):
        self.num = num
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        return "%s: (%s, %s, %s)" % str(self.num), str(self.p1), str(self.p2), str(self.p3)

def read_mesh(filename):
    f = open(filename, 'r')

    line = f.readline()
    line = f.readline()

    while line.find("$Nodes") == -1:
        line = f.readline()

    line = f.readline()
    line = f.readline()

    nodeList = []
    while line.find("$EndNodes") == -1:
        s = [float(i) for i in line.split()]
        nodeList.append(Node(s[0], s[1], s[2]))
        line = f.readline()

    line = f.readline() 
    line = f.readline()
    line = f.readline()

    elemList = []
    while line.find("$EndElements") == -1:
        s = [int(i) for i in line.split()]
        print s
        elemList.append(Element(s[0], s[5], s[6], s[7]))
        line = f.readline()
        print line
        
    return nodeList, elemList        


if __name__ == "__main__":
    read_mesh("mesh/untitled.msh")
