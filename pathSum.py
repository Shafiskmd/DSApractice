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

def pathSum(root, target):
        res=[]
        def dfs(root,arr):
            if not root:
                return
            arr.append(root.data)
            if root.left is None and root.right is None:
                res.append(arr[:])
            
            dfs(root.left,arr[:])
            dfs(root.right,arr[:])
        dfs(root,[])
        out=[]
        for i in res:
            if sum(i)==target:
                out.append(i)
        return out
result=pathSum(firstNode,11)
print(result)