# cook your dish here
t=int(input())
while t:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    if s<0:
        print("NO")
    else:
        print("YES")