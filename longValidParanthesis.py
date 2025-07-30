def longvalid(s):
    stack=[]
    res=""
    map={")":"(","}":"{","]":"["}
    for c in s:
        if c in map:
            print(c)
            if stack and stack[-1]==map[c]:
                x=stack.pop()
                res+=x+c
        else:
            stack.append(c)
    return len(res)




s=")()())"
print(longvalid(s))