import sys

a, b, c = map(int, sys.stdin.readline().split())

if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
    print(1)
elif a == b == c:
    print(2)
else:
    print(0)