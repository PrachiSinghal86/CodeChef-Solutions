# cook your dish here
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    if l[1]+l[2]+l[3]<=l[0]:
        print(1)
    elif l[1]+l[2]<=l[0] or l[2]+l[3]<=l[0]:
        print(2)
    else:
        print(3)