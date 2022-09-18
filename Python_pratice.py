print("Hello World")
print("Hello Earth")

counties = ["Arapahoe","Denver","Jefferson"]

if counties[1] == 'Denver':
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties")

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in counties_dict.values():
        print(value)

for county_dict in voting_data:
    for county, value in county_dict.items():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])


# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes *100} % of the total votes.")

# # Using F-strings w Dictionaries.This is used to print each county and
# registered voter from the counties dictionary. Using concatenation.

# counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
# #     print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")


# # # Multiline F-Strings

# candidates_votes = int(input("How many votes did the candidate get in the election?"))
# total_votes = int(input("What is the total number of votes in the election?"))
# message_to_candidate = (

#     f"You received {candidates_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}."
#     f"You received {candidates_votes / total_votes * 100:.2f}%  of the total votes. ")

# print(message_to_candidate)

# Format Floating-Point Decimals

# In the format, the width specifies the number of characters used to display the value.
# However, if a value needs more space than the width specifies, the additional space is used.
# The precision indicates the number of decimal places to format the value. 
# For example, to format the interest to two decimal places, we would use .2f
# where f means "floating-point decimal format". When formatting a number,
# we can also add a thousands separator with a comma, using the following format. 
# The comma is placed after the {width}: 
# f'{value:{width},.{precision}}'

# SKILL DRILL

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")


#Import the datetime class from the datetime module.

import datetime as dt

# Use the now() attribute on the datetime class to get the present time.

now = dt.datetime.now()

# Print the present time.

print( "The time right now is ", now)



