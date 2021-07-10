class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = int(value)
        self.next = next
    def __str__(self):
        result = '[s]'
        current = self

        while current:
            result += ' -> ' + str(current.value)
            current = current.next

        return result

def main():
    list = readList()
    k = int(input())
    print(list, k)
    print(pivot(list, k))

def pivot(list, k):
    less = lessHead = LinkedList()
    eq = eqHead = LinkedList()
    more = moreHead = LinkedList()

    current = list
    while current:
        if current.value < k:
            less.next = current
            current = current.next
            less = less.next
            less.next = None
        elif current.value > k:
            more.next = current
            current = current.next
            more = more.next
            more.next = None
        else:
            eq.next = current
            current = current.next
            eq = eq.next
            eq.next = None

    less.next = eqHead.next
    eq.next = moreHead.next

    return lessHead.next

def readList():
    tokens = input().split(' ')
    dummyHead = LinkedList()

    current = dummyHead
    for t in tokens:
        current.next = LinkedList(t)
        current = current.next
    return dummyHead.next


if __name__ == '__main__':
    main()