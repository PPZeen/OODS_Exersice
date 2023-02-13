def drome(l):
    l2s = False
    s2l = False
    eq = False
    
    for i in range(len(l)-1):
        if l[i] < l[i+1]: s2l = True
        elif l[i] > l[i+1]: l2s = True
        else: eq = True
    
    if (s2l & (not l2s) & (not eq)): ans = "Metadrome"
    elif (s2l & (not l2s) & eq): ans = "Plaindrome"
    elif ((not s2l) & l2s & (not eq)): ans = "Katadrome"
    elif ((not s2l) & l2s & eq): ans = "Nialpdrome"
    elif ((not s2l) & (not l2s) & eq): ans = "Repdrome"
    else: ans = "Nondrome"

    return ans
    
inp = [int(i) for i in input("Enter Input : ")]
print(drome(inp))