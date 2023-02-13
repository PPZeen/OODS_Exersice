class Stack :

    def __init__(self,items = None) :
        if items == None:
            self.items = []
        else:
            self.items = items

    def isEmpty(self) :
        return True if len(self.items) == 0 else False
    
    def push(self, data) :
        self.items.append(data)

    def pop(self, index=-1) : 
        return self.items.pop(index) 

    def size(self) :
        return len(self.items)

    def peek(self) :
        return None if self.isEmpty() else self.items[-1]


def infix2postfix(exp) :
    s = Stack()
    ans = ''
    for e in exp:
        if e in ['+','-','*','/','(', ')']:
            if s.isEmpty() and e != ')': s.push(e)
            else:
                if e in ['+','-']:
                    while s.peek() in ['*','/','-','+']:
                        ch = s.pop()
                        ans += ch
                    s.push(e)
                elif e in ['*', '/']:
                    while s.peek() in ['*','/']:
                        ch = s.pop()
                        ans += ch
                    s.push(e)
                elif e == ')':
                    while s.peek() in ['+','-','*','/','(']:
                        ch = s.pop()
                        if ch != '(':
                            ans += ch
                else :
                    s.push(e)
        else:
            ans += e
    ans += ''.join(reversed(s.items))
    return ans

print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))