data = [list(x.rstrip()) for x in open("6").readlines()]
print(data)
res = [{}]
while len(data) > 0:
    x = data.pop()
    if x != []:
        if res[-1] != {}:
            res[-1] = res[-1].intersection(set(x))
        else:
            res[-1] = set(x)
    else:
        res.append({})

print(res)

i = 0
count = 0

while i < len(res):
    count += len(set(res[i]))
    i += 1

print(count)