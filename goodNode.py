from collections import deque


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
# Initialize and allocate memory for tree nodes
firstNode = Node(4)
secondNode = Node(2)
thirdNode = Node(7)
fourthNode = Node(1)
fifthNode=Node(3)
sixthNode=Node(6)
seventhNode=Node(9)


# Connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode
secondNode.right=fifthNode
thirdNode.left=sixthNode
thirdNode.right=seventhNode
def goodNode(root):
    nodes=[]
    def dfs(root,max_):
        nonlocal nodes
        if root is None:
            return 0
        count=0
        if root.data>=max_:
            count+=1
            nodes.append(root.data)
            max_=root.data
        left=dfs(root.left,max_)
        right=dfs(root.right,max_)
        return count+left+right
    dfs(root,float("-inf"))
    return nodes
print(goodNode(firstNode))


        