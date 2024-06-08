stars = 5

# *
# **
# ***
# ****
# *****

for i in range(1, stars+1):
    for j in range(i):
        print("*", end="")
    print()
    
print("\n")
    
# Create a Square Pattern with stars

# *****
# *   *
# *   *
# *****

for i in range(1, stars+1):
    for j in range(stars):
        if i == 1 or i == stars or j == 0 or j == stars-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    