import itertools
N, M = map(int, input().split(' '))

card_numbers = list(map(int, input().split(' ')))
card_combination_list = itertools.combinations(card_numbers, 3)
card_sum = []


for i in list(card_combination_list):
    if sum(i) <= M:
        card_sum.append(sum(i))
print(max(card_sum))