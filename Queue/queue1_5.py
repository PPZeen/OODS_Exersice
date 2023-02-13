class Stack:
    def __init__(self, items=None):
        if items == None: self.items = []
        else:
            self.items = [e for e in items]
    
    def push(self, value):
        self.items.append(value)
        
    def pop(self, index):
        if index == None: return self.items.pop() 
        return self.items.pop(index) 
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return True if len(self.items) == 0 else False
    
    def out(self):
        return "Empty" if self.isEmpty() else ''.join(reversed(self.items))
    
    def __str__(self):
        return "ytpmE" if self.isEmpty() else ''.join(reversed(self.items))
    
class Queue:
    def __init__(self, item=None):
        if item == None: self.items = []
        else:
            self.items = item
        
    def enqueue(self,i):
        self.items.append(i)
        
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return -1
    
    def isEmpty(self):
        return True if len(self.items) == 0 else False
    
    def size(self):
        return len(self.items)
    
def Bomb(S):
    ch = []
    item = []
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
                    item.append(S.pop(index))
                    S.pop(index)
                    S.pop(index)
                    if S.isEmpty() : out = True
                    ch.clear()
                    count = 0
                    combo += 1
                    break
        if count == S.size() : out = True
    return S, item, combo
    
normal, mirror = input("Enter Input (Normal, Mirror) : ").split()
Cmiror, it, combo = Bomb(Stack(mirror[::-1]))
item = Queue(it)

ans = ''
check = [normal[0]]
for i in range(1, len(normal)):
    ch = normal[i]
    if ch == check[-1]:
        if len(check) == 2 and not item.isEmpty():
            check.append(item.dequeue())
            ans += ''.join(check)
            check.clear()
        
        check.append(ch)
    else:
        ans += ''.join(check)
        check.clear()
        check.append(ch)
ans += ''.join(check)

Cnormal1, itN1, comboNormal = Bomb(Stack(normal))
Cnormal, itN, comboN = Bomb(Stack(ans))

if comboNormal > comboN: n = comboNormal - combo
else: n = comboN - combo
if n < 0 : n = 0
print(f"NORMAL :\n{Cnormal.size()}\n{Cnormal.out()}\n{n} Explosive(s) ! ! ! (NORMAL)")

bomb = comboNormal - comboN
if bomb < 0:
    bomb = abs(bomb)
    print(f"Failed Interrupted {bomb} Bomb(s)")
elif (bomb < combo) and (comboN != 0):
    print(f"Failed Interrupted {combo - bomb} Bomb(s)")

print("------------MIRROR------------")
print(f": RORRIM\n{Cmiror.size()}\n{Cmiror}\n(RORRIM) ! ! ! (s)evisolpxE {combo}")