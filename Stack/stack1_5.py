class Stack:
    def __init__(self, max,items = None) :
        if items == None or items == [0]:
            self.items = []
        else:
            self.items = items
        self.max = max
        
    def isEmpty(self) :
        return True if len(self.items) == 0 else False
    
    def push(self, data) :
        self.items.append(data)

    def pop(self, index = -1) : 
        return self.items.pop(index) 
    
    def size(self) :
        return len(self.items)
    
    def check(self, status, n):
        if status == "arrive":
            if self.size() == self.max: return f"car {n} cannot arrive : Soi Full"
            if n in self.items : return f"car {n} already in soi"
            self.push(n)
            return f"car {n} arrive! : Add Car {n}" 
        elif status == "depart":
            if self.size() == 0: return f"car {n} cannot depart : Soi Empty"
            if n not in self.items : return "car {} cannot depart : Dont Have Car {}".format(n,n)
            if self.items[0] == n :
                self.pop(0)
                return f"car {n} depart ! : Car {n} was remove"
            return f"car {n} cannot depart : Car {n} was not remove"
        return "Error status"

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

m,n = int(m),int(n)
S = Stack(m, [int(i) for i in s.split(',')])

print(S.check(o,n))
print(S.items)