class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, i):
        self.items.append(i)
        return f'Add = {i}'
        
    def pop(self):
        if self.isEmpty() : return -1
        item = self.items.pop()
        return f"Pop = {item}"
    
    def delete(self, item):
        if self.isEmpty() : return -1
        count = 0
        while item in self.items :
            x = self.items.pop(self.items.index(item))
            count += 1
        if count != 0:
            return '\n'.join([f"Delete = {item}" for i in range(count)])
    
    def Ldelete(self, item):
        if self.isEmpty() : return -1
        cl = [i for i in sorted(self.items) if item > i]
        for i in cl:
            self.delete(i)
        if len(cl) != 0:
            return '\n'.join([f"Delete = {i} Because {i} is less than {item}" for i in [str(e) for e in cl]])
        
    def Mdelete(self,item):
        if self.isEmpty() : return -1
        cl = [i for i in sorted(self.items) if item < i]
        for i in cl:
            self.delete(i)
        if len(cl) != 0:
            return '\n'.join([f"Delete = {i} Because {i} is more than {item}" for i in [str(e) for e in cl]])
    
    def isEmpty(self):
        return True if len(self.items) == 0 else False
    
    def __str__(self):
        return f"Value in Stack = {self.items}"    

def ManageStack(o):
    if o[0] == 'P':
        print(s.pop())
    elif o[0] == 'A':
        print(s.push(int(o[2::])))
    elif o[0] == 'D':
        ans = s.delete(int(o[2::]))
        if ans != None:
            print(ans)
    elif o[0:2] == 'LD':
        ans = s.Ldelete(int(o[3::]))
        if ans != None:
            print(ans)
    elif o[0:2] == 'MD':
        ans = s.Mdelete(int(o[3::]))
        if ans != None:
            print(ans)
   
s = Stack()
orders = [e for e in input("Enter Input : ").split(',')]
for order in orders:
    ManageStack(order)
print(s)
