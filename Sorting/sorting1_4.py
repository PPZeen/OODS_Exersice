def insertion(l): 
    for i in range(1, len(l)):
        iEle= l[i]
        for j in range(i, -1, -1):
            if iEle < l[j-1] and j > 0:
                l[j] = l[j-1]
            else: l[j] = iEle; break
    return l

def find_median(l):
    l = insertion(l)
    if len(l) == 1: median = l[0]
    elif len(l)%2 == 0: median = (l[len(l)//2] + l[len(l)//2 - 1])/2
    else: median = l[len(l)//2]
    
    return median

l = [int(e) for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "insertion sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print(f"   Your Answer : {Ans}")
else:
    for i in range(len(l)):
        print(f"list = {l[:i+1:]} : median = {find_median(l[:i+1:]):.1f}")