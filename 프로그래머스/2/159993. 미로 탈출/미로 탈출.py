from collections import deque

def bfs(maps, start, target):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    h = len(maps)
    w = len(maps[0])

    # 큐를 [start]로 감싸서 튜플로 저장
    queue = deque([start])
    visited = [[-1] * w for _ in range(h)]  # 방문한 곳의 거리를 기록 (-1로 초기화)
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        if (x, y) == target:  # 목표 지점에 도달한 경우
            return visited[x][y]  # 최단 거리 반환

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return -1  # 목표에 도달할 수 없는 경우 -1 반환

def solution(maps):
    # maps를 리스트의 리스트로 변환 (문자열을 리스트로 변환)
    maps = [list(row) for row in maps]

    start = None
    lever = None
    exit = None

    for i in range(len(maps)):
        for j in range(len(maps[0])):  # 열 크기만큼 순회하도록 수정
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)

    # BFS로 출발점에서 레버까지의 거리
    to_lever = bfs(maps, start, lever)
    # BFS로 레버에서 출구까지의 거리
    to_exit = bfs(maps, lever, exit)

    # 둘 중 하나라도 -1이면 -1을 반환
    if to_lever == -1 or to_exit == -1:
        return -1
    else:
        return to_lever + to_exit

# 테스트 호출
print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
