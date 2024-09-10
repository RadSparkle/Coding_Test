def solution(N, recommends):
    photo_frame = {}
    time = 0  # 학생들이 사진틀에 등록된 시간을 기록하는 변수

    for student in recommends:
        if student in photo_frame:
            photo_frame[student][0] += 1  # 추천 횟수 증가
        else:
            if len(photo_frame) >= N:  # 사진틀이 가득 찼을 때
                # 추천 횟수가 가장 적고, 오래된 학생 찾기
                to_remove = min(photo_frame.items(), key=lambda x: (x[1][0], x[1][1]))
                del photo_frame[to_remove[0]]  # 해당 학생 제거

            photo_frame[student] = [1, time]  # 새로운 학생 추가
        time += 1

    # 남은 학생들의 ID를 오름차순으로 출력
    result = sorted(photo_frame.keys())
    print(' '.join(map(str, result)))

N = int(input())
M = int(input())
recommends = list(map(int, input().split()))
solution(N, recommends)
