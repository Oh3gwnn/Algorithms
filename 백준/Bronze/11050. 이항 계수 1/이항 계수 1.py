from itertools import combinations
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
print(len(list(combinations(range(1, a+1), b))))