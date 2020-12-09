import re
import math

data = [list(x.rstrip()) for x in open("6").readlines()]
print(data)
res = [[]]
while len(data) > 0:
    x = data.pop()
    if x != []:
        res[-1] += x
    else:
        res.append([])

i = 0
count = 0

while i < len(res):
    count += len(set(res[i]))
    i += 1

print(count)