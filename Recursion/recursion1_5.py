def staircase(n, m):
    ans = ""
    if n == 0:
        if m == 0 : return "Not Draw!"
        return ans
    elif n > 0:
        return ans + '_'*(n-1) + '#'*(m-(n-1)) + '\n' + staircase(n-1, m)
    else:
        return ans + '_'*(abs(m)+n) + '#'*(abs(n)) + '\n' + staircase(n+1, m)

n = int(input("Enter Input : "))
print(staircase(n, n))