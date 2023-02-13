def hbd(age):
    return f"saimai is just {20 if age%2 == 0 else 21}, in base {age//2}!"

year = input("Enter year : ")
print(hbd(int(year)))