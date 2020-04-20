# cook your dish here
t=int(input())
while(t):
    t-=1
    a,b=map(int,input().split())
    l=0
    bo=0
    i=1
    while 1:
        if a>=l+i:
            l=l+i
            i=i+1
        else:
            print("Bob")
            break
        if b>=bo+i:
            bo=bo+i
            i+=1
        else:
            print("Limak")
            break