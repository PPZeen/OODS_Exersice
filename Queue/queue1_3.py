class Queue:
    def __init__(self, item):
        self.items = [i for i in item if i != ' ']
        self.lebel = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                      'n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    def enqueue(self,i):
        self.items.append(i)
        
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return -1
    
    def isEmpty(self):
        return True if len(self.items) == 0 else False
    def size(self):
        return len(self.items)

def encodemsg(q1, q2):
    ans = []
    count = 0
    for e in q1.items:
        num = q2.dequeue()
        q2.enqueue(num)
        if e in q1.lebel:
            index = q1.lebel.index(e)
            ans.append(q1.lebel[(index + int(num))%26]) 
        else :
            index = q1.lebel.index(e.lower())
            ans.append(q1.lebel[(index + int(num))%26].upper())
        count += 1
    for i in range(abs(count%q2.size() - q2.size())):
        num = q2.dequeue()
        q2.enqueue(num)
    
    return ans

def decodemsg(q1, q2):
    newL = encodemsg(q1, q2)
    print(f"Encode message is :  {newL}")
    q1.items = newL

    ans = []
    for e in q1.items:
        num = q2.dequeue()
        q2.enqueue(num)
        if e in q1.lebel:
            index = q1.lebel.index(e)
            ans.append(q1.lebel[(index - int(num))%26]) 
        else :
            index = q1.lebel.index(e.lower())
            ans.append(q1.lebel[(index - int(num))%26].upper())   
    print(f"Decode message is :  {ans}")


string, number = input("Enter String and Code : ").split(',')

q1 = Queue(string)
q2 = Queue(number)

encodemsg(q1, q2)
decodemsg(q1, q2)