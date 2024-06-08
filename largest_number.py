numbers = [3, 41, 12, 9, 74, 15]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("\t The largest number is:", largest)