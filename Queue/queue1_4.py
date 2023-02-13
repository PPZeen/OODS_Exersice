class Queue:
    def __init__(self, item=None):
        if item == None: self.items = []
        else:
            self.items = item
            
        self.ac = {'0':"Eat", '1':"Game", '2':"Learn", '3':"Movie"}
        self.lo = {'0':"Res.", '1':"ClassR.", '2':"SuperM.", '3':"Home"}
        
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
    
    def num2mean(self):
        ans = []
        for e in self.items:
            ans.append(self.ac[e[0]] + ':' + self.lo[e[2]])
        return ans

def score(my, your):
    count = 0
    for i in range(my.size()):
        n = my.dequeue().split(':')
        m = your.dequeue().split(':')
        if n[0] == m[0]:
            if n[1] == m[1]: count += 4
            else: count += 1
        else:
            if n[1] == m[1]: count += 2
            else: count -= 5
    if count >= 7:
        return f"Yes! You're my love! : Score is {count}."
    elif count > 0:
        return f"Umm.. It's complicated relationship! : Score is {count}."
    return f"No! We're just friends. : Score is {count}."

lis = [i.split() for i in input("Enter Input : ").split(',')]

My = Queue([n for n,m in lis])
Your = Queue([m for n,m in lis])

print(f"My   Queue = {', '.join(My.items)}")
print(f"Your Queue = {', '.join(Your.items)}")
print(f"My   Activity:Location = {', '.join(My.num2mean())}")
print(f"Your Activity:Location = {', '.join(Your.num2mean())}")
print(score(My, Your))