class translator:
    def check(self, num):
        ans = ''
        if num == 0 :return ans
        
        ch = {1:'I', 4: 'IV', 5:'V', 9:'IX', 10:'X',
              40:'XL', 50:'L', 90:'XC', 100:'C',
              400:'CD', 500:'D', 900:'CM', 1000:'M'}
        
        lich = list(ch.keys())
        
        while True:
            index = len([-1*(i-num) for i in lich if -1*(i-num) >= 0])-1
            ans += ch[lich[index]]
            num -= list(ch.keys())[index]
            if num == 0: break
        return ans
        
    def deciToRoman(self, num):
        ans = []
        count = 0
        while True:
            ans.insert(0,self.check(num%10 * 10**count))
            num //= 10
            count += 1 
            if num == 0 :break
        return ''.join(ans)

    def romanToDeci(self, s):
        ch = {1:'I', 4: 'IV', 5:'V', 9:'IX', 10:'X',
              40:'XL', 50:'L', 90:'XC', 100:'C',
              400:'CD', 500:'D', 900:'CM', 1000:'M'}
        lich = list(ch.values())
        lich.reverse()
        
        ans = 0
        count = 0

        while count < len(lich):
            key = lich[count]
            le = len(key)
            index = s.find(key)
            if (index != -1 and index == 0) or (le>1 and index>0):
                indexH = lich.index(key)
                ans += list(ch.keys())[len(lich) - indexH - 1]
                s = s[le::]
            else: count += 1
        return ans

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))