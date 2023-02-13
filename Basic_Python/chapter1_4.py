from asyncio import constants


print("*** Minesweeper ***")

def chage(n,m,lst):
    for i in range(n-1,n+2):
        if i < 0: continue
        if i > 4 : break
        for j in range(m-1, m+2):
            if j < 0: continue
            if j > 4 : break
            if lst[i][j] == '-':
                lst[i][j] = '1'
            elif lst[i][j] not in ['-', '#']:
                lst[i][j] = str(int(lst[i][j]) + 1)
    return lst

def num_grid(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '#':
                lst = chage(i,j,lst)
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '-':
                lst[i][j] = '0'
    return lst

lst_input = []
input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:
  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")