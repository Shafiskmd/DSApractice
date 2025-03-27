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

def DiameterLenght(root):
    total=0
    def dfs(root):
        nonlocal total
        if root is None:
            return 0
        l=dfs(root.left)
        r=dfs(root.right)
        total=max(total,r+l)
        return max(l,r)+1
    dfs(firstNode)
    print(total)
DiameterLenght(firstNode)