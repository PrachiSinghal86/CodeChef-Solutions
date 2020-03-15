# cook your dish here
t=int(input())
for i in range(t):
    n,l=map(int,input().split())
    a=list(map(int,input().split()))
    s=a[0]
    ns=1
    k=0
    a.sort()
    while(k+ns<=n):
        if a[k+ns-1]-a[k]<=l:
            d=1
            while (k+ns-1+d)<n and a[k+ns-1+d]-a[k]<=l:
                d=d+1
            if ns+d-1>=ns:
                ns=ns+d-1
                s=a[k]
        k=k+1
    print(ns,"",s)
                