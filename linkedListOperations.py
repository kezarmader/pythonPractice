from typing import List


class ListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
    def display(self):
        if self.next:
            return str(self.data) + ' --> ' + self.next.display()
        else:
            return str(self.data) + ' --> X'
    def __str__(self):
        return self.display()


#search, insert and delete
class Solution:
    def main(self):
        start = ListNode(10)

        next = start
        for i in range(20, 100, 10):
            next.next = ListNode(i)
            next = next.next
        print(start)
        print(self.search(start, 50).data)
        self.insert(start, 4, 55)
        print(start)
        start = self.delete(start, 55)
        start = self.delete(start, 10)
        start = self.delete(start, 10)
        start = self.delete(start, 90)
        start = self.delete(start, 90)
        print(start)
    
    def delete(self, start:ListNode, element: int):
        if start.data == element:
            start = start.next
            return start

        prev = start
        head = start.next
        while(head != None):
            if head.data == element:
                break
            prev = head
            head = head.next

        if head and prev:    
            prev.next = head.next

        return start

    def insert(self, start:ListNode, position:int, element: int):
        head = start
        for i in range(position):
            if head == None or i == position:
                break
            head = head.next
        
        newElement = ListNode(element)

        newElement.next = head.next
        head.next = newElement

        return newElement

    def search(self, start:ListNode, element: int):
        while(start != None):
            if start.data == element:
                return start
            start = start.next
        return start

if __name__ == '__main__':
    Solution().main()