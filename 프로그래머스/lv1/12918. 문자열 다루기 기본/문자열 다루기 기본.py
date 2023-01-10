import re

def solution(s):
    pattern = re.compile('[a-zA-Z]')
    if pattern.findall(s) == [] and (len(s) ==4 or len(s) ==6):
        return True
    else :
        return False
    