k, n = map(int,input().split())
lan_list = []

for _ in range(k):
    lan_list.append(int(input()))

lan_avg = int(sum(lan_list) / n)

left, right= 1, max(lan_list)

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for i in lan_list:
        cnt+= i // mid
    if cnt >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)
