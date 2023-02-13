class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
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
        ans = []
        t = self.head
        while t != None:
            ans.append(t.value)
            t = t.next
        return ' '.join(ans)
    
    def append(self, item): 
        p = Node(item)
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
    
    def pop(self, pos):
        t = self.head
        if pos >= self.size(): return None
        elif pos == 0:
            self.head = self.head.next
        else:
            count = 0
            while count < pos:
                count += 1
                b = t
                t = t.next
            b.next = t.next
        return t.value
    
    def size(self):
        count = 0
        t = self.head
        while t != None:
            count += 1
            t = t.next
        return count
    
    def cut(self, amount):
        for i in range(amount):
            self.append(self.shift())
    
    def riffle(self, amount):
        index = 1
        count = 0
        for i in range(self.size()):
            if i >= amount:
                self.insert(index, self.pop(i))
                if count < amount:
                    index += 2
                    count += 1
                    if count == amount: index -= 1
                else : index += 1
    
    def deriffle(self, amount):
        index = 1
        for i in range(self.size() - amount):
            if index != amount:
                index = i+1 
            self.append(self.pop(index))

def createLL(LL):
    return LinkList(LL)

def printLL(head):
    return head

def SIZE(head):
    return head.size()

def scarmble(head, b, r, size):
    perB = int((b*size)//100)
    perR = int((r*size)//100)
    
    head.cut(perB); print(f"BottomUp {b:.3f} % : {head}")
    head.riffle(perR); print(f"Riffle {r:.3f} % : {head}")
    head.deriffle(perR); print(f"Deriffle {r:.3f} % : {head}")
    head.cut(size - perB); print(f"Debottomup {b:.3f} % : {head}")

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)