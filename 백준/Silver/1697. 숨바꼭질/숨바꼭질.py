from collections import deque

def bfs(n, k):
    queue = deque()
    queue.append(n)
    visited = [False] * 100001  # 0부터 100000까지 총 100001개
    visited[n] = True
    time = 0

    while queue:
        size = len(queue)
        for i in range(size):
            cur = queue.popleft()
            if cur == k:
                return time
            if cur - 1 >= 0 and not visited[cur - 1]:
                queue.append(cur - 1)
                visited[cur - 1] = True
            if cur + 1 <= 100000 and not visited[cur + 1]:
                queue.append(cur + 1)
                visited[cur + 1] = True
            if cur * 2 <= 100000 and not visited[cur * 2]:
                queue.append(cur * 2)
                visited[cur * 2] = True
        time += 1

n, k = map(int, input().split())
print(bfs(n, k))
