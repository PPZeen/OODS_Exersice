class TorKham:
    def __init__(self):
        self.words = []

    def restart(self):
        self.words = []
        return "game restarted"

    def play(self, word):
        if len(self.words) == 0:
            self.words.append(word)
            return f"'{word}' -> {self.words}"
        else:
            if word[:2].lower() == self.words[-1][-2::].lower():
                self.words.append(word)
                return f"'{word}' -> {self.words}"
        return f"'{word}' -> game over"

torkham = TorKham()
print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')

for c in S:
    if c == 'R':
        print(torkham.restart())
    elif c == 'X':
        break
    elif 'P ' in c:
        print(torkham.play(c[2::]))
    else:
        print(f"'{c}' is Invalid Input !!!")
        break