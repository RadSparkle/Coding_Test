from collections import deque

def solution(people, limit) :
    answer = 0
    people.sort(reverse=True)
    people = deque(people)

    while people:
        if len(people) == 1 :
            answer+=1
            people.pop()
            break
        a = people.pop()
        b = people.popleft()
        if a + b > limit:
            people.append(a)
            answer+=1
        else :
            answer+=1
    return answer