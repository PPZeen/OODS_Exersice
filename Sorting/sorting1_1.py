def bubbleSort(array):
    count = 0
    for idx in range(len(array)-1):
        if array[idx] > array[idx + 1]:
            array[idx],array[idx + 1] = array[idx + 1],array[idx]
            count += 1

    if count == 0: return array
    return bubbleSort(array)
    
inp = [int(i) for i in input("Enter Input : ").split()]
print(bubbleSort(inp))