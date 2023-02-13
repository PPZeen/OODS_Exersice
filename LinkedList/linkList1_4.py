class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class TextEditor:
    def __init__(self):
        self.head = Node('|')
        
    def __str__(self):
        ans = []
        t = self.head
        while t != None:
            ans.append(t.value)
            t = t.next
        return ' '.join(ans)

    def insert(self, pos, item):
        p = Node(item)
        if pos == 0:
            if self.head == None:
                self.head = p
            else:
                t = self.head
                self.head = p
                p.next = t
        elif pos <= self.size() and pos > 0:
            count = 0
            t =  self.head
            while count < pos:
                b = t
                t = t.next
                count += 1
            b.next = p
            p.next = t
   
    def pop(self, pos):
        if pos == 0:
            t = self.head.next
            if t != None: self.head = t
        elif pos < self.size() and pos > 0:
            count = 0
            t =  self.head
            while count < pos:
                p = t
                t = t.next
                count += 1
            p.next = t.next
    
    def size(self):
        count = 0
        t = self.head
        while t != None:
            count += 1
            t = t.next
        return count
    
    def index(self):
        count = 0
        t = self.head
        while t.value != '|':
            count += 1
            t = t.next
        return count

    def isEmpty(self):
        return self.head == None

    def word(self, item):
        pos = self.index()
        self.insert(pos, item)

    def left(self):
        pos = self.index()
        if pos > 0 :
            self.pop(pos)
            self.insert(pos-1, '|')
    
    def right(self):
        pos = self.index()
        if pos < self.size() - 1:
            self.pop(pos)
            self.insert(pos+1, '|')
    
    def back(self):
        pos = self.index()
        if pos > 0 : self.pop(pos-1)

    def delete(self):
        pos = self.index()
        if pos < self.size()-1 : self.pop(pos+1)
    
T = TextEditor()
orders = input('Enter Input : ').split(',')

for order in orders:
    inp = order[0]
    value = order[2::]
    
    if inp == 'I': T.word(value)
    elif inp == 'L': T.left()
    elif inp == 'R': T.right()
    elif inp == 'B': T.back()
    elif inp == 'D': T.delete()
print(T)