# Input couple names
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Contatination of both the names with lowercase string
result_set = name1 + name2
converted_result_set = result_set.lower()
print(converted_result_set)

# Character count extraction-TRUE
t = converted_result_set.count("t");
r = converted_result_set.count("r");
u = converted_result_set.count("u");
e = converted_result_set.count("e");

true_count = t + r + u + e

# Character count extraction-LOVE
l = converted_result_set.count("l");
o = converted_result_set.count("o");
v = converted_result_set.count("v");
e = converted_result_set.count("e");

love_count = l + o + v + e

# Concatenation of two counts
love_score = str(true_count) + str(love_count)
love_score = int(love_score)

# Calculation of love score
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")
