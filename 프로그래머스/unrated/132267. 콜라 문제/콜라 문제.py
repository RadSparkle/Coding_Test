def solution(a, b, n):
    answer = 0
    while n >= a :
        newCount = n // a * b
        leftOver = n % a
        answer += newCount
        n = leftOver + newCount
    return answer