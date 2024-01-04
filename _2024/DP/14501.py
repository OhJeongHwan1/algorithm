import sys

input=sys.stdin.readline

N = int(input())
schedule = []

for i in range(N):
    schedule.append(list(map(int,(input().split()))))

print(schedule)