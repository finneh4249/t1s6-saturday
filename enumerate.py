animals = ['cat', 'dog', 'rabbit', 'horse', 'giraffe']

for index, animal in enumerate(animals):
    print(f"{index}:{animal}")
    
fruits = ['apple', 'banana', 'cherry', 'date', 'grape', 'kiwi']

print('\n')

# Using for, if, break, and enumerate
target = 'cherry'

for index, fruit in enumerate(fruits):
    if fruit == target:
        print(f"Found {target} at index {index}")
        break