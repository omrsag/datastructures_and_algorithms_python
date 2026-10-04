name = input("Enter file:")
lst = list()
dict = dict()
num = "test"
if len(name) < 1:
    name = "text.txt"
handle = open(name)
for line in handle:
    if line.lower().startswith("from"):
        line = line.rstrip()
        lst = line.split(":")
        try:
            num = int(lst[0][-2:])
        except:
            continue
        dict[lst[0][-2:]] = dict.get(lst[0][-2:], 0) + 1
            
lst = sorted([(k,v) for k,v in dict.items()])
for k,v in lst:
    print(k,v)