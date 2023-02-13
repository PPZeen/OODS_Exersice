def find_palindrome(st, l):
    global index
    if len(st) not in [1,2]: 
        if st[index] != st[l-index]:
            return False
        else: 
            index += 1
            return find_palindrome(st[1:-1], len(st[1:-1])-1)
    return True

index = 0
x = input("Enter Input : ")
print(f"'{x}'", "is palindrome" if find_palindrome(x, len(x)-1) else "is not palindrome")