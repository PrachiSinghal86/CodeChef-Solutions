# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=1
    for j in range(1,n):
        k=j-1
        f=0
        while(k>=j-5 and k>=0):
            if a[k]<=a[j]:
                f=1
                break
            k=k-1
        if f==0:
            c=c+1
    print(c)