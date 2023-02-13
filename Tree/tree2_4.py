def find_Team(t, n, l):
    if n > l : return l
    if n == l : t.append(l)
    if (2*n + 1) < l:
        t.append(2*n + 1)
        find_Team(t, 2*n + 1, l)
    if (2*n + 2) < l:
        t.append(2*n + 2)
        find_Team(t, 2*n + 2, l)
    return t
    
def compare(n, m):
    power1 = 0
    power2 = 0
    for i in n: power1 += power[i]
    for j in m: power2 += power[j]
    if power1 > power2: return f"{n[0]}>{m[0]}"
    elif power1 < power2: return f"{n[0]}<{m[0]}"
    return f"{n[0]}={m[0]}"
            
power, order = input('Enter Input : ').split('/')
power = [int(i) for i in power.split()]
print(sum(power))

for e in order.split(','):
    a, b = [int(i) for i in e.split()]
    team1 = find_Team([a], a, len(power))
    team2 = find_Team([b], b, len(power))
    print(compare(team1, team2))