from collections import deque

n = int(input())
lst = deque()
for _ in range(n):
    lst.append(int(input()))

dasom = lst.popleft()
cnt = 0
while lst:
    max_value = max(lst)
    if dasom <= max_value:
        max_idx = lst.index(max_value)
        lst[max_idx] -= 1
        dasom+=1
        cnt+=1
    else:
        break
print(cnt)