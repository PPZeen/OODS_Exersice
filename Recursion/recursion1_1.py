def find_min(r, list):
    global min
    if r != 0:
        num = list[r-1]
        if num < min : min = num
        return find_min(r-1, list)
    return min

x = [int(i) for i in input("Enter Input : ").split()]
min = x[-1]
print(f"Min : {find_min(len(x)-1, x)}")