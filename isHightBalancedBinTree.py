# is given tree a Heighted Binary Tree

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def main():
    root = inputTree()
    result = isBalancedHeighted(root)
    print(result)

def isBalancedHeighted(node):
    if node.left == None and node.right == None:
        return (0, True)
    
    if node.left == None or node.right == None:
        return (False, 0)

    (leftHeight, isLeftBalanced) = isBalancedHeighted(node.left)
    (rightHeight, isRightBalanced) = isBalancedHeighted(node.right)
    
    isBalanced = isLeftBalanced and isRightBalanced
    isBalanced = abs(leftHeight - rightHeight <= 1) and isBalanced

    height = max(leftHeight, rightHeight) + 1

    return (height, isBalanced)


def inputTree():
    #               0
    #       -1            1
    #   -2      -3      2   3
    node = Node('A')
    node.left = Node('B')
    node.left.left = Node('C')
    node.left.left.left = Node('D')
    node.left.left.left.left = Node('E')
    node.left.left.left.right = Node('F')
    node.left.left.right = Node('G')
    node.left.right = Node('H')
    node.left.right.left = Node('I')
    node.left.right.right = Node('J')
    node.right = Node('K')
    node.right.left = Node('L')
    node.right.left.left = Node('M')
    node.right.left.right = Node('N')
    node.right.right = Node('O')

    return node;

if __name__ == '__main__':
    main()