# cook your dish here
t=int(input())
while(t):
    s=input()
    t-=1
    l=len(s)
    up=0
    dw=0
    cr=s[0]
    if cr=='U':
        up=1
    else:
        dw=1
    
    for i in range(1,l):
        if cr!=s[i]:
            if s[i]=='U':
                up+=1
            else:
                dw=dw+1
            cr=s[i]
   
    m=min(up,dw)
    print(m)
        