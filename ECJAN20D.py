# cook your dish here
t=int(input())
while(t):
    t-=1
    n,q=map(int,input().split())
    h=[0]*100000
    s=[]
    a=list(map(int,input().split()))
    l=len(a)
    for k in range(l):
        
        if h[a[k]]==0:
            h[a[k]]=1
            s.append(a[k])
    while(q):
        q-=1
        d=list(map(int,input().split()))
        if d[0]==2:
            
            try:
                while(d[1]):
                    m=s.pop()
                    h[m]=0
                    d[1]-=1
            except:
                continue
        else:
        
            for k in range(2,d[1]+2):
                if h[d[k]]==0:
                    h[d[k]]=1
                    s.append(d[k])
    try:
        while(1):
            print(s.pop(),end=" ")
    except:
        print()
                
                
    
                
    