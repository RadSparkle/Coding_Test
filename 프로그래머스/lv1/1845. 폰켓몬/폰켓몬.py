def solution(nums):
    getPokets = int(len(nums) / 2)
    dictPoket = {}
    for i in nums:
        dictPoket[i] = i

    return len(dictPoket) if len(dictPoket) < getPokets else getPokets

