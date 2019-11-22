# cook your dish here
t = int(input())
for i in range(t):
    e = 0
    f = 0
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for j in range(n):
        if (e + a[j]) < k:

            print("NO", end=" ")
            print(j + 1)
            f = 1
            break
        else:
            e = e + a[j] - k

    if f == 0:
        print("YES")

