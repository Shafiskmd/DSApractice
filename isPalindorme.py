def ispalindrome(string):
    string1=""
    for i in string:
        if i.isalnum():
            i=i.lower()
            string1+=i
    i=0
    j=len(string1)-1
    while i<=j:
        if string1[i]!=string1[j]:
            return False
        i+=1
        j-=1
    return True

s = "A man, a plan, a canal: Panama"
out=ispalindrome(s)
print(out)