lst = list()
counts = dict()


###
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

###
print(sorted([(v, k) for k, v in counts.items()]))