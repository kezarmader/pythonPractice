class Node:
    def __init__(self, value=0, prev=None, next=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

def main():
    L1 = readList()
    L2 = readList()

    R:Node = merge(L1, L2)

    printList(R)
    printListBack(R)

def merge(L1:Node, L2:Node):
    R:Node = Node()
    RL:Node = R

    while (L1 != None and L2 != None):
        if L1.value < L2.value:
            RL.next = L1
            L1.prev = RL
            L1 = L1.next
        else:
            RL.next = L2
            L2.prev = RL
            L2 = L2.next
        RL = RL.next
    
    if L1 == None:
        RL.next = L2
        L2.prev = RL
    else:
        RL.next = L1
        L1.prev = RL

    R.next.prev = None
    return R.next

def printList(L:Node):
    T:Node = L
    while (T != None):
        print(T.value, end=' -> ')
        T = T.next
    print()

def printListBack(L:Node):
    T:Node = L
    while (T.next != None):
        T = T.next
    
    while (T != None):
        print(T.value, end=' -> ')
        T = T.prev
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
            T.next = Node(int(t), T)
            T = T.next
    return L

if __name__ == '__main__':
    main()