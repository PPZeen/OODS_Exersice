level = ["Breeze", "Depression", "Tropical Storm", "Typhoon", "Super Typhoon"]
print(" *** Wind classification *** ")

speed = float(input("Enter wind speed (km/h) : "))
if speed < 52: 
    s = 0
elif speed < 56: 
    s = 1
elif speed < 102:
    s = 2
elif speed < 209:
    s = 3
else :
    s = 4

print(f"Wind classification is {level[s]}.")