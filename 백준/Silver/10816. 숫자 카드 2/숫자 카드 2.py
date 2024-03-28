import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

def lower_idx(target):
    high = N
    low = 0
    while low < high:
        mid = (low + high) // 2
        if target <= N_list[mid]:
            high = mid
        else:
            low = mid + 1
    return low

def upper_idx(target):
    high = N
    low = 0
    while low < high:
        mid = (low + high) // 2
        if target < N_list[mid]:
            high = mid
        else:
            low = mid + 1
    return low

for x in M_list:
    result = upper_idx(x) - lower_idx(x)
    print(result, end=' ')