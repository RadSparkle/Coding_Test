def solution(price, money, count):
    pay = 0
    for i in range(1,count+1) :
        pay+=price * i
    result = pay - money
    if result <= 0 :
        return 0
    return result
