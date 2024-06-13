dice_number = list(map(int, input().split()))
dice_dict_tmp = set(dice_number)
dice_dict = {key: 0 for key in dice_dict_tmp}


for key in dice_dict:
    count_dice = dice_number.count(key)
    dice_dict[key] = count_dice

max_dice_number = max(dice_dict, key=dice_dict.get)

if dice_dict[max_dice_number] == 3:
    print(10000 + max_dice_number * 1000)
elif dice_dict[max_dice_number] == 2:
    print(1000 + (max_dice_number * 100))
elif dice_dict[max_dice_number] == 1:
    print(100 * max(dice_number))


