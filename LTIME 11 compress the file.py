# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    fl = 0
    a = list(map(int, input().split()))
    for j in range(n - 1):

        if (a[j] == a[j + 1] - 1):
            c = c + 1
            if fl == 0:
                l = a[j]
                fl = 1


        else:
            fl = 0
            if c < 1:

                print(a[j], end=",")
                c = 0
            elif c == 1:
                print(a[j - 1], end=",")
                print(a[j], end=",")
                c = 0
            else:
                c = 0
                print(l, end="...")
                print(a[j], end=",")
    if (c > 1 and a[n - 1] == a[n - 2] + 1):
        print(l, end="...")
        print(a[n - 1])
    elif c == 1:
        print(a[n - 2], end=",")
        print(a[n - 1])
    else:
        print(a[n - 1])
