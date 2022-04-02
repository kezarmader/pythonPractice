'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.


[1,2] => remove from end
insert => [3,1,2]
pick that element (find the element in the Q) and add to the start of the Q
read 1
[1, 3, 2]

1. Dictionary for lookups
2. Doubly Linked with Dictionary (Ordered Dictionary)

start <-> 1 <-> end

1
{1: node}
{2: node}

{1,1}
{2,2}
get 1
{3,3}

'''
class Node():
    def __init__(self, val=0, key=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}              # {1: (1), 2: (2)}
        self.start = Node()        # start <-> (1) <-> (2) <-> end
        self.end = Node()          
        self.start.next = self.end
        self.end.prev = self.start
    def get(self, key):
        if len(self.dic) == 0:
            return -1
        
        if key in self.dic:
            node = self.dic[key]
            
            # 1. remove me
            node.prev.next = node.next
            node.next.prev = node.prev
            # 2. add me to the start
            self.insertAfter(self.start, node)
            
            return node.val
        else:
            return -1
    def put(self, key, value):
        if len(self.dic) == self.capacity:
            #remove the last
            lastNode = self.end.prev
            self.end.prev = self.end.prev.prev
            self.start.next = self.start.next.next
            del self.dic[lastNode]
        
        # insert the new
        newNode = Node(value, key)
        self.insertAfter(self.start, newNode)
        self.dic[key] = newNode
            
    def insertAfter(self, node, newNode):    #start->end
        temp = node.next    #temp = end
        node.next = newNode # start <-> (1) <-> end
        newNode.next = temp # 

        temp.prev = newNode
        newNode.prev = node
    
def main():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))
    
    
if __name__ == '__main__':
    main()
    
    

    #   
    # 
    # 
4/5    
    
    
    
    
    
    
    
    
    
    