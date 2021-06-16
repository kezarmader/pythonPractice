from typing import List


class ListNode:
    def __init__(self, value:str='', next=None):
        self.value = value
        self.next = next
    def __str__(self) -> str:
        result = ''
        c = self
        buffer = {}
        while(c != None and buffer.get(c) == None):
            result += c.value + ' -> '
            buffer[c] = c
            c = c.next
        return result

def main():
    L:ListNode = readList()
    
    L.next.next.next.next.next.next = L
    print(L)

    if L == None or L.next == None:
        print(None)
        return

    C = L.next
    D = L.next.next
    while D != None and D.next != None:
        if(C == D):
            break
        C = C.next
        D = D.next.next

    if C == D:
        C = L
        while C != D:
            C = C.next
            D = D.next
        print(C)
    else:
        print(None)

def readList():
    tokens = input().split(' ')
    DH = C = ListNode()

    for t in tokens:
        C.next = ListNode(t)
        C = C.next

    return DH.next

if __name__ == '__main__':
    main()