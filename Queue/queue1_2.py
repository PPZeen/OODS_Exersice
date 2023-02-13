class Queue:
    def __init__(self):
        self.items = {"EN":[], "ES":[]}
    
    def enqueue(self,status, id):
        self.items[status].append(id)
        
    def dequeue(self):
        if self.isEmpty() : return "Empty"
        return self.items["EN"].pop(0) if len(self.items["ES"]) == 0  else self.items["ES"].pop(0)         
   
    def isEmpty(self):
        return True if len(self.items["EN"]) + len(self.items["ES"]) == 0 else False
    
orders = input("Enter Input : ").split(',')
Q = Queue()

for order in orders:
    if order[0] == 'D': print(Q.dequeue())
    elif order[0] == 'E': Q.enqueue(order[:2:], order[3::])
    else : continue