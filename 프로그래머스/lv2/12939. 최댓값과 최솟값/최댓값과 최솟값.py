def solution(s):
    return str(min([int(i) for i in s.split(" ")])) + " " + str(max([int(i) for i in s.split(" ")]))