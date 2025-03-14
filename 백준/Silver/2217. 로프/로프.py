import sys

N = int(sys.stdin.readline())

weight = list(int(sys.stdin.readline()) for _ in range(N))

weight.sort(reverse = True)

for i in range(N):
    weight[i] = weight[i] * (i + 1)

print(max(weight))