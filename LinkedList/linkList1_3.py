class Node:
    def __init__(self, value, next = None):
        self.value = value
        if next == None:
            self.next = None
        else:
            self.next = next
    def __str__(self):
        return self.value
    
class LinkList:
    def __init__(self, dataset = None):
        if dataset == None or dataset == ['']:
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
        return f"{' '.join(ans)}"
    
    def shift(self):
        if self.head != None:
            t = self.head
            self.head = self.head.next
            return t.value
        return None
    
    def insert(self, pos, item):
        p = Node(item)
        t = self.head
        
        if pos == 0:
            self.head = p
            if t != None: p.next = t
        else:
            count = 0
            while count < pos:
                count += 1
                b = t
                t = t.next
                if count == self.size(): break
            b.next = p
            p.next = t
    
    def revers(self):
        t = self.head
        size = self.size()
        for i in range(size-1):
            self.insert(size-i-1, self.shift())
            
    def size(self):
        count = 0
        t = self.head
        while t != None:
            count += 1
            t = t.next
        return count
    
    def isEmpty(self):
        return self.head == None
    
def Merge(L1, L2):
    L2.revers()
    t = L1.head
    while t != None:
        b = t
        t = t.next
    b.next = L2.head
    return L1
    
l1, l2 = input("Enter Input (L1,L2) : ").split()
L1 = LinkList(l1.split('->'))
L2 = LinkList(l2.split('->'))
print(f"L1    : {L1}")
print(f"L2    : {L2}")
print(f"Merge : {Merge(L1, L2)}")