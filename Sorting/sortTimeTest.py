import time, random

def bubble(l):  # ตัวที่ใหญ่ที่สุดลอยไปด้านบน
    for last in range(len(l)-1,0,-1):
        swap = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i] 
                swap = True
        #print(l)
        if not swap: break
    return l

def bubbleSort(l): # recursive version
    count = 0
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            count += 1
    if count == 0: return l
    return bubbleSort(l)

def selection(l): # ไล่จากด้านหลัง หาตัวใหญ่สุดจากด้านหน้า สลับไปด้านหลัง
    for last in range(len(l)-1, 0, -1):
        b = l[0]
        bInx = 0
        for i in range(1, last+1):
            if l[i] > b:
                b = l[i]
                bInx= i
        l[last], l[bInx] = l[bInx], l[last]
        #print(l)
    return l

def insertion(l):
    for i in range(1, len(l)):
        iEle = l[i]
        for j in range(i, -1, -1):
            if iEle < l[j-1] and j > 0: 
                l[j] = l[j-1]
            else: l[j] = iEle; break
        #print(l)
    return l

def shell(l):
    def shellSort(l, dIc):
        for inc in dIc:
            for i in range(inc,len(l)):
                iEle = l[i]
                for j in range(i, -1, -inc):
                    if iEle < l[j-inc] and j >= inc:
                        l[j] = l[j-inc]
                    else :l[j] = iEle; break
            #print(l)
        return l
    
    dIc = [i for i in range(int(len(l)/3 + 0.67),0,-2)]
    shellSort(l, dIc)
    return l

def merge(l):
    if len(l) > 1:
        r = len(l)//2
        L = l[:r]
        M = l[r:]

        merge(L)
        merge(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            l[k] = M[j]
            j += 1
            k += 1
    return l

def quick(l):
    def quickSort(l, fpos, lpos):
        if fpos < lpos:
            pv = fpos
            fc = fpos
            lc = lpos
            
            while (fc < lc):
                while (l[fc] <= l[pv]) and fc < lpos: fc += 1
                while l[lc] > l[pv]: lc -= 1
                if fc < lc:
                    l[fc], l[lc] = l[lc], l[fc]#; print(l)
                    
            l[pv], l[lc] = l[lc], l[pv]#; print(l)
            quickSort(l, fpos, lc-1)
            quickSort(l, lc+1, lpos)
        return l
    return quickSort(l, 0, len(l)-1)

def heap(l):
    def heapify(ar, n, i):
        lg = i 
        l = 2 * i + 1 
        r = 2 * i + 2
 
        if l < n and ar[i] < ar[l]: lg = l
        if r < n and ar[lg] < ar[r]: lg = r

        if lg != i:
            ar[i], ar[lg] = ar[lg], ar[i]
            heapify(ar, n, lg)
 
    def heapSort(l):
        n = len(l)
        for i in range(n // 2 - 1, -1, -1): heapify(l, n, i)
        for i in range(n - 1, 0, -1):
            l[i], l[0] = l[0], l[i]
            heapify(l, i, 0)
        return l
    
    return heapSort(l)

def radix(l):
    def countingSort(l, exp1):
        n = len(l)
        output = [0] * n
        count = [0] * 10

        for i in range(0, n):
            index = l[i] // exp1
            count[index % 10] += 1

        for i in range(1, 10): count[i] += count[i-1]
    
        i = n - 1
        while i >= 0:
            index = l[i] // exp1
            output[count[index % 10] - 1] = l[i]
            count[index % 10] -= 1
            i -= 1
            
        i = 0
        for i in range(0, len(l)): l[i] = output[i]
    
    max1 = max(l)
    exp = 1
    while max1 / exp >= 1:
        countingSort(l, exp)
        exp *= 10

    return l            

def test(l):
    start_time = time.time()
    L = bubble(l)
    end_time = time.time()
    print(f"Bubble Sort:  {end_time - start_time:.8f} s")
    
    start_time = time.time()
    L = selection(l)
    end_time = time.time()
    print(f"Selection Sort: {end_time - start_time:.8f} s")
    
    start_time = time.time()
    L = insertion(l)
    end_time = time.time()
    print(f"Insertion Sort: {end_time - start_time:.8f} s")
    
    start_time = time.time()
    L = shell(l)
    end_time = time.time()
    print(f"Shell Sort: {end_time - start_time:.8f} s")
    
    start_time = time.time()
    L = merge(l)
    end_time = time.time()
    print(f"Merge Sort: {end_time - start_time:.8f} s")

    start_time = time.time()
    L = quick(l)
    end_time = time.time()
    print(f"Quick Sort: {end_time - start_time:.8f} s")
    
    start_time = time.time()
    L = heap(l)
    end_time = time.time()
    print(f"Heap Sort: {end_time - start_time:.8f} s")

    start_time = time.time()
    L = radix(l)
    end_time = time.time()
    print(f"Radix Sort: {end_time - start_time:.8f} s")
    

l = []
for i in range(2000): l.append(random.randint(0, 100))
test(l)

# def bubble(l):
#     start_time = time.time()
#     for last in range(len(l)-1, 0,-1):
#         swaped = False
#         for i in range(last):
#             if l[i] > l[i+1]:
#                 l[i], l[i+1] = l[i+1], l[i] 
#                 swaped = True
#         if not swaped: break
#     end_time = time.time()
#     return f"{end_time - start_time:.8f} s"
            
# def selection(l):
#     start_time = time.time()
#     for last in range(len(l)-1, 0, -1):
#         biggest = l[0]
#         biggest_i= 0
#         for i in range(1, last+1):
#             if l[i] > biggest:
#                 biggest = l[i]
#                 biggest_i= i
#         l[last], l[biggest_i] = l[biggest_i], l[last]
#     end_time = time.time()
#     return f"{end_time - start_time:.8f} s"

# def insertion(l):
#     start_time = time.time()
#     for i in range(1, len(l)):
#         iEle= l[i]
#         for j in range(i, -1, -1):
#             if iEle < l[j-1] and j > 0:
#                 l[j] = l[j-1]
#             else: l[j] = iEle; break
#     end_time = time.time()
#     return f"{end_time - start_time:.8f} s"

# def shell(l):
#     start_time = time.time()
#     def shellSort(l, dIncrements):
#         for inc in dIncrements:
#             for i in range(inc,len(l)):
#                 iEle = l[i]
#                 for j in range(i, -1, -inc):
#                     if iEle < l[j-inc] and j >= inc:
#                         l[j] = l[j-inc]
#                     else :l[j] = iEle; break
#         return l
#     dIncrements = [i for i in range(99,0,-2)]
#     shellSort(l, dIncrements)
#     end_time = time.time()
#     return f"{end_time - start_time:.8f} s"

# def merge(l):
#     def mergeSort(array):
#         if len(array) > 1:
#             r = len(array)//2
#             L = array[:r]
#             M = array[r:]

#             mergeSort(L)
#             mergeSort(M)

#             i = j = k = 0

#             while i < len(L) and j < len(M):
#                 if L[i] < M[j]:
#                     array[k] = L[i]
#                     i += 1
#                 else:
#                     array[k] = M[j]
#                     j += 1
#                 k += 1

#             while i < len(L):
#                 array[k] = L[i]
#                 i += 1
#                 k += 1

#             while j < len(M):
#                 array[k] = M[j]
#                 j += 1
#                 k += 1
#         return array
#     start_time = time.time()
#     l = mergeSort(l)
#     end_time = time.time()
#     return f"{end_time - start_time:.8f} s"

# def quick(l):
#     start_time = time.time()
#     def partition(array, low, high):
#         pivot = array[high]
#         i = low - 1
#         for j in range(low, high):
#             if array[j] <= pivot:
#                 i = i + 1
#                 (array[i], array[j]) = (array[j], array[i])
#         (array[i + 1], array[high]) = (array[high], array[i + 1])
#         return i + 1

#     def quickSort(array, low, high):
#         if low < high:
#             pi = partition(array, low, high)
#             quickSort(array, low, pi - 1)
#             quickSort(array, pi + 1, high)
    
#     quickSort(l, 0, len(l)-1)
#     end_time = time.time()
#     return f"{end_time - start_time:.8f} s"

# print(f"Bubble: {bubble(l)}")
# print(f"Selection: {selection(l)}")
# print(f"Insertion: {insertion(l)}")
# print(f"Shell: {shell(l)}")
# print(f"Merge: {merge(l)}")
# print(f"Quick: {quick(l)}")