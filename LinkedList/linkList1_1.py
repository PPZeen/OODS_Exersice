class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
    def __str__(self):
        return self.data

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
        return f"link list : {'->'.join(ans)}"
    
    def isEmpty(self):
        return self.head == None
    
    def append(self, data): 
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
            
    def insert(self, index, data):
        if index >= 0:
            p = Node(data)
            if self.head == None:
                if index == 0:
                    self.head = p
                    return f"index = {index} and data = {data}"
            else:
                count = 0
                t = self.head
                if index == 0 :
                    self.head = p
                    p.next = t
                    return f"index = {index} and data = {data}"
                else:
                    while t.next != None:
                        count += 1
                        if count == index:
                            q = t.next
                            t.next = p
                            p.next = q
                            return f"index = {index} and data = {data}"
                        t = t.next
                    if count+1 == index:
                        t.next = p
                        return f"index = {index} and data = {data}"

        return "Data cannot be added"    
    
orders = input("Enter Input : ").split(',')
l = LinkList(orders[0].split(' '))
print(l)

for index, data in [e.split(':') for e in orders[1::]]:
    print(l.insert(int(index), data))
    print(l)