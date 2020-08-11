# cook your dish here
t=int(input())
while t:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    c=[0]*3
    h=0
    for i in range(n):
        if a[i]==5:
            c[0]+=1
        elif a[i]==10:
            if c[0]==0:
                print("NO")
                h=1
                break
            else:
                c[1]+=1
                c[0]-=1
        else:
            if c[1]==0 and c[0]<2:
                print("NO")
                h=1
                break
            elif c[1]>0:
                c[1]-=1
                c[2]+=1
            else:
                c[0]-=2
                c[2]+=1
    if h==0:
        print("YES")
                