# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    j=0
    while(len(a)>=3):
        x=min(a[j],a[j+1],a[j+2])
        y=max(a[j],a[j+1],a[j+2])
        if a[j]!=x and a[j]!=y:
            a.remove(a[j])
        elif a[j+1]!=x and a[j+1]!=y:
            a.remove(a[j+1])
        else:
            a.remove(a[j+2])
    print(a[0],end=" ")
    print(a[1])
        
        