from collections import deque


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
# Initialize and allocate memory for tree nodes
firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)
fourthNode = Node(4)
fifthNode=Node(5)
sixthNode=Node(6)
seventhNode=Node(7)
eighthNode=Node(8)
ninthhNode=Node(9)

# Connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode
secondNode.right=fifthNode
thirdNode.left=sixthNode
thirdNode.right=seventhNode
sixthNode.left=eighthNode
sixthNode.right=ninthhNode
total=0
def sumNodes(root):
    if root is None:
        return 0
    l=sumNodes(root.left)
    r=sumNodes(root.right)
    return l+r+root.data
output=sumNodes(firstNode)
print(output)