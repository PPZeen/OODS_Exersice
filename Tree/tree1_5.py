class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop(-1) 
        
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
    def preOrder(self):
        BST._preOrder(self.root)
    def _preOrder(root):
        if root is not None:
            print(root, end= '')
            BST._preOrder(root.left)
            BST._preOrder(root.right)
    def inOrder(self):
        BST._inOrder(self.root)
    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.left)
            print(root, end= '')
            BST._inOrder(root.right)
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
def post2In(s):
    S = Stack()
    for e in s:
        if e in "+-*/":
            r = S.pop()
            l = S.pop()
            S.push(f"({l}{e}{r})")
        else: S.push(e)
    return S.pop()
    
inp = input("Enter Postfix : ")
S = Stack()
for e in inp:
    node = Node(e)
    if e in "+-*/":
        node.right = S.pop()
        node.left = S.pop()
        S.push(node)
    else:
        S.push(node)
        
B = BST()
B.root = S.pop()
print("Tree :"); B.printTree(B.root)
print("--------------------------------------------------")
print(f"Infix : {post2In(inp)}")
print("Prefix : ", end=''); B.preOrder()