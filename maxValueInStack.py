class item:
    def __init__(self, value: int):
        self.value = value
        self.count = 1
    def add(self, addNumber):
        self.count += addNumber

class stack:
    def __init__(self) -> None:
        self.data = []
        self.max = float('-inf')
        self.maxStack = [item(float('-inf'))]
    def push(self, element:int):
        if element >= self.max:
            if self.maxStack[-1].value == element:
                self.maxStack[-1].add(1)
            else:
                self.maxStack.append(item(element))
            self.max = element
        self.data.append(element)
    def pop(self):
        if len(self.data):
            if self.max == self.data[-1]:
                self.maxStack[-1].add(-1)
                if self.maxStack[-1].count == 0:
                    self.maxStack.pop()
                self.max = self.maxStack[-1].value
            return(self.data.pop())
        else:
            return None
    def peek(self):
        if len(self.data):
            return self.data[-1]
        else:
            return None
    def getMax(self):
        return self.max

def main():
    s = readStack()
    print(s.getMax())
    
    s.pop()
    print(s.getMax())
    s.pop()
    print(s.getMax())
    s.push(4)
    s.push(5)
    print(s.getMax())
    s.push(5)
    s.push(5)
    s.push(5)
    print(s.getMax())
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print(s.getMax())
    s.pop()
    s.pop()
    print(s.getMax())
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print(s.getMax())
    s.push(10)
    print(s.getMax())


def readStack():
    tokens = input().split(' ')
    s = stack()
    for t in tokens:
        s.push(int(t))
    return s
if __name__ == '__main__':
    main()