
from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue=deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

bfs()

result = 0
for row in box:
    for value in row:
        if value == 0:
            print(-1)
            exit(0)
        result = max(result, value)

print(result-1)