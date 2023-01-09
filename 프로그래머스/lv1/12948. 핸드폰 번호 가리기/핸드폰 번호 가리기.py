def solution(phone_number):
    num_list = list(phone_number)
    num_hidden = num_list[:5]
    num_open = ''.join(s for s in num_list[-4:])
    
    result = "*" * len(num_list[4:]) + num_open

    return result
    