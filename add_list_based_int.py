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
    while fNum or sNum or carry > 0:
        result = carry + (fNum.value if fNum else 0) + (sNum.value if sNum else 0)
        rNum.next = ListNode(result % 10)
        carry = result // 10
        fNum = fNum.next if fNum else None
        sNum = sNum.next if sNum else None
        rNum = rNum.next
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