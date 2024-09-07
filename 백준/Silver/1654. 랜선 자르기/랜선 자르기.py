n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

start = 1
end = max(lst)

while start<=end:
    mid = (start+end) // 2
    total = 0
    for i in lst:
        total += i // mid

    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)