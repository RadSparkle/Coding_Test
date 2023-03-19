a = int(input())
t = int(input())
s = input()


answer = []
cnt=0

for i in range(2,100):
    answer.append('0')
    answer.append('1')
    answer.append('0')
    answer.append('1')
    for k in range(i):
        answer.append('0')
    for l in range(i):
        answer.append('1')
    if answer.count(s) > t :
        break
for idx,i in enumerate(answer):
    if i == s:
        cnt+=1
    if cnt == t:
        break
print(idx % a)