from collections import deque


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
arr=[]
res=[]
def pathLists(root,arr):
    arr.append(root.data)
    if root.left is None and root.right is None:
        res.append(arr)
        # print(res)
        return arr[:]
    pathLists(root.left,arr[:])
    pathLists(root.right,arr[:])
q=deque()
def levelOrder(root):
    if root:
        q.append(root)
        while q:
            # res.append([i.data for i in q][0])
            res.append([i.data for i in q][len(q)-1])
            # print([i.data for i in q])
            for _ in range(len(q)):
                
                
                num=q.popleft()
                if num.left:
                    q.append(num.left)
                if num.right:
                    q.append(num.right)
            






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
# output=pathLists(firstNode,[])
levelOrder(firstNode)
print(res)
