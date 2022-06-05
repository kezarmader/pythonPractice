'''
Build a tree from edges
[[1,2],[1,4],[2,3],[4,5],[4,6],[6,7],[6,8]]
'''

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.value = value
    def __str__(self):
        s = []

        self.postOrder(self, s)

        return ''.join(s)
    def postOrder(self, node, s):
        if node == None:
            return

        s.append(str(node.value))
        s.append(',')
        self.postOrder(node.left, s)
        self.postOrder(node.right, s)
        
def solution(edges):
    root = None
    nodes = {}

    for edge in edges:
        [source, destination] = edge
        if source not in nodes:
            nodes[source] = (TreeNode(source), None)
        if destination not in nodes:
            nodes[destination] = (TreeNode(destination), source)

        parent = nodes[source][0]
        child = nodes[destination][0]

        if parent.left:
            parent.right = child
        else:
            parent.left = child
    
    for value in nodes.values():
        if value[1] == None:
            return value[0]
    
    return None

print(solution([[1,2],[1,4],[2,3],[4,5],[4,6],[6,7],[6,8]]))
