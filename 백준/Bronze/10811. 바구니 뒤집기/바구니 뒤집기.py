n , m = map(int, input().split())

a = list(range(1, n+1))
for _ in range(m):
    i, j = map(int, input().split())
    tmp = list(reversed(a[i-1:j]))
    a[i-1:j] = tmp

for i in a:
    print(i, end=' ')