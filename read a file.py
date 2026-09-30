fname = input('Enter file name: ')

try:
    text = open(fname, 'r')
except:
    print(f'error, {fname} not found')
    quit()

for x in text:
    print(f'{x}', end='')

print('\nhello', end=' ')
print('how are you?', end=' ')
print('I am fine', end=' ')
print('I am learning python')