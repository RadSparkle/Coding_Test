N = int(input())
s = 0
a = 0
count = 0

while True:
    a += 1
    s += a
    count+=1
    if s > N:
        break
print(count-1)