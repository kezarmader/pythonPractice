from collections import defaultdict
from collections import deque

class Solution:
    def __init__(self, parentChildPairs, n):
        self.revGraph = defaultdict(list)
        for pair in parentChildPairs:
            self.revGraph[pair[1]].append(pair[0])
        self.n = n
        
    def lca(self, node1, node2):
        Q = deque([(node1, node1), (node2, node2)])

        visited = [-1] * self.n
        
        visited[node1] = node1
        visited[node2] = node2

        self.revGraph[node1]

        while len(Q):
            (node, ancestor) = Q.pop()
            for neighbour in self.revGraph[node]:
                if (visited[neighbour] == -1):
                    visited[neighbour] = ancestor
                    Q.appendleft((neighbour, ancestor))
                elif visited[neighbour] != visited[node]:
                    if len(self.revGraph[neighbour]) > 0 or visited[neighbour] != neighbour:
                        return True

        return False

def main():
    parentChildPairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),(4, 8), (4, 9), (9, 11), (14, 4), (13, 12),(12, 9),(15, 13)]
    graph = Solution(parentChildPairs, 16)

    print(graph.lca(3, 8) == False)
    print(graph.lca(5, 8) == True)
    print(graph.lca(6, 8) == True)
    print(graph.lca(6, 9) == True)
    print(graph.lca(1, 3) == False)
    print(graph.lca(3, 1) == False)
    print(graph.lca(7, 11) == True)
    print(graph.lca(6, 5) == True)
    print(graph.lca(5, 6) == True)
    
    parentChildPairs = [(1, 3), (11, 10), (11, 12), (2, 3), (10, 2),(10, 5), (3, 4), (5, 6), (5, 7), (7, 8)]

    graph = Solution(parentChildPairs, 13)

    print(graph.lca(4, 12) == True)
    print(graph.lca(1, 6) == False)
    print(graph.lca(1, 12) == False)
    
if __name__ == '__main__':
    main()