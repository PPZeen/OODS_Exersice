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
        self.items = []

    def insert(self, data):
        node = Node(data)
        self.items.append(data)
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
            if p.data > data :
                p.left = node
            else : p.right = node
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def rank(self, n):
        items = sorted(self.items)
        if n < items[0]: return 0
        for i in items:
            if n < i: return items.index(i)
        return len(items)
            

T = BST()
order, rank = input('Enter Input : ').split('/')
order = [int(i) for i in order.split()]
for i in order: T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------") 
print(f"Rank of {rank} : {T.rank(int(rank))}")