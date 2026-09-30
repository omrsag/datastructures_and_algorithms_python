fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
list = []
for line in fh:
    if line.lower().startswith("from "):
        line = line.rstrip()
        list.append(line.split()[1])
        count += 1
        print(line.split()[1])

    
print("There were", count, "lines in the file with From as the first word")
