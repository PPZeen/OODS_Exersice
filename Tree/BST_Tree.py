class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop(-1)
    
    def peek(self) :
        return None if self.isEmpty() else self.items[-1]
    
    def isEmpty(self) :
        return len(self.items) == 0

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
        self.count = 0
        self.items = []

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
    
    def delete(self, r, data):
        self.root = BST._deleteNode(r, data)
    
    def _deleteNode(root, data):
        
        if root is None:
            print("Error! Not Found DATA")
            return root
        
        if data < root.data:
            root.left = BST._deleteNode(root.left, data)
            return root
    
        elif data > root.data :
            root.right = BST._deleteNode(root.right, data)
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
    
        succParent = root
        succ = root.right
    
        while succ.left != None:
            succParent = succ
            succ = succ.left

        if succParent != root: succParent.left = succ.right
        else: succParent.right = succ.right

        root.data = succ.data
        return root

    def compareK(self, node, k):    # มีกี่ตัวที่มีค่า <= k
        if node != None:
            if node.right != None:
                if node.right.data <= k: self.count += 1
            if node.left != None:
                if node.left.data <= k: self.count += 1
            self.compareK(node.right, k)
            self.compareK(node.left, k)    
        return self.count
    
    def getListItems(self, node):
        self.items = [self.root.data]
        return self._listItems(node)

    
    def _listItems(self, node):    # มีกี่ตัวที่มีค่า <= k
        if node != None:
            if node.right != None:
                self.items.append(node.right.data)
            if node.left != None:
                self.items.append(node.left.data)
            self._listItems(node.right)
            self._listItems(node.left)
        
        return self.items
    
    def min(self): return min(self.getListItems(self.root))
    
    def max(self): return max(self.getListItems(self.root))

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def inOrder(self):
        BST._inOrder(self.root)
    
    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.left)
            print(root, end= '')
            BST._inOrder(root.right)

    def preOrder(self):
        BST._preOrder(self.root)
    
    def _preOrder(root):
        if root is not None:
            print(root, end= '')
            BST._preOrder(root.left)
            BST._preOrder(root.right)
    
    def postOrder(self):
        BST._postOrder(self.root)
    
    def _postOrder(root):
        if root is not None:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root, end= '')

def creatBSTwInfix(inp):
    S = Stack()
    for e in inp:
        if e == ')':
            right = S.pop()
            root = S.pop()
            left = S.pop()
            
            root.right = right
            root.left = left
            s = S.pop()
            S.push(root)
        else:
            S.push(Node(e))

    B = BST()
    B.root = S.pop()
    return B

def creatBSTwPostfix(inp):
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
    return B

def creatBSTwPrefix(inp):
    S = Stack()
    s = inp[::-1]
    for i in s:
        if i in ['+', '-', '*', '/']:
    
            a = S.pop()
            b = S.pop()
    
            temp = a+b+i
            S.push(temp)
        else: S.push(i)

    return creatBSTwPostfix(S.pop())

# T = BST()
# inp = [int(i) for i in '8 7 3 1 2 6 9'.split()]
# for i in inp: T.insert(i)

# T.printTree(T.root); print("-"*40)

# T.delete(T.root, 8); T.printTree(T.root); print("-"*40)
# T.delete(T.root, 2); T.printTree(T.root)

print(f"{'-'*20} Creat with Postfix form {'-'*20}")
T = creatBSTwPostfix("ab+cde+**")
T.printTree(T.root)

print(f"{'-'*20} Creat with Infix form {'-'*20}")
T = creatBSTwInfix("((a+b)*(c*(d+e)))")
T.printTree(T.root)

print(f"{'-'*20} Creat with Prefix form {'-'*20}")
T = creatBSTwPrefix("*+ab*c+de")
T.printTree(T.root)
