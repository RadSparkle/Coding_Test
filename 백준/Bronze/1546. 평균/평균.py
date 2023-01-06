n = int(input())
score_list = list(map(int,input().split()))
fake_list = []
m = max(score_list)

for i in range(n) :
    fake_list.append(score_list[i]/m*100)

fake_score = sum(fake_list)
result = fake_score/n

print(result)
