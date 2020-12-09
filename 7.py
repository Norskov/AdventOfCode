import re
data = [x.rstrip() for x in open("7").readlines()]

cols = dict()

for x in data:
    s = x.split(' ')
    c = s[0] + ' ' + s[1]
    i = 2
    cols[c] = dict()
    while i < len(s):
        if re.match('[0-9]+', s[i]):
            nc = s[i + 1] + ' ' + s[i + 2]
            cols[c][nc] = s[i]
        i += 1

count = 0

def contains(c):
    if c == 'shiny gold':
        return True
    else:
        for x in cols[c]:
            if contains(x):
                return True
    return False

for c in cols.keys():
    if contains(c):
        count += 1

def inside(c):
    if len(cols[c]) == 0:
        return 1
    else:
        sum = 1
        for x in cols[c]:
            sum += int(cols[c][x]) * inside(x)
        return sum

print(count - 1)
print(inside('shiny gold') - 1)