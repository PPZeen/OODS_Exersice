class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,i):
        self.items.append(i)
        return f"Add {i} index is {self.size() - 1}"
        
    def dequeue(self):
        if self.isEmpty() == "Empty": return -1
        i = self.items.pop(0)
        return f"Pop {i} size in queue is {self.size()}"
    
    def isEmpty(self):
        return "Empty" if len(self.items) == 0 else f"Number in Queue is :  {self.items}"
    
    def size(self):
        return len(self.items)

orders = input("Enter Input : ").split(',')
Q = Queue()

for order in orders:
    if order[0] == 'D':
        print(Q.dequeue())
    elif order[0] == 'E':
        print(Q.enqueue(order[2::]))
    else : continue
print(Q.isEmpty())