class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        node = Node(data)
        if self.root == None : self.root = node
        else:
            p = None
            r = self.root
            while r != None :
                if r.data > data :
                    p = r
                    r = r.left
                elif r.data < data :
                    p = r
                    r = r.right
            if p.data > data : p.left = node
            else : p.right = node
            
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)
    
T.printTree(T.root)         
                       