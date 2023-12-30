# Please do not use the existing built-in functions
# Compute Average_Height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
total_number = 0
for student_height in student_heights:
    total_height += student_height
for number in student_heights:
    total_number += 1
average_height = total_height / total_number
print(f"Average Height : ", round(average_height))

# Compute Highest_Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for student_score in student_scores:
    if student_score > highest_score:
        highest_score = student_score
print(f"Highest Score : {highest_score}")
