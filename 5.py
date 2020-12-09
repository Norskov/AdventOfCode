import re
import math

data = [x.rstrip() for x in open("5").readlines()]

def fun(d, x, y):
    if x % 2 != 0 or y % 2 != 1:
        print('ABORT')
    print(str(x) + ' ' + str(y) + ' ' + str(math.ceil((y-x)/2)))
    if len(d) == 0:
        return x
    a = d[0]
    b = d[1:]
    if re.match('F|L', a):
        if len(b) == 0:
            return x
        else:
            return fun(b, x, y - math.ceil((y-x)/2))
    elif re.match('B|R', a):
        if len(b) == 0:
            return y
        else:
            return fun(b, x + math.ceil((y-x)/2), y)
print('SOMETHING')
print(fun('FBFBBFF',0,127) == 44)
print(fun('RLR',0,7) == 5)
print('SOMETHING')
print('SOMETHING')
print(fun('BFFFBBF',0,127) == 70)
print(fun('RRR',0,7) == 7)
print('SOMETHING')
print('SOMETHING')
print(fun('FFFBBBF',0,127) == 14)
print(fun('RRR',0,7) == 7)
print('SOMETHING')
print(fun('BBFFBBF',0,127) == 102)
print(fun('RLL',0,7) == 4)
m = 0

print(data[0][:7])
print(data[0][7:])

for x in data:
    m = max(fun(x[:7],0,127) * 8 + fun(x[7:],0,7),m)

print(m)

y = []

for x in data:
    y.append(fun(x[:7],0,127) * 8 + fun(x[7:],0,7))

y.sort()


i = 0
print(y)
y = list(set(y))

print(y)


while i < len(y) - 1:
    if (y[i+1] - y[i] == 2):
        print(y[i] + 1)
    i += 1