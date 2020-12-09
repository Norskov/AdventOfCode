import re
data = [x.rstrip() for x in open("8").readlines()]

print(data)

mData = []

for x in data:
    s = x.split(' ')
    mData.append((s[0],s[1],0))
    i = 2
    while i < len(s):
        if re.match('[0-9]+', s[i]):
            nc = s[i + 1] + ' ' + s[i + 2]
        i += 1

def do(fData, i, acc, done):
    if i == len(fData):
        return acc, True
    t = fData[i]
    if t[2] > 0:
        return acc, done
    fData[i] = (t[0],t[1],t[2]+1)
    if t[0] == 'acc':
        acc += int(t[1])
        return do(fData, i+1, acc, done)
    elif t[0] == 'jmp':
        i += int(t[1])
        return do(fData, i, acc, done)
    elif t[0] == 'nop':
        return do(fData, i+1, acc, done)
    raise ValueError('Uknown operator')

print(mData)
count = 0


#print(do(mData,0,0,False)) Solution to 1st part

j = 0

while j < len(mData):
    nData = mData.copy()
    if nData[j][0] == 'jmp':
        nData[j] = ('nop', nData[j][1], 0)
    elif nData[j][0] == 'nop':
        nData[j] = ('jmp', nData[j][1], 0)
    r = do(nData, 0, 0, False)
    if r[1]:
        print(r[0])
    j += 1