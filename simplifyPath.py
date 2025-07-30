def simplifyPath(path):
    stack=[]
    p=path.split("/")
    for i in p:
        if i=='..':
            if stack:
                stack.pop()

        elif i == '' or i=='.':
            continue
        else:
            stack.append(i)
    res="/"+"/".join(stack)
    print(res)


path = "/home/"
path1="/home/../foo/"
simplifyPath(path)
simplifyPath(path1)