def output(a,b,c):
    for x,y,z in zip(a,b,c): print(f"{x}  {y}  {z}")

def switch(li, lf):
    i1 = li.index([e for e in li if e != '|'][0])
    if lf[-1] == '|': lf[-1] = li.pop(i1)
    else:
        i2 = lf.index([e for e in lf if e != '|'][0]) - 1 
        value = li.pop(i1)
        lf.pop(i2)
        lf.insert(i2, value)
    li.insert(i1, '|')
    
    return li, lf
  
def move(n, A, B, C):
    if n == 1:
        print(f"move {n} from  {A} to {C}")
        x[A], x[C] = switch(x[A], x[C]); output(x['A'],x['B'],x['C'])
    else:
        move(n-1, A, C, B)
        print(f"move {n} from  {A} to {C}")
        x[A], x[C] = switch(x[A], x[C]); output(x['A'],x['B'],x['C'])
        move(n-1, B, A, C)
    
n = int(input("Enter Input : "))
x = {'A':['|'] + [i for i in range(1,n+1)], 'B':['|']*(n+1), 'C':['|']*(n+1)}
output(x['A'],x['B'],x['C'])
move(n, 'A', 'B', 'C')