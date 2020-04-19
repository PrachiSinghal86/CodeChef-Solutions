# cook your dish here
t=int(input())
while(t):
    t-=1
    dict={}
    n=int(input())
    c=0
    while(n):
        s=input()
        n-=1
        if s in dict:
            c+=(dict[s]//2)
        else:
            cr=s[0]
            f=2
            l=len(s)
            for j in range(1,l):
                if (cr=='j' or cr=='k') and (s[j]=='j' or s[j]=='k'):
                    f=f+4
                elif (cr=='j' or cr=='k') and (s[j]=='d' or s[j]=='f'):
                    f=f+2
                elif( cr=='d' or cr=='f') and (s[j]=='j' or s[j]=='k'):
                    f=f+2
                else:
                    f=f+4
                
                cr=s[j]
            dict[s]=f
            c=c+f
            
    print(c)
                    
                    
            
        