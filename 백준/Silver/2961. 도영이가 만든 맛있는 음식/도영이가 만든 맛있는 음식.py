import sys

N = int(sys.stdin.readline())
ingredients = []
for i in range(N):
    S, B = map(int, sys.stdin.readline().split())
    ingredients.append((S, B))

min_diff = sys.maxsize
for i in range(1, 2**N):  # 모든 조합 탐색
    s_mul, b_sum = 1, 0
    cnt = 0  # 선택된 재료의 수를 세기 위한 변수
    for j in range(N):
        if i & (1 << j):  # j번째 재료가 선택되었는지 확인
            s_mul *= ingredients[j][0]
            b_sum += ingredients[j][1]
            cnt += 1
    if cnt > 0 and abs(s_mul - b_sum) < min_diff:  # 쓴맛이 0인 경우 제외
        min_diff = abs(s_mul - b_sum)

print(min_diff)
