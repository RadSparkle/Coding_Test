n, m = map(int, input().split())
money_list = list(map(int, input().split()))

window_len = m
window = 0

for i in range(window_len):
    window += money_list[i]

MAX = window
start = 0
end = m

while end < len(money_list):
    window -= money_list[start]
    window += money_list[end]
    start += 1
    end += 1
    if window > MAX:
        MAX = window
print(MAX)