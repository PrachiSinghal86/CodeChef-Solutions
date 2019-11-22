# cook your dish here
t=int(input())
for i in range(t):
    n,c=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    if s>c:
        print("No")
    else:
        print("Yes")