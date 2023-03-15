a, b, c = map(int,input().split())

time = [[] for _ in range(100)]
answer = 0
for _ in range(3):
    x,y = map(int,input().split())
    for i in range(x,y):
        time[i].append(1)
for i in time:
    if sum(i) == 1:
        answer += sum(i)*a
    elif sum(i) ==2:
        answer += sum(i)*b
    elif sum(i) ==3:
        answer += sum(i)*c
    else :
        answer +=0
print(answer)