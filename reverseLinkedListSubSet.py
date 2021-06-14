class ListNode():
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next
    def __str__(self) -> str:
        result = ''
        while(self.next != None):
            result += str(self.value) + ' -> '
            self = self.next

        result += str(self.value) + ' -> {}'
        return result
    def at(self, index):
        S = self
        
        for i in range(1, index):
            if S:
                S = S.next
        return S
    def reverse(self, start, end):
        S = self.at(start - 1)
        buffer = []
        
        if S is None:
            return None
        C = S.next
        for i in range(1, start-end+1):
            if C:
                buffer.append(C)
                C = C.next
            else:
                return None

        S.next = C
        E = C.next
        
        item = buffer.pop()
        while len(buffer) > 0:
            C.next = item
            item = buffer.pop()
            C = C.next
        C.next = item
        C = C.next
        C.next = E
    def reverseE(self, start, end):
        H = SH = ListNode()
        SH = self.at(start)
        
        I = SH.next
        for _ in range(end - start):
            temp = I.next
            I.next = temp.next
            temp.next = SH.next
            SH.next = temp

        return H.next

            
def main():
    L = readList()
    start = int(input())
    end = int(input())

    L.reverseE(start,end)
    print(L)

def readList():
    L:ListNode = ListNode()
    C:ListNode = L

    tokens = input().split(' ')
    for t in tokens:
        C.next = ListNode(t)
        C = C.next
    
    return L.next


if __name__ == '__main__':
    main()