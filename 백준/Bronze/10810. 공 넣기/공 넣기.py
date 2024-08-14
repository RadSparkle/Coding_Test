n, m = map(int, input().split())

a = [0 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())

    for i in range(i-1, j):
        a[i] = k

for i in a:
    print(i, end = ' ')