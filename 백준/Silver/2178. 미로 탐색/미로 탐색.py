from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx, ny))
    return maze[N-1][M-1]



N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(bfs(0, 0))

