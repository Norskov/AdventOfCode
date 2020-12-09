import re

data = [x.rstrip() for x in open("4").readlines()]

print(data)
i=0

byr=False
iyr=False
eyr=False
hgt=False
hcl=False
ecl=False
pid=False
cid=False

count = 0

while (i < len(data)):
    if (data[i] == ''):
        byr=False
        iyr=False
        eyr=False
        hgt=False
        hcl=False
        ecl=False
        pid=False
        cid=False
    else:
        val = data[i].split(':')[1]
        ident = data[i].split(':')[0]
    if ident == 'byr' and 1920 <= int(val) <= 2002:
        byr = True
    elif ident == 'iyr' and 2010 <= int(val) <= 2020:
        iyr = True
    elif ident == 'eyr' and 2020 <= int(val) <= 2030:
        eyr = True
    elif ident == 'hgt' and re.match('[0-9]*(cm|in)$', val):
        height = int(val[0:-2])
        type = val[-2:]
        if (type == 'cm' and 150 <= height <= 193) or (type == 'in' and 59 <= height <= 76):
            hgt = True
    elif ident == 'hcl' and re.match('#[0-9a-f]{6}$', val):
        hcl = True
    elif ident == 'ecl' and re.match('(amb|blu|brn|gry|grn|hzl|oth)$', val):
        ecl = True
    elif ident == 'pid' and re.match('[0-9]{9}$', val):
        pid = True
    elif ident == 'cid':
        cid = True

    if(byr and iyr and eyr and hgt and hcl and ecl and pid):
        byr=False
        iyr=False
        eyr=False
        hgt=False
        hcl=False
        ecl=False
        pid=False
        cid=False
        count += 1
    i+=1

print(count)