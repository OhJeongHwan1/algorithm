import sys

input=sys.stdin.readline

minions = []

for i in range(9):
    minions.append(int(input()))

minions.sort()

noMinions = sum(minions) - 100
found = False
for i in range(9):
    if found == True:
        break
    for j in range(9):
        if(i != j):
            sum = minions[i]+minions[j]
            if(sum == noMinions):
                minions[i] = 0
                minions[j] = 0
                found = True
                break
            sum = 0

for minion in minions:
    if(minion != 0):
        print(minion)