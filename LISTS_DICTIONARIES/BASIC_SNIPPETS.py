# Lists-Sequence of element sets with similar/dissimilar datatypes
print("LISTS")
print("")

States_Of_America = ["Alaska", "Arizona", "Georgia"]
# Offset/Shift/Index value through which each item identification can be done
print("ACCESS ELEMENTS")
print(States_Of_America[0])

# Extract last item from list
print("ACCESS LAST ELEMENT")
print(States_Of_America[-1])

# Alter list contents
States_Of_America[1] = "Ohio"
print("UPDATE ELEMENT SET")
print(States_Of_America)

# Single value addition-Append items to end of list
States_Of_America.append("North Carolina")
print("APPEND ELEMENT SET VALUES")
print(States_Of_America)

# Multiple value addition-Extend items to existing list
States_Of_America.extend(["Washington", "New Jersey"])
print("EXTEND ELEMENTS TO EXISTING LIST")
print(States_Of_America)

# Insert item at a particular offset
States_Of_America.insert(1, "California")
print("INSERT AN ELEMENT TO EXISTING LIST")
print(States_Of_America)

# List within a list
vegetables = ["Cabbage", "Beetroot", "Potato", "Bottle guard"]
fruits = ["Cherry", "Kiwi", "Strawberry", "Durian"]
combo_list = [vegetables, fruits]
print("NESTED LIST")
print(combo_list)

# Single value extraction-[list index][offset value]
print("ACCESS ELEMENT SET FOR NESTED LIST")
print(combo_list[1][1])
print("")
print("****************************************************************************************")
print("****************************************************************************************")
print("")

# Dictionary - Mutable/Immutable data structures to store key-value pair
print("DICTIONARY")
print("")
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Bug"])
print("")
print("****************************************************************************************")
print("****************************************************************************************")
print("")

# Adding new items to existing dictionary set
print("ADD/UPDATE DICTIONARY SET")
print("")
programming_dictionary["Bug"] = "A moth in a program"
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)
print("")
print("****************************************************************************************")
print("****************************************************************************************")
print("")

# #Creating an empty dictionary
# print("INITIALIZE EMPTY DICTIONARY")
# print("")
# empty_dictionary = {}
# print(empty_dictionary)
# print("")

# #Wipe out existing dictionary
# print("WIPE OUT EXISTING DICTIONARY")
# print("")
# programming_dictionary = {}
# print(programming_dictionary)
# print("")
# print("****************************************************************************************")
# print("****************************************************************************************")
# print("")

# Loop through dictionary
print("KEY-VALUE PAIR EXTRACTION")
print("")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
print("")
print("****************************************************************************************")
print("****************************************************************************************")
print("")

# Nesting a dictionary/list within a dictionary
print("NESTED DICTIONARY")
print("")
travel_log = {
    "France": {
        "cities visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 20
    },
    "Germany": {
        "cities visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 25
    }
}
print("ACTUAL DICTIONARY")
print(travel_log)
print("ELEMENT ACCESS")
print(travel_log["France"])
print("")
print("****************************************************************************************")
print("****************************************************************************************")
print("")

# Nesting a dictionary within a list
print("NESTED LIST")
print("")
travel_log = [
    {
        "country": "France",
        "cities visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 20
    },
    {
        "country": "Germany",
        "cities visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 25
    }
]
print("ACTUAL LIST")
print(travel_log)
print("ELEMENT ACCESS")
print(travel_log[0])
print("ELEMENT VALUE ACCESS")
print(travel_log[0]["country"])
