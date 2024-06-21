coin = [500, 100, 50, 10, 5, 1]

price = 1000-int(input())
changes_cnt = 0

for i in coin:
    a, b = divmod(price, i)
    if a > 0:
        changes_cnt+=a
        price = b

print(changes_cnt)