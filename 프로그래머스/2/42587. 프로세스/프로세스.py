from collections import deque
def solution(priorities, location):
    p = deque(priorities)
    location_priority = priorities[location]
    p[location] = -1
    cnt = 0
    start = True
    while start:
        w = max(p)
        top = max(w, location_priority)
        a = p[0]
        if a == -1 and top == location_priority:
            cnt+=1
            start=False
        elif a < top:
            p.popleft()
            p.append(a)
        elif a == top:
            p.popleft()
            cnt+=1
    return cnt