def insertion(l): 
    for i in range(1, len(l)):
        iEle= l[i]
        for j in range(i, -1, -1):
            if iEle < l[j-1] and j > 0:
                l[j] = l[j-1]
            else: l[j] = iEle; break
    return l

def ssEn(l, num):
    def subsets(numbers):
        if numbers == []:
            return [[]]
        x = subsets(numbers[1:])
        return x + [[numbers[0]] + y for y in x]
 
    def subsets_of_given_size(numbers, n): return insertion([insertion(x) for x in subsets(numbers) if len(x) == n])
    
    ans = []
    for i in range(len(l)):
        ls = subsets_of_given_size(l, i+1)
        for j in ls:
            if sum(j) == num: ans.append(j)
    return ans if len(ans) != 0 else ["No Subset"]

num, l = input("Enter Input : ").split('/')
l = [int(i) for i in l.split()]
ans = ssEn(l, int(num))
for a in ans: print(a)
