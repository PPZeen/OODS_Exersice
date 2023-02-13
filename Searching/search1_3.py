class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, size, maxCollision):
        self.items = [None]*size
        self.size = size
        self.maxCollision = maxCollision
        self.full = False

    def Add(self, k, v):
        if None in self.items:
            defult = self.ASCLL(k) % self.size
            index = defult
            for i in range(self.maxCollision):
                if self.items[index] == None:
                    self.items[index] = Data(k,v)
                    return 
                print(f"collision number {i+1} at {index}")
                index = (defult + (i+1)**2) % self.size
            print("Max of collisionChain")
        elif not self.full:
            self.full = True
            print("This table is full !!!!!!")
            
    def table(self):
        if not self.full:
            print(''.join([f"#{i+1}\t{self.items[i]}\n" for i in range(self.size)]) + "---------------------------")
         
    def ASCLL(self, text):
        return sum([ord(c) for c in text])

print(" ***** Fun with hashing *****")
pops, orders = input("Enter Input : ").split('/')
s, mC = list(map(int, pops.split()))
orders = [o.split() for o in orders.split(',')]

H = Hash(s, mC)
for key, value in orders:
    H.Add(key,value)
    H.table()