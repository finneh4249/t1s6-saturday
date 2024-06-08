i = 0

#break loop
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break

print('\n')
i = 0
#continue loop
while i < 5:
    print(i)
    i += 1
    if i == 3:
        continue
    
print('\n')


# skipping vowels from text using continue

text = "Coder Academy"
vowels = "aeiouAEIOU"

for each in text:
    if each in vowels:
        continue
    print(each, end="")
print()

print('\n')

#

signals = ['start','halt', 'continue', 'start', 'stop', 'hold', 'halt', 'go']

for signal in signals:
    if signal == 'stop':
        break
    print(signal)