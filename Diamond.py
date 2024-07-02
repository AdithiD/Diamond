def diamond1(s1):
    len1 = len(s1)
    for i in range(1,len1,1):
        print(s1[0:i])
    for j in range(1,len1,1):
        print(s1[0:len1-j])

s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
diamond1(s1)

def diamond2(s1):
    len1 = len(s1)
    for i in range(1,len1+1,1):
        print(s1[0:-i])
    for j in range(1,len1+1,1):
        print(s1[0:j-len1])

s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
diamond2(s1)


