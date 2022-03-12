class TreeNode:
    def __init__(self, value=0, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right
    def insert(self, value):
        foundNode = self.search(value)
        if value <= foundNode.value:
            foundNode.left = TreeNode(value)
        else:
            foundNode.right = TreeNode(value)
    def delete(self, value):
        pass
    def search(self, value):
        curr = self
        while curr:
            if value <= curr.value:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        return prev
    def __str__(self) -> str:
        return self.getPreOrder(self, '')
    def getPreOrder(self, node, result):
        print(node.value)
        if node == None:
            return result

        result += node.value
        print(node.value + '-')
        result = self.getPreOrder(node.left, result)
        result = self.getPreOrder(node.right, result)
        return result


def main():
    root:TreeNode = buildBST()
    print(root)

def buildBST():
    root = TreeNode(12)
    root.insert(11)
    root.insert(10)
    root.insert(20)
    root.insert(14)
    root.insert(5)
    root.insert(0)
    return root