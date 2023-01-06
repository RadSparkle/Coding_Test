n = int(input())
result_list = []
for _ in range(n) :
    score_list = list(map(int,input().split()))
    student_count = score_list[0]
    score_list.pop(0)

    sum_score = sum(score_list)
    avg_score = int(sum_score / student_count)
    cnt = 0
    for i in score_list :
        if i > avg_score :
            cnt += 1
        result = (cnt / len(score_list)) * 100
    result_list.append(round(result,3))


for k in result_list :
    print(f'{k:.3f}',end='%\n')







