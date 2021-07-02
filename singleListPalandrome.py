class ListNode:
    def __init__(self, value='', next=None):
        self.value = value
        self.next = next
    def __str__(self):
        result = ''

        e = self
        while e:
            result += e.value + ' -> '
            e = e.next

        return result

def main():
    L = readList()
    print(isPalendrome(L))
    print(L)

def isPalendrome(L:ListNode) -> bool:
    fast = slow = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
    start_first_half, start_second_half = L, reverseList(slow)
    while start_first_half and start_second_half:
        if start_first_half.value != start_second_half.value:
            return False
        start_first_half, start_second_half = start_first_half.next, start_second_half.next
    
    return True

def reverseList(L):
    dummy_head = ListNode('', L)

    a = dummy_head.next
    while a and a.next:
        temp = a.next
        a.next = temp.next
        temp.next = dummy_head.next
        dummy_head.next = temp
        
    return dummy_head.next


def readList():
    tokens = input().split(' ')
    start = dummy = ListNode()
    
    for e in tokens:
        dummy.next = ListNode(e)
        dummy = dummy.next
    
    return start.next

if __name__ == '__main__':
    main()