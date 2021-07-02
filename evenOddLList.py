from __future__ import annotations
from typing import List

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
    def mergeEvenOdd(self) -> ListNode:
        even_start, odd_start = ListNode(), ListNode()
        even = even_start
        odd = odd_start
        is_even = True
        el = self
        while el:
            if is_even:
                even.next = el
                even = even.next
            else:
                odd.next = el
                odd = odd.next
            el = el.next
            is_even = not is_even
            
        odd.next = None
        even.next = odd_start.next
        
        return even_start.next

def readList():
    tokens = input().split(' ')
    temp = dummyHeader = ListNode()
    for t in tokens:
        temp.next = ListNode(t)
        temp = temp.next
    return dummyHeader.next

def main():
    L = readList()
    print(L.mergeEvenOdd())
    

if __name__ == '__main__':
    main()