data = [int(x.rstrip()) for x in open("9").readlines()]

def check(num, data, preamble):
    if len(data) < preamble:
        return True
    for i in range(min(preamble,len(data))):
        for j in range(i+1,min(preamble,len(data))):
            if num == data[i] + data[j]:
                return True
    return False

def getSet(num, data):
    for i in range(len(data)):
        sum = data[i]
        set = [data[i]]
        for j in range(i+1,len(data)):
            sum += data[j]
            if sum <= num:
                set.append(data[j])
            if sum == num:
                return set
    raise EOFError

for i,x in enumerate(data):
    if not check(x, data[i-25:i], 25):
        print('Answer to part 1: ' + str(x))
        res = getSet(x, data)
        res.sort()
        print('Answer to part 2: ' + str(res[0]) + ' and ' + str(res[-1]) + ' = ' + str(res[0] + res[-1]))
