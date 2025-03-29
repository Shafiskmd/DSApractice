def simplifyPath(path):
    p=path.split("/")
    print(p)

path = "/home/"
path1="/home//foo/"
simplifyPath(path)
simplifyPath(path1)