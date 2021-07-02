from __future__ import annotations

class ListNode:
    def __init__(self, value='', next=None) -> None:
        self.value = value
        self.next = next
    def __str__(self) -> str:
        result = ''
        temp = self
        while temp:
            result += temp.value + ' -> '
            temp = temp.next
        return result
    def removeDups(self) -> ListNode:
        first = self
        if not first or not first.next:
            return first
        
        second = first.next

        while second:
            if first.value == second.value:
                first.next = second.next
            else:
                first = first.next
            second = second.next
        return self


def readList():
    tokens = input().split(' ')
    temp = dummyHeader = ListNode()
    for t in tokens:
        temp.next = ListNode(t)
        temp = temp.next
    return dummyHeader.next

def main():
    L = readList()
    print(L)
    FL = L.removeDups()
    print(FL)
    

if __name__ == '__main__':
    main()