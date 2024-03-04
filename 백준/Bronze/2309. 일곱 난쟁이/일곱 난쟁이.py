from itertools import combinations

dwarf_list = []

for i in range(9):
    dwarf_list.append(int(input()))



for i in list(combinations(dwarf_list, 7)):
    sum_heigh = sum(i)
    if sum_heigh == 100:
        for s in sorted(i):
            print(s)
        break
    

