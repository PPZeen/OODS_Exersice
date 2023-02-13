class node:
    def __init__(self, data):
        self.data = data
        self.day = 0

def sort(l):
    l = [(i.data, i) for i in l]
    l = sorted(l)
    l = [n for i,n in l]
    return l    
        
k, order = input("Enter Input : ").split('/')
vans = [node(i) for i in range(1, int(k)+1)]
order = [int(i) for i in order.split()]
booking = []

count = 0
while len(order) != 0:
    while len(vans) != 0 and len(order) != 0:
        o = order.pop(0)
        vans[0].day = o
        print(f"Customer {count+1} Booking Van {vans[0].data} | {o} day(s)")
        
        booking.append(vans.pop(0))
        count += 1
    
    s = 0
    for i in range(len(booking)):
        b = booking[s]
        b.day -= 1
        if b.day == 0:
            vans.append(booking.pop(booking.index(b)))
            vans = sort(vans)
            continue
        s += 1