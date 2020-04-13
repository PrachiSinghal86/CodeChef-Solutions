# cook your dish here
n=int(input())
m=n
s=[]
while(m):
    m-=1
    s.append(input().strip())
s.sort()
c=1
i=0
while i<n:
    while i+1<n and s[i]==s[i+1]:
        i=i+1
        c=c+1
    print(s[i],c)
    c=1
    i=i+1