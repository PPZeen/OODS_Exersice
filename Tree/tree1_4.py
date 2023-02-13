class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        node = Node(val)
        if self.root == None : self.root = node
        else:
            p = None
            r = self.root
            while r != None :
                if r.data > val :
                    p = r
                    r = r.left
                elif r.data < val :
                    p = r
                    r = r.right
            if p.data > val : p.left = node
            else : p.right = node
    
    def delete(self, r, data):
        self.root = BinarySearchTree._deleteNode(r, data)
    
    def _deleteNode(root, data):
        if root is None:
            print("Error! Not Found DATA")
            return root
        if data < root.data:
            root.left = BinarySearchTree._deleteNode(root.left, data)
            return root
        elif data > root.data :
            root.right = BinarySearchTree._deleteNode(root.right, data)
            return root
        if root.left is None and root.right is None:
            return None
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        sP = root
        s = root.right
        while s.left != None:
            sP = s
            s = s.left
        if sP != root: sP.left = s.right
        else: sP.right = s.right
        root.data = s.data
        return root
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for e in data:
    if e[0] == 'i': print(f"insert {int(e[2::])}"); tree.insert(int(e[2::]))
    elif e[0] == 'd': print(f"delete {int(e[2::])}"); tree.delete(tree.root, int(e[2::]))
    printTree90(tree.root)