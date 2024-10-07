from collections import deque

t = int(input())
a = 0

dx = [0, 0, 1, -1]
dy = [1, -1 ,0 , 0]
def bfs(xa, ya):
    queue = deque()
    queue.append((xa, ya))
    while queue:
        x, y = queue.popleft()
        field[x][y] = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0<= ny < m and field[nx][ny] != 0:
                field[nx][ny] = 0
                queue.append((nx, ny))
    return 1

while a < t:
    cnt = 0
    m, n, k = map(int, input().split())

    field = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                cnt+=bfs(i, j)
    print(cnt)
    a+=1