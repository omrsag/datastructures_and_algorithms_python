fname = input("Enter file name: ")
fh = open(fname)
lst = list()
a = list()

for line in fh:
    line = line.rstrip()
    a = line.split()

    for check in a:
        if len(lst) == 0:
            lst.append(check)
            continue

        for x in lst:
            if check.upper() == x.upper():
                break
            if check.upper() != x.upper() and lst.index(x) == len(lst)-1:
                lst.append(check)
                lst.sort()
                break

for x in lst:
    for y in lst:
        if lst.index(x) != lst.index(y) and x.upper() == y.upper():
            del lst[y]

print(lst)