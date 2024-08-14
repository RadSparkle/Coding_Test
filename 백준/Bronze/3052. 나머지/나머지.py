a = list()
result = 0

for _ in range(10):
    k = int(input())
    a.append(k%42)

a = set(a)
print(len(a))