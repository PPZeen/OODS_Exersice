class Hash:
    def __init__(self, size, maxCollision, threshold):
        self.items = [None]*size
        self.size = size
        self.maxCollision = maxCollision
        self.threshold = threshold
        
        print("Initial Table :")
        self.table()

    def Add(self, value):
        if self.getAmount() + 1 > (self.threshold/100)*self.size:
            print("****** Data over threshold - Rehash !!! ******")
            self.reHash(value)
        elif None in self.items:
            defult = value % self.size
            index = defult
            for i in range(self.maxCollision):
                if self.items[index] == None:
                    self.items[index] = value
                    return 
                print(f"collision number {i+1} at {index}")
                index = (defult + (i+1)**2) % self.size
            print("****** Max collision - Rehash !!! ******")
            self.reHash(value)

    def table(self):
        print(''.join([f"#{i+1}\t{self.items[i]}\n" for i in range(self.size)]) + "----------------------------------------")
    
    def reHash(self, value):
        global orders
        self.size = self.findNextPirme(self.size*2)
        items = [i for i in self.items if i != None]
        self.items = [None]*self.size
        for i in range(len(items)+1): self.Add(orders[i])
        
    def findNextPirme(self, n):
        def prime(n):
            if n <= 1: return False
            for i in range(2,n):
                if n%i == 0: return False
            return True
        
        while True:
            if prime(n): return n
            n += 1
    
    def getAmount(self):
        return len([i for i in self.items if i != None])
    
print(" ***** Rehashing *****")
pops, datas = input("Enter Input : ").split('/')
s, mC, tSh = list(map(int, pops.split()))
orders = [int(num) for num in datas.split()]

H = Hash(s, mC, tSh)
for value in orders: print(f"Add : {value}"); H.Add(value); H.table()