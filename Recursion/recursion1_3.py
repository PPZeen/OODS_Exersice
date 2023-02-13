def find_GCD(x, y):
    global n
    if n == 0: return y
    if y%n == 0 and x%n == 0:
        return n
    n -= 1
    return find_GCD(x,y)

x, y = [int(i) for i in input("Enter Input : ").split()]
if x == 0 and y == 0: print("Error! must be not all zero.")
else:
    if x > y :
        n = y
        x,y = y,x
    n = abs(x)
    if (x < 0 and y < 0) or (x >= 0 and y >= 0):
        print(f"The gcd of {y if abs(y) > abs(x) else x} and {x if abs(y) > abs(x) else y} is : {find_GCD(abs(x),abs(y))}")
    else:
        print(f"The gcd of {y if y > x else x} and {x if y > x else y} is : {find_GCD(abs(x),abs(y))}")