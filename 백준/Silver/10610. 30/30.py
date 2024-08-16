n = input()
n_sum = 0

if '0' not in n:
    print(-1)
else:
    for i in range(len(n)):
        n_sum+= int(n[i])

    if n_sum % 3 != 0:
        print(-1)
    else:
        sorted_num = sorted(n, reverse=True)
        print("".join(sorted_num))