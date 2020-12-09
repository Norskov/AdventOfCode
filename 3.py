data = [list(x.rstrip()) for x in open("3").readlines()]

print(data[0])


def slope(x,y):

    count = 0
    i = 0
    j = 0

    while i < len(data):
        while (len(data[i]) < j + 1):
            data[i].extend(data[i])
        if (data[i][j] == '#'):
            count +=1
        i += x
        j += y

    return count

print(slope(1,1))
print(slope(1,3))
print(slope(1,5))
print(slope(1,7))
print(slope(2,1))