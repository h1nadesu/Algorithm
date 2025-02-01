import sys

n = int(sys.stdin.readline())
fib = [0] * (n + 1)

if n != 0:
    fib[1] = 1

if n not in [0, 1]:
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

print(fib[n])