T = int(input())
i = 0
case = []
while i < T :
    A, B = map(int, input().split())
    case.append(A+B)
    i+=1

for k in case :
    print(k)
