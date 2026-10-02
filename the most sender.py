name = input("Enter file:")
hilo = dict()
lastv = 0
lastk = ""

if len(name) < 1:
    name = "text.txt"
    
handle = open(name)
for line in handle:
    line = line.rstrip()
    if line.lower().startswith("from"):
        hilo[line.split()[1]] = hilo.get(line.split()[1], 0)+1
        
for key,value in hilo.items():
    if value > lastv:
        lastv = value
        lastk = key

print(lastk,lastv)