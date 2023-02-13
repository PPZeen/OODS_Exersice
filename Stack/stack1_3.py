class Stack:

    def __init__(self, items):
        if items == None:
            self.items = []
        else:
            self.items = items
    
    def push(self, value):
        self.items.append(value)
        
    def pop(self, index):
        if index == None: return self.items.pop() 
        return self.items.pop(index) 
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return True if len(self.items) == 0 else False
    
    def __str__(self):
        return "Empty" if self.isEmpty() else ''.join(reversed(self.items))

inp = input('Enter Input : ').split()

S = Stack(inp)

ch = []
combo = 0
count = 0
out = False
while not out:
    if S.size() < 3: break
    for i in S.items:
        count += 1
        if len(ch) == 0: ch.append(i)
        else:
            if ch[0] == i: ch.append(i)
            else:
                ch.clear()
                ch.append(i)
            if len(ch) == 3:
                index = S.items.index(ch[0])
                S.pop(index)
                S.pop(index)
                S.pop(index)
                if S.isEmpty() : out = True
                ch.clear()
                count = 0
                combo += 1
                break
    
    if count == S.size() : out = True
        
print(S.size())
print(S)
if combo > 1: print(f"Combo : {combo} ! ! !")