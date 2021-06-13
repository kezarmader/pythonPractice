class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

def main():
    L1 = readList()
    L2 = readList()

    R:Node = merge(L1, L2)

    printList(R)

def merge(L1:Node, L2:Node):
    R:Node = None
    RL:Node = None

    while (L1 != None and L2 != None):
        if L1.value < L2.value:
            if R == None:
                R = L1
                RL = L1
            else:
                RL.next = L1
                RL = L1
            L1 = L1.next
        else:
            if R == None:
                R = L2
                RL = L2
            else:
                RL.next = L2
                RL = L2
            L2 = L2.next
    
    if L1 == None:
        RL.next = L2
    else:
        RL.next = L1
            
    return R

def printList(L:Node):
    T:Node = L
    while (T != None):
        print(T.value, end=' ')
        T = T.next
    print()

def readList():
    tokens = input().split(' ')
    
    L:Node = None
    
    T:Node = L
    for t in tokens:
        if L == None:
            L = Node(int(t))
            T = L
        else:
            T.next = Node(int(t))
            T = T.next
    return L

if __name__ == '__main__':
    main()