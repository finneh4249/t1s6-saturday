# country1= "Australia"
# country2= "India"
# country3= "New Zealand"
# country4= "England"

# print(country1)
# print(country2)
# print(country3)
# print(country4)

# list of countries
country_list = ["Australia", "India", "New Zealand", "England"]
# print the list
print(country_list)
# print the second element in the list (India)
print(country_list[1])

# change the second element in the list (India) to Nepal
country_list[1] = "Nepal"
# print the updated list
print(country_list)

# append Japan to the list
country_list.append('Japan')
# print the updated list
print(country_list)

# remove England from the list
country_list.remove('England')
# print the updated list
print(country_list)

# print the total number of elements in the list
print("Total length of the list: ", len(country_list))
