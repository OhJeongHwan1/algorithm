# 1043 거짓말 골4

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
honest_people_list = list(map(int,input().split()))
parties = []
result = 0

for _ in range(M):
    parties.append(list(map(int,input().split())))

if honest_people_list[0] == 0:
    print(M)
    exit()
else:
    honest_people_list.pop(0)

honest_people = set(honest_people_list)
cant_parties = []
while True:
    count = 0
    for party in parties:
        if party != False:
            delete = False
            for i in range(1,len(party)):
                if party[i] in honest_people:
                    for j in range(1,len(party)):
                        honest_people.add(party[j])
                    delete = True
                    count += 1
                    break
            if delete == True:
                cant_parties.append(party)

    if count == 0:
        break

    for i in range(len(parties)):
        if parties[i] in cant_parties:
            parties[i] = False

#print(cant_parties)
count = 0
for party in parties:
    if party == False:
        count += 1
print(M - count)

