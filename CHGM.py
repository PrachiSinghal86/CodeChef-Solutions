# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mt=0
    mp=0
    for j in range(n):
        mt=mt+a[j]
        if mt<0:
            mt=0
        if mt>mp:
            mp=mt
    print(mp)
            