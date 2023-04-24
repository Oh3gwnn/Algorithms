def solution(s):
    return "".join([i.lower().capitalize() + " " for i in s.split(" ")])[0:len(s)]