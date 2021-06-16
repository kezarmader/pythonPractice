class ListNode:
    def __init__(self, value='', next=None):
        self.value = value
        self.next = next
    def __str__(self) -> str:
        result = ''
        c = self
        buffer = {}
        while (c != None and buffer.get(c) == None):
            buffer[c] = c
            result += c.value + ' -> '
            c = c.next
        if c:
            result += c.value + ' <- '
        return result
    def len(self) -> int:
        c = self
        buffer = {}
        count = 0
        while (c != None and buffer.get(c) == None):
            buffer[c] = c
            count += 1
            c = c.next
        return count
    def distance(self, endNode):
        length = 0
        temp = self
        while temp != endNode:
            length += 1
            temp = temp.next
        return length

def main():
    list1 = readList()
    list2 = readList()

    list1.next.next.next = list2.next.next.next
    list1.next.next.next.next = list1.next.next.next
    
    overlapedNode = findOverlapNodeWithCycles(list1, list2)
    print(overlapedNode)

def findOverlapNodeWithCycles(list1, list2):
    #find starting point of the cycles
    root1, root2 = findCycle(list1), findCycle(list2)

    #if no loops find the node using normal approach
    if not root1 and not root2:
        return findOverlapNodeWithoutCycles(list1, list2)
    
    #if only one have a loop then there's no connection
    if (not root1 and root2) or (root1 and not root2):
        return None

    #traverse the loop until we reach back to any of the root
    temp = root2
    while True:
        temp = temp.next
        if temp == root1 or temp == root2:
            break
    
    #if temp is not root1, that means there are 2 disconnected loops
    if temp is not root1:
        return None
    
    #If both lists have loops
    step_len1, step_len2 = list1.distance(root1), list2.distance(root2)

    if step_len1 > step_len2:
        list1, list2 = list2, list1
        step_len1, step_len2 = step_len2, step_len1

    #travel the loops distance
    for _ in range(step_len2 - step_len1):
        list2 = list2.next
    
    #travel both list until anyone loop start is met
    while list1 is not list2 and list1 is not root1 and list2 is not root2:
        list1, list2 = list1.next, list2.next
    
    #if list1 and list2 matches this is start of the connection
    #else it's the starting
    if list1 is list2:
        return list1
    else:
        return root1
 

def findCycle(L):
    C = D = L

    while D != None and D.next != None:
        C = C.next
        D = D.next.next

        if C == D:
            C = L
            while C != D:
                C = C.next
                D = D.next
            return C
    return None

def findOverlapNodeWithoutCycles(list1, list2):
    list1_len = list1.len()
    list2_len = list2.len()

    if list1_len > list2_len:
        list1_len, list2_len, list1, list2 = list2_len, list1_len, list2, list1

    for _ in range(list2_len - list1_len):
        list2 = list2.next
    
    while list1 and list2 and list1 is not list2:
        list1, list2 = list1.next, list2.next
    return list1

def readList():
    tokens = input().split(' ')
    dummyHead = ListNode()

    current = dummyHead
    for t in tokens:
        current.next = ListNode(t)
        current = current.next
    return dummyHead.next

if __name__ == '__main__':
    main()