# Range arguments (start, stop, step)

# print(range(5,10,1))
# range(5, 10)

# For loop in a range

for each in range(1,10):
    print(each)

print('\n')

for each in range(10,5,-1):
    print(each)
    
print('\n')

# For loop in a list
fruits = ["Apple", "Banana", "Cherry"]

for each in fruits:
    print(each)
    
print('\n')

#For loop with string
for each in "CoderAcademy":
    print(each)
    
print('\n')

for i in range(len(fruits)):
    print(f"Index {i} is {fruits[i]}")