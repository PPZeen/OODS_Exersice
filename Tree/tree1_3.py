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
        self.count = None

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
    
    def compareK(self, node, k):
        if node != None:
            if node.right != None:
                if node.right.data <= k: self.count += 1
            if node.left != None:
                if node.left.data <= k: self.count += 1
            self.compareK(node.right, k)
            self.compareK(node.left, k)    
        return self.count

T = BST()
inp, k = input('Enter Input : ').split('/')
inp = [int(i) for i in inp.split()]
for i in inp:
    T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
T.count = 1 if T.root.data <= int(k) else 0
print(T.compareK(T.root, int(k)))