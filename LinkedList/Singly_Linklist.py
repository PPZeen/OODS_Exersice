class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
    def __str__(self):
        return self.data

class LinkList:
    def __init__(self, dataset = None):
        if dataset in [None, ['']]:
            self.head = None
        else:
            p = Node(dataset[0])
            self.head = p
            for data in dataset[1::]:
                q = Node(data)
                p.next = p = q
        
    def __str__(self):
        if self.isEmpty(): return "List is empty"
        
        t = self.head
        ans = [str(t)]
        while t.next != None:
            ans.append(str(t.next))
            t = t.next
        return f"link list : {'->'.join(ans)}"

    def append(self, data): 
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
    
    def shift(self):
        if self.head != None:
            t = self.head
            self.head = self.head.next
            return t.data
        return None
            
    def insert(self, pos, item):
        p = Node(item)
        t = self.head
            
        if pos == 0:
            self.head = p
            if t != None: p.next = t
        elif pos > 0:
            count = 0
            while count < pos:
                count += 1
                b = t
                t = t.next
                if count == self.size(): break
            b.next = p
            p.next = t
        else: print("Data cannot be added")
    
    def pop(self, pos):
        if pos < 0 or pos > (self.size()-1): return "Out of Range"
        if pos == 0: self.head = self.head.next
        else:  
            count = 0
            t = self.head
            while count < pos:
                count += 1
                p = t
                t = t.next
                if count > self.size()-1:
                    if count == 1: self.head = None
                    else: p = None
                    break
            p.next = t.next       
    
    def revers(self):
        size = self.size()
        for i in range(size-1):
            self.insert(size-i-1, self.shift())

    def addHead(self, item): self.insert(0, item)

    def search(self, item):
        t = self.head
        while t != None:
            if t.data == item:
                return "Found"
            t = t.next
        return "Not Found"
    
    def index(self, item):
        count = 0
        t = self.head
        while t != None:
            if t.data == item:
                return count
            count += 1
            t = t.next
        return -1

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        count = 0
        p = self.head

        while p != None:
            count += 1
            p = p.next
        
        return count  

# -------------- test ----------------------
#1 Enter Input : 1 2, 0:0, 3:3
#1 link list : 1->2
#1 index = 0 and data = 0
#1 link list : 0->1->2
#1 index = 3 and data = 3
#1 link list : 0->1->2->3

#2 Enter Input : ,1:1
#2 List is empty
#2 Data cannot be added
#2 List is empty

#3 Enter Input : 0 1 2 4, -1:2, 3:3, 5:5, 0:-1
#3 link list : 0->1->2->4
#3 Data cannot be added
#3 link list : 0->1->2->4
#3 index = 3 and data = 3
#3 link list : 0->1->2->3->4
#3 index = 5 and data = 5
#3 link list : 0->1->2->3->4->5
#3 index = 0 and data = -1
#3 link list : -1->0->1->2->3->4->5

l = LinkList(['1','2','4','5']); print(l)
l.append('0'); print(l)
l.insert(-1, '3'); print(l)
l.insert(2, '3'); print(l)
l.pop(0); print(l)
l.shift(); print(l)
l.revers(); print(l)
