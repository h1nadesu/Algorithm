import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
dp_max = arr
dp_min = arr

for _ in range(N - 1):
    arr = list(map(int, sys.stdin.readline().split()))
    dp_max = [arr[0] + max(dp_max[0], dp_max[1]), arr[1] + max(dp_max[0], dp_max[1], dp_max[2]), arr[2] + (max(dp_max[1], dp_max[2]))]
    dp_min = [arr[0] + min(dp_min[0], dp_min[1]), arr[1] + min(dp_min[0], dp_min[1], dp_min[2]), arr[2] + (min(dp_min[1], dp_min[2]))]

print(max(dp_max), min(dp_min))