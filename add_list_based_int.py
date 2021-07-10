from typing import List


class ListNode():
    def __init__(self, value = 0, next = None) -> None:
        self.value = value
        self.next = next
    def __str__(self):
        result = ' -> '
        current = self
        while current:
            result += str(current.value) + ' -> '
            current = current.next
        result += '[x]'
        return result

def main():
    fNum = readList()
    sNum = readList()
    rNum = add(fNum, sNum)
    print(rNum)

def add(fNum, sNum) -> ListNode:
    rNumHead = rNum = ListNode()
    carry = 0
    while fNum and sNum:
        result = carry + fNum.value + sNum.value
        rNum.next = ListNode(result % 10)
        carry = result // 10
        fNum = fNum.next
        sNum = sNum.next
        rNum = rNum.next
    while fNum:
        rNum.next = ListNode(fNum)
    while sNum:
        rNum.next = ListNode(sNum)
    if carry > 0:
        rNum.next = ListNode(carry)
    return rNumHead.next

def readList():
    tokens = input().split(' ')
    dummyHead = ListNode()
    current = dummyHead
    for t in tokens:
        current.next = ListNode(int(t))
        current = current.next
    return dummyHead.next

if __name__ == '__main__':
    main()