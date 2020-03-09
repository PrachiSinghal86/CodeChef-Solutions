# cook your dish here

t=int(input())

for i in range(t):

    n=int(input())

    a=list(map(int,input().split()))

    a.sort()

    m=999999999

    for j in range(n-1):

        if a[j+1]-a[j]<m:

            m=a[j+1]-a[j]

        if m==0:

            break

    print(m)
        