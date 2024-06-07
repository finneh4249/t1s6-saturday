# country1= "Australia"
# country2= "India"
# country3= "New Zealand"
# country4= "England"

# print(country1)
# print(country2)
# print(country3)
# print(country4)

country_list = ["Australia", "India", "New Zealand", "England"]
print(country_list)
print(country_list[1])

country_list[1] = "Nepal"
print(country_list)

country_list.append('Japan')
print(country_list)

country_list.remove('England')
print(country_list)

print("Total length of the list: ", len(country_list))