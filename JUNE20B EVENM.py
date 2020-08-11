# cook your dish here
t=int(input())
while t:
    t-=1
    n=int(input())
    a=[]
    
    m=1
    f=0
    for i in range(n):
        s=[]
        if(f==0):
            for j in range(m,m+n):
                s.append(j)
            a.append(s)
            
            m=m+n
            if(n%2==0):
                f=1
        else:
            for j in range(m+n-1,m-1,-1):
                s.append(j)
            a.append(s)
            m=m+n
            f=0
    for i in range(n):
        for j in range(n):
            print(a[i][j],end=" ")
        print()