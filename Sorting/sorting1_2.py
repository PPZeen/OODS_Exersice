def selection(l): 
    for last in range(len(l)-1, 0, -1):
        biggest = l[0]
        biggest_i= 0
        for i in range(1, last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i= i
        l[last], l[biggest_i] = l[biggest_i], l[last]
    return l

def sortIgnNegative(l):
    ans = l.copy()
    for n in ans:
        if n >= 0 : ans[ans.index(n)] = 0
        else: x = l.pop(l.index(n))
        
    l = selection(l)
    for i in range(len(ans)):
        if ans[i] == 0 : ans[i] = l.pop(0)

    return ' '.join([str(n) for n in ans])

inp = [int(i) for i in input("Enter Input : ").split()]
print(sortIgnNegative(inp))