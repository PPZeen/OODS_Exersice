class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root: return Node(key)
        elif key < root.data: root.left = self.insert(root.left, key)
        else: root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        b = self.getBal(root)

        if b > 1 and key < root.left.data:
            print("Not Balance, Rebalance!")
            return self.rRotate(root)
        
        if b < -1 and key > root.right.data:
            print("Not Balance, Rebalance!")
            return self.lRotate(root)
        
        if b > 1 and key > root.left.data:
            print("Not Balance, Rebalance!")
            root.left = self.lRotate(root.left)
            return self.rRotate(root)
        
        if b < -1 and key < root.right.data:
            print("Not Balance, Rebalance!")
            root.right = self.rRotate(root.right)
            return self.lRotate(root)
        
        return root
        
    def lRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        
        return y

    def rRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def getHeight(self, root):
        if not root: return 0
        return root.height
    
    def getBal(self, root):
        if not root: return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in '1 6 9 4 15 12 7 18 11 13 14 2 5 3 17 28 29 25 20'.split()]
for i in inp:
    print(f"insert : {i}")
    T.root = T.insert(T.root, i)
    T.printTree(T.root)
    print("="*30)