bingo = [list(map(int,input().split())) for _ in range(5)]
numbers = []
for _ in range(5):
    numbers+=list(map(int, input().split()))
number_cnt = 0

def check():
    bingo_cnt = 0
    for i in bingo:
        if i.count(0) == 5:
            bingo_cnt+=1

    for i in range(5):
        cnt = 0
        for k in range(5):
            if bingo[k][i] == 0:
                cnt+=1
        if cnt == 5:
            bingo_cnt+=1

    d1 = 0
    for i in range(5):
        if bingo[i][i] == 0:
            d1+=1
    if d1 == 5:
        bingo_cnt+=1

    d2 = 0
    for i in range(5):
        if bingo[i][4-i] == 0:
            d2 += 1
    if d2 == 5:
        bingo_cnt +=1

    return bingo_cnt

for i in range(25):
    for x in range(5):
        for y in range(5):
            if numbers[i] == bingo[x][y]:
                bingo[x][y] = 0
                number_cnt+=1
    if number_cnt >= 12:
        result = check()
        if result >= 3:
            print(i+1)
            break


