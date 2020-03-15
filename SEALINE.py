# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=[]
    c=0
    s.append(1)
    for k in range(1,n):
        if a[k]==0:
            s.insert(0,k+1)
        else:
            ind=s.index(a[k])
            s.insert(ind+1,k+1)
            if ind+1<=k-ind-1:
                c+=ind+1
                
                
            else:
                c=c+k-ind-1

    print(c)
    
    