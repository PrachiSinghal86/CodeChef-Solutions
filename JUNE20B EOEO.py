# cook your dish here
t=int(input())
while t:
    t-=1
    n=int(input())
    c=1
    if n%2!=0:
        print(n//2)
    else:
        x=n
        while n%2==0:
            n=n//2
            c=c*2
        c=c*2
        c=x//c
        print(c)
            