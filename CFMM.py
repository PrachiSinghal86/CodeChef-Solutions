# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=""
    for j in range(n):
        p=input()
        s=s+p
    a=[0,0,0,0,0,0]
    a[0]=s.count('c')
    a[0]=int(a[0]/2)
    a[1] = s.count('o')
    a[2] = s.count('d')
    a[3] = s.count('e')
    a[3] = int(a[3] / 2)
    a[4] = s.count('h')
    a[5] = s.count('f')
    m=a[0]
    for j in range(6):
        if m>a[j]:
            m=a[j]
    print(m)