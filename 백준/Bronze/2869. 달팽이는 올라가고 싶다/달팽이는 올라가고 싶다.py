#반복+조건문 시간초과
import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

tmp = (v-b)/(a-b)

print(int(tmp) if tmp == int(tmp) else int(tmp)+1)