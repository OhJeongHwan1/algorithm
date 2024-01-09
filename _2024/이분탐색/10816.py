import sys

input = sys.stdin.readline

def find_first(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def find_last(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

def count_occurrences(arr, target):
    first = find_first(arr, target)
    last = find_last(arr, target)
    return max(0, last - first + 1)

N = int(input())
myCard = sorted(map(int, input().split()))

M = int(input())
checkCards = list(map(int, input().split()))

for target in checkCards:
    print(count_occurrences(myCard, target), end=' ')
