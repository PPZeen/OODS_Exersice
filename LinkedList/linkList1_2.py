class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = self.tail = p
            
        else:
            t = self.head
            while t.next != None:
                t = t.next
            p.previous = t
            self.tail = t.next = p
               
    def addHead(self, item):
        self.insert(0, item)

    def insert(self, pos, item):
        p = Node(item)
        if pos < 0: pos = self.size() + pos 
        if pos <= 0:
            if self.size() != 0: 
                t = self.head
                self.head = p
                self.head.next = t
                t.previous = self.head
            else:
                self.head = self.tail = p
        elif pos >= self.size(): self.append(item)
        else:
            count = 0
            t = self.head
            while count < pos:
                count += 1
                i = t
                t = t.next
            i.next = p
            p.previous = i
            p.next = t
            t.previous = p
            
    def search(self, item):
        t = self.head
        while t != None:
            if t.value == item:
                return "Found"
            t = t.next
        return "Not Found"
    
    def index(self, item):
        count = 0
        t = self.head
        while t != None:
            if t.value == item:
                return count
            count += 1
            t = t.next
        return -1

    def size(self):
        count = 0
        t = self.head
        while t != None:
            count += 1
            t = t.next
        return count

    def pop(self, pos):
        if pos < 0 or pos > (self.size()-1):
            return "Out of Range"
        if pos == 0:
            self.head = self.head.next
        else:  
            count = 0
            t = self.head
            while count < pos:
                count += 1
                p = t
                t = t.next
            if t != None:
                p.next = t.next
                t.previous = p
            else:
                self.tail = p.previous        
        return "Success"
    
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())