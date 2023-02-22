coin = [500,100,50,10,5,1]
money = 1000-int(input())
answer = 0
for i in coin:
    a,b = divmod(money, i)
    answer += a
    money = b
print(answer)