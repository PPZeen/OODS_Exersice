def firstGreaterValue(l, k):
    values = [j for j in sorted([i-k for i in l]) if j > 0]
    return  values[0]+k if len(values) > 0 else "No First Greater Value"

inp = input('Enter Input : ').split('/')
l, r = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for n in r: print(firstGreaterValue(l,n))