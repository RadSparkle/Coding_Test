n = int(input())
drink = list(map(int,input().split()))
answer = 0
max_drink = max(drink)
for i in drink:
    if i == max_drink:
        continue
    else:
        answer+= float(i/2)
print(answer+max_drink)