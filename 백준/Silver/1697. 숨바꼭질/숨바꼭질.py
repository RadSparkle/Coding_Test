from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
MAX = 100001

def bfs(n):
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for i in (x-1, x+1, x*2):
            if 0 <= i < MAX and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)
print(bfs(n))