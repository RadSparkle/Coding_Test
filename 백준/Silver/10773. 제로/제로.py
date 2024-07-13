K = int(input())

account = []
for _ in range(K):
    n = int(input())

    if n == 0 :
        account.pop()
    else:
        account.append(n)
print(sum(account))