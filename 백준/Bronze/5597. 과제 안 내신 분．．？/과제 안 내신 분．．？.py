a = [0 for i in range(30)]
for _ in range(28):
    k = int(input())
    a[k-1] = 1

for i in range(30):
    if a[i] == 0:
        print(i+1)