print("*** Reading E-Book ***")
Text , Highlight = input("Text , Highlight : ").split(",")

index = 0
while True:
    indexH = Text.find(Highlight, index)
    if indexH < 0:
        break
    print(f"{Text[index:indexH]}[{Highlight}]", end='')
    index = indexH + 1
print(Text[index:])