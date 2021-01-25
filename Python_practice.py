print("Hello World")
counties = ["arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver' :
    print(counties[1])

counties = [ "Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties :
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not the list of counties.")
for county in counties:
    print(county)
numbers = [0, 1, 2, 3, 4]
for num in numbers :
    print(num)
for i in range(len(counties)) :
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438} 
for county in counties_dict:
    print(counties_dict[county])
voting_data = [{"county":"Arapahoe","registered_voters": 422829},
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}]
for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


import csv
dir(csv)
