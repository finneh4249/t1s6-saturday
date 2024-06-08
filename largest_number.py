numbers = [3, 41, 12, 9, 74, 15]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("\t The largest number is:", largest)

# Non-class note: 
# This can be completed using the max() function but I'm following along with the class for sanity.