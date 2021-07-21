a=[]
for i in range(9):
    a.append(int(input()))

import itertools

for lists in itertools.combinations(a,7):
    if sum(lists)==100:
        lists = sorted(list(lists))
        for data in lists:
            print(data)
        break
