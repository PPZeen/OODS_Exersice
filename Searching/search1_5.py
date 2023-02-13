def minW(L, box, maxW):
    curBox = 1
    w = 0
    for l in L:
        if w + l <= maxW: w += l
        else:
            curBox += 1
            w = l
    if curBox == box: return maxW

    return minW(L, box, maxW + 1)

inp, box = input('Enter Input : ').split('/')
L = [int(x) for x in inp.split()]
box = int(box)
print(f'Minimum weigth for {box} box(es) = {minW(L, box, max(L))}')