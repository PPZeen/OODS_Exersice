#--------------------------------------------------------- min --------------------------------------------------------------
def find_min(l, n):
    if len(l) == 0: return n
    if l[0] > n: return find_min(l[1::],n)
    return find_min(l[1::], l[0])

def test_find_min():
    x = [3,5,6,7,2,8,-8,-3,-54,1,0]
    min = find_min(x[1::], x[0])
    print(f"min of {x} : {min}")

#--------------------------------------------------------- max --------------------------------------------------------------
def find_max(l, n):
    if len(l) == 0: return n
    if l[0] < n: return find_max(l[1::],n)
    return find_max(l[1::], l[0])

def test_find_max():
    x = [3,5,6,7,2,8,-8,-3,-54,1,0]
    max = find_max(x[1::], x[0])
    print(f"max of {x} : {max}")

#--------------------------------------------------- sum of array -----------------------------------------------------------
def find_sum_of_array(l,n):
    if len(l) == 0: return n
    return n + find_sum_of_array(l[1::], l[0])

def test_find_sum_of_array():
    x = [3,5,6,7,2,8,-8,-3,-54,1,0]
    sumArray = find_sum_of_array(x[1::], x[0])
    print(f"sum of {x} : {sumArray}")

#------------------------------------------------------ palindome -----------------------------------------------------------
def find_palindome(t):
    if len(t) in [0,1]: return True
    if t[0] == t[-1]: return find_palindome(t[1:-1])
    return False

def test_find_palindome():
    x = "abcd"
    y = "abccba"
    z = "abcba"
    print(f"{x} is palindome" if find_palindome(x) else f"{x} is not palindome")
    print(f"{y} is palindome" if find_palindome(y) else f"{y} is not palindome")
    print(f"{z} is palindome" if find_palindome(z) else f"{z} is not palindome")

#------------------------------------------------------ factorial -----------------------------------------------------------
def find_factorial(n):
    if n in [0,1]: return 1
    return n * find_factorial(n-1)

def test_find_factorial():
    n = 7
    print(f"factorial of {n} is {find_factorial(n)}")

#------------------------------------------------------ fibonacci -----------------------------------------------------------
def find_fibonacci(n):
    if n <= 1: return n
    return find_fibonacci(n-1) + find_fibonacci(n-2)

def test_find_fibonacci():
    n = 6
    print(f"fibonacci of {n} is {find_fibonacci(n)}")

#------------------------------------------------------ base hanoi ----------------------------------------------------------
def move(n, A, C, B):
    if n == 1: print(f"{n} from {A} to {C}")
    else:
        move(n-1, A, B, C)
        print(f"{n} from {A} to {C}")
        move(n-1, B, C, A)

def output(a, b, c):
    for x,y,z in zip(a,b,c): print(f"{x}  {y}  {z}")

#---------------------------------------------------------------------------------------------------------------------------